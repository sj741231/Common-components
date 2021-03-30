from common.mysql_conn import MySQLClient

USER = 'root'
PASSWORD = 'ZAQ!2wsx'
DATABASE = 'hc_cmdb'



def get_mysql_user(dbconn, user=None, **kwargs):

    _ip = dbconn.ip
    _port = int(dbconn.port) if str(dbconn.port).strip().isdigit() else 3306
    _user = str(user).strip() if user and str(user).strip() else None

    db_args = {
        'host': _ip,
        'port': _port,
        'user': USER,
        'password': PASSWORD,
        'database': DATABASE,
        'charset': 'utf8',
    }

    if _user:
        sql = """select user, host, password_expired, password_last_changed from mysql.user where user = %s;"""
        args = (_user,)
    else:
        sql = """select user, host, password_expired, password_last_changed from mysql.user;"""
        args = None

    print("11 ### sql args:", sql, args)
    with MySQLClient(**db_args) as db:
        print("22 ### db_args:", db_args)
        result = db.select(sql, args)
        print("33 ### result: ", result)

        for i in result:
            i['password_last_changed'] = i['password_last_changed'] .strftime("%Y-%m-%d %H:%M:%S") if i.get('password_last_changed') else ''
        return result