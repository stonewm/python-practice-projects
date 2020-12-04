from win32com.client import Dispatch
from ADOWrapper.adoconstants import *


class RecordSetWrapper(object):
    def __init__(self):
        pass

    @staticmethod
    def rst_to_list(recordset):
        """
        Convert recordset to list
        """

        result = []

        if not (recordset.BOF and recordset.EOF):
            # header line
            header = []
            for idx in range(recordset.Fields.Count):
                header.append(recordset.Fields(idx).Name)
            result.append(header)

            # line items
            # Python对于数据库的NULL值自动转换成None
            recordset.MoveFirst()
            while not recordset.EOF:
                item = []
                for idx in range(recordset.Fields.Count):
                    item.append(str(recordset.Fields(idx)))
                result.append(item)
                recordset.MoveNext()

        return result

    @staticmethod
    def query(conn, sql):
        rst = Dispatch("ADODB.Recordset")
        result = []

        try:
            if conn.state != adStateOpen:
                conn.Open()

            rst.Open(sql, conn, adOpenKeyset, adLockReadOnly)

            result = RecordSetWrapper.rst_to_list(rst)
        except Exception as ex:
            print(ex)
            for err in conn.Errors:
                print(err.Description)
        finally:
            rst.Close()
            conn.Close()

        return result

    @staticmethod
    def get_recordset(conn, sql):
        rst = Dispatch("ADODB.Recordset")
        conn.Open()
        rst.Open(sql, conn, adOpenKeyset, adLockReadOnly)
        return rst


    @staticmethod
    def to_excel(recordset, excel_file, replace = False):
        # create excel file
        excel_app = Dispatch("Excel.Application")
        excel_app.Visible = True

        try:
            work_book = excel_app.Workbooks.Add()
            target_sheet = work_book.ActiveSheet

            # copy recordset header
            for idx in range(0, recordset.Fields.Count):
                target_sheet.cells(1, idx+1).Value = recordset.Fields(idx).Name

            # copy recordset lines
            target_sheet.Range("A2").CopyFromRecordSet(recordset)

            print("导出成功！")
        finally:
            recordset.Close()
