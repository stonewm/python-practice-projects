from win32com.client import Dispatch
from . import error_handler
from . import adoconstants


class CommandWrapper(object):

    @staticmethod
    def execute(conn, sql):
        cmd = Dispatch("ADODB.Command")

        try:
            conn.Open()
            cmd.ActiveConnection = conn
            cmd.CommandText = sql

            cmd.execute()
        except Exception as ex:
            print(ex)
            for err in conn.Errors:
                error_handler.print_error(err)
        finally:
            if conn.State == adoconstants.adStateOpen:
                conn.Close()
