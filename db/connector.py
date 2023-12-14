import pymysql
import psycopg2
from sqlalchemy import create_engine
class DBConnector:
    def __init__(self, host,user,password,database,port,engine):
        self.engine = engine
        
        if self.engine == "postgresql":
        
            self.postgre_params = dict(
                                    host = host,
                                    dbname = database,
                                    user = user,
                                    password = password,
                                    port  = int(port)
                                    )
            self.connect = self.postgre_conn()
            self.orm_conn_params = f'{engine}://{user}:{password}@{host}:{port}/{database}'
            self.orm_connect = self.orm_postgre_conn()
            
        elif self.engine == "mysql":
            self.mysql_params = dict(
                                    host = host,
                                    db = database,
                                    user = user,
                                    password = password,
                                    port  = int(port),
                                    charset = 'utf8'
                                    )
            self.connect = self.mysql_conn()
            
    
    def __enter__(self):
        print("Success Connect")
        # self.connect
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        self.conn.close()
        print("Success DisConnect")
    
    def postgre_conn(self):
        self.conn = psycopg2.connect(**self.postgre_params)

    def mysql_conn(self):
        self.conn = pymysql.connect(**self.mysql_params)

    def orm_postgre_conn(self):
        self.orm_conn = create_engine(self.orm_conn_params)
    # def get_query(self,table_name):
    #     _query = self.queries[table_name]
    #     return _query
        
    
