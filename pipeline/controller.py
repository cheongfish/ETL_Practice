import os
import pandas as pd

from settings import DB_SETTINGS,TEMP_PATH

from db.connector import DBConnector
from db.mysql_query import select_query
from db.postgresql_query import queries



from pipeline.extract import extractor
from pipeline.transform import get_path,preprocessing
from pipeline.load import to_other_dbms_sql, to_other_dbms_engine


from utils import make_table,make_temp_storage,get_batch_date,remover

batch_date = get_batch_date()
table_name = select_query.split(' ')[-1]
#########################################################################################################


def main(batch_date):
    # 임시 저장소 만들기
    make_temp_storage(TEMP_PATH)
    # 이관할 테이블 만들기
    db_postgre= DBConnector(**DB_SETTINGS['POSTGRES'])
    make_table(db_postgre, queries['make_table_query'])
    
    
    # Mysql에서 이관할 데이터 추출하기
    db_mysql = DBConnector(**DB_SETTINGS['MYSQL'])
    extracted_df = extractor(db_mysql,select_query)
    
    
    df = preprocessing(extracted_df)
    res, path = get_path(df,batch_date,TEMP_PATH,table_name)
    

    
    # Mysql -> Postgresql By Query(INSERT)
    to_other_dbms_sql(db_postgre,path,queries['INSERT_query'])

    # Mysql -> Postgresql By sqlalchemy engine
    to_other_dbms_engine(db_postgre,path)
    
    # 작업 종료후 임시 저장소 삭제 후 재생성
    remover(TEMP_PATH)
    