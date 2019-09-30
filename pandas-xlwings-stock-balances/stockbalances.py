import xlwings as xw
import pandas as pd
import numpy as np
from sqlalchemy import create_engine


def do_get_stock_balances(year, month):
    """
    year: int type, selection criterion for transaction year
    month: int type, selection criterion for transaction month
    """

    year = int(year)
    month = int(month)

    engine = create_engine('mssql+pyodbc://sa:pwd!@mssql')


    df_details = pd.read_sql(
        'select DocNo, MaterialNo, Qty from dbo.stock_movement_details',  engine)

    df_headers = pd.read_sql(
        'select DocNo, DocDate, MovementType from dbo.stock_movement_headers',  engine)

    df_mvt_type = pd.read_sql(
        'select MovementTypeID, InoutSign from dbo.movement_types', engine)

    # merge columns
    df_merged_headers = df_details.merge(df_headers, on='DocNo')
    df = df_merged_headers.merge(
        df_mvt_type, left_on='MovementType', right_on='MovementTypeID')

    # add columns
    df['TxYear'] = df.DocDate.dt.year
    df['TxMonth'] = df.DocDate.dt.month
    df['ActualQty'] = np.where(
        df.InoutSign == "+",
        df.Qty,
        -1 * df.Qty
    )

    df['BeginQty'] = np.where(
        df.TxYear < year,
        df.ActualQty,
        (np.where(
            (df.TxYear == year) & (df.TxMonth < month),
            df.ActualQty,
            0
        ))
    )

    df['StockIn'] = np.where(
        (df.TxYear == year) & (df.TxMonth == month) & (df.InoutSign == "+"),
        df.ActualQty,
        0
    )

    df['StockOut'] = np.where(
        (df.TxYear == year) & (df.TxMonth == month) & (df.InoutSign == "-"),
        df.ActualQty,
        0
    )

    df['EndQty'] = df.BeginQty + df.StockIn + df.StockOut

    # grouped by materialNo and then calculate total
    df_grouped = df[['MaterialNo', 'BeginQty', 'StockIn',
                     'StockOut', 'EndQty']].groupby('MaterialNo').sum()

    df = df_grouped

    # remove empty rows
    df = df.drop(
        df[(df.BeginQty == 0) & (df.StockIn == 0) & (df.StockOut == 0)].index
    )

    return df


def get_stock_balances(year, month):
    df = do_get_stock_balances(year, month)
    wb = xw.Book.caller()
    wb.sheets["Sheet1"].range("A1").options(index=True).value = df
