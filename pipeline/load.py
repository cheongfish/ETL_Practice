import os
import pandas as pd
    
def to_other_dbms_sql(db_connector,path,sql):
    with db_connector as connected:
        con = connected.conn
        cursor = con.cursor()
        df = pd.read_parquet(path)
        for row in df.iterrows():
            
            cursor.execute(sql,(row[1]['ID'],
                                      row[1]["Name"],
                                      row[1]["CountryCode"],
                                      row[1]["District"],
                                      row[1]["Population"]
                                      )
                           )
        con.commit()
    print("Insert to psql by sql complete")


def to_other_dbms_engine(db_connector,path):
    df = pd.read_parquet(path)
    with db_connector as connected:
        con = connected.orm_conn
        df.to_sql('TEST2',con,if_exists='append', index = False)
    print("Insert to psql by sql_engine complete")
    