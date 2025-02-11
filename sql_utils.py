import psycopg2
from psycopg2 import sql

def connect_to_postgres(username, password, url, port, db_name):
    try:
        connection = psycopg2.connect(
            dbname=db_name,
            user=username,
            password=password,
            host=url,
            port=port
        )
        
        print("Подключено")
        
        return connection

    except Exception as ex:
        print(f"Ошибка подключения: {ex}")
        return None



def sql_to_df(username, password, url, port, db_name, query):
    con = connect_to_postgres(username, password, url, port, db_name)
    if con:
        df = pd.read_sql_query(query, con)
        return df
    else:
        print('Не удалось подключиться')
        return None