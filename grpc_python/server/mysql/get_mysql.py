from common.mysql_conn import MySQLClient

USER = 'root'
PASSWORD = 'ZAQ!2wsx'
DATABASE = 'hc_cmdb'


def get_mysql_info(dbconn, database=None, **kwargs):
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
        sql = "select table_schema, COUNT(table_schema) as table_count, \
		       truncate(sum(IFNULL(data_length,0) + IFNULL(index_length,0))/1024/1024,3) as total_size, \
		       truncate(sum(data_length)/1024/1024,3) as data_size, \
               truncate(sum(index_length)/1024/1024,3) as index_size \
               from information_schema.tables where table_schema = %s group by table_schema order by data_size desc;"
        args = (_database,)
    else:
        sql = "select table_schema, COUNT(table_schema) as table_count, \
		       truncate(sum(IFNULL(data_length,0) + IFNULL(index_length,0))/1024/1024,3) as total_size, \
		       truncate(sum(data_length)/1024/1024,3) as data_size, \
               truncate(sum(index_length)/1024/1024,3) as index_size \
               from information_schema.tables group by table_schema order by data_size desc;"
        args = None

    with MySQLClient(**db_args) as db:
        # print("### db_args:", db_args)
        # print("### sql args:", sql, args)
        result = db.select(sql, args)
        # print("### result: ", result)
        return result
