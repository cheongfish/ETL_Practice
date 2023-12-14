import os
import dotenv

env_path = dotenv.find_dotenv()
dotenv.load_dotenv(env_path)

DB_SETTINGS = {
    "MYSQL" : { 
                "engine" : os.environ.get("MYSQL_ENGINE"),
                "host" : os.environ.get("MYSQL_HOST"),
                "user" : os.environ.get("MYSQL_ID"),
                "password" : os.environ.get("MYSQL_PW"),
                "port" : os.environ.get("MYSQL_PORT"),
                "database" : os.environ.get("MYSQL_DB_1"),
                },
    "POSTGRES" : { 
                "engine" : os.environ.get("POSTGRES_ENGINE"),
                "host" : os.environ.get("POSTGRES_HOST"),
                "user" : os.environ.get("POSTGRES_ID"),
                "password" : os.environ.get("POSTGRES_PW"),
                "port" : os.environ.get("POSTGRES_PORT"),
                "database" : os.environ.get("POSTGRES_DB")
                }
    }

TEMP_PATH= "./temp_storage"
    