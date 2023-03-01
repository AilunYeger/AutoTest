import pymysql
DB_CONF = {
    "host": "127.0.0.1",
    "port": 13306,
    "user": "root",
    "password": "123456",
    "db": "DRF_Demo"
}

def txc(**kwargs):
    print(kwargs)


txc(**DB_CONF)


