import os, shutil

from datetime import datetime
from db.mysql_query import select_query

def make_table(db_obj , query):
    for _query in query:
        with db_obj.conn as connected:
            cursor  = connected.cursor()
            cursor.execute(_query)
    

def make_temp_storage(storage_name):
    _path = os.path.join(os.getcwd(), storage_name)
    if os.path.exists(_path):
        print("Already temp_storage exists")
        pass
    else:
        os.makedirs(_path)
        print("Complete make temp storage")
        
        
def get_batch_date():
    today = datetime.now()
    batch_date = today.strftime('%Y%m%d')
    return batch_date
    
    

def remover(path):
    # 임시저장된 폴더 지우기
    shutil.rmtree(path)
    # 스테이징 스토리지 생성
    os.makedirs(path)
    

