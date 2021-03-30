import pymysql
import copy
import logging
import traceback

try:
    names = globals()
    if names.get('logger', None) is None:
        logging.basicConfig(filename='mysqllog.log',
                            format='%(asctime)s -%(name)s-%(levelname)s-%(module)s.%(funcName)s:%(lineno)d:%(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S %p',
                            level=logging.DEBUG)
        logger = logging.getLogger()
except:
    raise


def mysqlconn(host, port, user, password, database, charset='utf8', **kwargs):
    conn = pymysql.connect(host, port, user, password, database, charset, **kwargs)
    return conn


class MySQLClient(object):
    """ pymysql """

    __db_args = ('host', 'database', 'port', 'user', 'password')
    __pymysql_args = ('host', 'user', 'password', 'database', 'port', 'unix_socket',
                      'charset', 'sql_mode', 'read_default_file', 'conv', 'use_unicode',
                      'client_flag', 'cursorclass', 'init_command', 'connect_timeout', 'ssl',
                      'read_default_group', 'compress', 'named_pipe', 'autocommit', 'db', 'passwd',
                      'local_infile', 'max_allowed_packet', 'defer_connect', 'auth_plugin_map',
                      'read_timeout', 'write_timeout', 'bind_address', 'binary_prefix', 'program_name',
                      'server_public_key')

    def __init__(self, **kwargs):
        self.connection = None
        self.get_db_conn(**kwargs)

    def get_db_conn(self, **kwargs):
        """ get mysql db conn """
        params = self.get_conn_params(**kwargs)
        self.connection = pymysql.connect(**params)
        return self.connection

    def get_conn_params(self, **kwargs):
        _params = copy.deepcopy(kwargs)
        _params['database'] = _params['database'] if _params.get('database') else _params.get('db')
        _params['password'] = _params['password'] if _params.get('password') else _params.get('passwd')
        _params['charset'] = _params['charset'] if _params.get('charset') and str(
            _params.get('charset')).strip() else _params.get('utf8')

        try:
            # 使用 difference 求a与b的差(补)集：求a中有而b中没有的元素
            missing_params = list(set(self.__db_args).difference(set(_params.keys())))
            if missing_params:
                raise ValueError("Miss required params: {p}".format(p=','.join(missing_params)))

            for k in kwargs.keys():
                if k not in self.__pymysql_args:
                    _params.pop(k)
                else:
                    if getattr(self, '_check_{p}'.format(p=k), None):
                        func = getattr(self, '_check_{p}'.format(p=k), None)
                        _params[k] = func(**_params)
            return _params
        except:
            logger.error("get_conn_params error: {e}".format(e=traceback.format_exc()))
            raise

    def _check_port(self, port, **kwargs):
        """ check db port """
        try:
            return int(port)
        except:
            raise ValueError("port '{p}' invalid".format(p=str(port)))

    def _check_host(self, host, **kwargs):
        """ check db host """
        try:
            if host and str(host).strip():
                return str(host).strip()
            else:
                raise ValueError("host '{p}' invalid".format(p=str(host)))
        except:
            raise

    def switch_database(self, database):
        self.connection.select_db(database)
        self.connection.commit()
        return self.connection.cursor()

    def get_cursor(self, cursor=None):
        # self.connection.ping()
        return self.connection.cursor(cursor)

    def select(self, sql, args=None):
        """
        :param query: query is dict: {'query':sql4, "args":("mysql",)}
                      or tuple or list: [sql4, ['vsa',]] or [sql4, ('vsa',)]
        :return:
        """
        cur = self.get_cursor(cursor=pymysql.cursors.DictCursor)
        try:
            pymysql_params = self.check_sql_params(sql, args)
            print("*** 111 pymysql_params:", pymysql_params)
            # _q = cur.mogrify(**pymysql_params)
            cur.execute(**pymysql_params)
            # dsc = cur.description
            # dsc = [d[0] for d in dsc]
            rst = cur.fetchall()
            return rst
            # return [dict(zip(dsc, r)) for r in rst]
        except:
            print(traceback.format_exc())
            logger.error("select error: {e}".format(e=traceback.format_exc()))
        finally:
            cur.close()
            self.connection.commit()

    # def create_database(self, db):
    #     return self.execute(MySQL_CreateDataBase_SQL.format(db=db))
    #
    # def drop_database(self, db):
    #     return self.execute(MySQL_DropDataBase_SQL.format(db=db))

    def get_sql_params_dict(self, sql):
        """ check param that sql is dict """
        pymysql_params = dict()
        if sql.get('query'):
            pymysql_params['query'] = sql.get('query')
        else:
            raise ValueError("get_sql_params_dict param {s} query invalid".format(s=str(sql)))

        if sql.get('args'):
            if isinstance(sql.get('args'), (list, tuple)):
                pymysql_params['args'] = sql.get('args')
            else:
                raise ValueError("get_sql_params_dict param {s} args {s} invalid".format(s=str(sql)))
        return pymysql_params

    def get_sql_params_list(self, sql):
        """ check param that sql is list """
        pymysql_params = dict()
        print("sql: ", sql)
        print("len: ", len(sql))
        if len(sql) == 1:
            pymysql_params['query'] = sql[0]
        elif len(sql) > 1 and isinstance(sql[1], (list, tuple)):
            pymysql_params['query'] = sql[0]
            pymysql_params['args'] = sql[1]
        else:
            raise ValueError("get_sql_params_list param {s} invalid".format(s=str(sql)))
        return pymysql_params

    def get_sql_params_string(self, sql, args=None):
        """ check param that sql is string """
        pymysql_params = dict()
        if str(sql).strip():
            pymysql_params['query'] = str(sql).strip()
        else:
            raise ValueError("get_sql_params_string param {s} query invalid".format(s=str(sql)))
        if args:
            if isinstance(args, (list, tuple)):
                pymysql_params['args'] = args
            else:
                raise ValueError("get_sql_params_string param {s} args invalid".format(s=str(args)))
        return pymysql_params

    def check_sql_params(self, sql, args=None):
        """ check sql that pymysql params"""
        if isinstance(sql, dict) and sql:
            pymysql_params = self.get_sql_params_dict(sql)
        elif isinstance(sql, list) and sql:
            pymysql_params = self.get_sql_params_list(sql)
        elif isinstance(sql, str) and sql:
            pymysql_params = self.get_sql_params_string(sql, args)
        else:
            raise ValueError("check_sql_params param sql invalid".format(s=str(sql)))
        return pymysql_params

    def execute(self, sqls):
        try:
            sql_list = list()
            if isinstance(sqls, list):
                pass
            elif isinstance(sqls, str):
                sqls = [str]
            else:
                raise ValueError("params sqls {p} invalid".format(p=str(sqls)))

            for i in sqls:
                pymysql_params = self.check_sql_params(i)
                sql_list.append(pymysql_params)
        except:
            logger.error("execute error: {e}".format(e=traceback.format_exc()))
            raise

        cur = self.get_cursor(cursor=pymysql.cursors.DictCursor)
        rows = 0
        try:
            for pymysql_params in sql_list:
                cur.execute(**pymysql_params)
                rows += cur.rowcount
        except Exception as e:
            logger.error("execute error: {e}".format(e=traceback.format_exc()))
            self.connection.rollback()
            return
        else:
            self.connection.commit()
            return rows
        finally:
            cur.close()
            # self.connection.commit()

    def close(self):
        try:
            self.get_cursor().close()
            self.connection.commit()
        except:
            logger.error("close error: {e}".format(e=traceback.format_exc()))
        finally:
            self.connection.close()

    def __enter__(self):
        print("__enter__")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("###" *30)
        print("__exit__")
        print(exc_type, exc_val, exc_tb)
        print("###" * 30)
        self.get_cursor().close()
        self.connection.commit()
        self.connection.close()
        return False


