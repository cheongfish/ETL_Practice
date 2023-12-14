import pandas as pd
import os

def preprocessing(df:pd.DataFrame()):
    res_df = df.dropna()
    res_df.reset_index(inplace = True,drop = True)
    return res_df

def get_path(df,batch_date,temp_path,table_name):
    
    path = create_path(temp_path,table_name,batch_date)
        
    res,save_path = save_to_file(df,path,table_name)
    
    return res , save_path


def create_path(temp_path,table_name,batch_date):
    
    _y = batch_date[:4]
    _m = batch_date[4:6]
    _d = batch_date[6:]
    
    _path = os.path.join(temp_path,table_name,f'yyyy={_y}',f'mm={_m}', f'dd={_d}')
    return _path

def save_to_file(df,path,table_name):
    if len(df) > 0:
        os.makedirs(path, mode= 777)
        save_path = os.path.join(path, f"{table_name}.parquet")
        if os.path.exists(save_path) is True:
            print(f"{table_name}.parquet already exists")
            pass
        else:
            df.to_parquet(save_path,index = False)
        return True , save_path
    else:
        print("EMPTY FILE")
        return False 
    