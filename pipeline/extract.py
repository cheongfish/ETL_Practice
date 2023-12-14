import pandas as pd

def extractor(db_connector,sql):
    with db_connector as connected:
        con = connected.conn
        df = pd.read_sql(sql, con)
        
        return df
        