if __name__ == '__main__':
    db_args = {
        'host': '127.0.0.1',
        'port': '3306',
        'user': 'root',
        'password': 'ZAQ!2wsx',
        'database': 'hc_cmdb',
        'charset': 'utf8',
    }

    sql1 = """  select User, Host, password_expired, password_last_changed FROM mysql.user;"""
    sql2 = """  select 	table_schema, 
		COUNT(table_schema) as table_count,
		truncate(sum(IFNULL(data_length,0) + IFNULL(index_length,0))/1024/1024,2) as total_size,
		truncate(sum(data_length)/1024/1024,2) as data_size, 
        truncate(sum(index_length)/1024/1024,2) as index_size
        from information_schema.tables group by table_schema order by data_size desc;  """
    sql3 = """  select table_name, truncate(data_length/1024/1024,2) as data_size,
                truncate(index_length/1024/1024,2) as index_size from information_schema.tables 
                where table_schema = 'mysql' order by data_size desc;"""
    sql4 = """  select table_name, truncate(data_length/1024/1024,2) as data_size, 
                truncate(index_length/1024/1024,2) as index_size from information_schema.tables 
                where table_schema = %s order by data_size desc;"""

    sqls = [sql1, sql2, sql3, {'query': sql4, "args": ("mysql",)}, [sql4, ['vsa', ]]]

    with MySQLClient(**db_args) as db:
        raise ValueError("THIS IS TEST")
        # result = db.select(query=sql1)
        # print("result: ", result)
        # print("***" * 30)
        # result = db.select(query=sql2)
        # print("result: ", result)
        # print("***" * 30)
        # result = db.select(query=sql3)
        # print("result: ", result)
        print("###" * 30)
        result = db.select(sql={'query': sql4, "args": ('mysql',)})
        print("result: ", result)
        print("***" * 30)
        result = db.select(sql=[sql4, ['vsa', ]])
        print("result: ", result)
        print("###" * 30)


        # result = db.execute(sqls=sqls)
        # print("result: ", result)
        # print("***" * 30)
