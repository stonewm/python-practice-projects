from win32com.client import Dispatch

class ConnectionWrapper(object):
    def __init__(self, conn_str):
        self.connection_string = conn_str

    def get_connection(self):
        conn = Dispatch("ADODB.Connection")
        conn.ConnectionString = self.connection_string
        return conn
    
    
        
