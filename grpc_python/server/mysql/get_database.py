from common.mysql_conn import MySQLClient

USER = 'root'
PASSWORD = 'ZAQ!2wsx'
DATABASE = 'hc_cmdb'


def get_database_details(dbconn, database, **kwargs):
    _ip = dbconn.ip
    _port = int(dbconn.port) if str(dbconn.port).strip().isdigit() else 3306
    _database = str(database).strip() if database and str(database).strip() else None

    db_args = {
        'host': _ip,
        'port': _port,
        'user': USER,
        'password': PASSWORD,
        'database': DATABASE,
        'charset': 'utf8',
    }

    if _database:
        sql = " select table_name, \
                truncate((IFNULL(data_length,0) + IFNULL(index_length,0))/1024/1024,3) as total_size, \
                truncate(data_length/1024/1024,3) as data_size, \
                truncate(index_length/1024/1024,3) as index_size \
                from information_schema.tables \
                where table_schema = %s order by data_size desc;"
        args = (_database,)
    else:
        raise ValueError("param database error: {e}".format(e=str(database)))

    with MySQLClient(**db_args) as db:
        print("### db_args:", db_args)
        print("### sql args:", sql, args)
        result = db.select(sql, args)
        print("### result: ", result)
        return result
