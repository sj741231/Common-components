from concurrent import futures
import logging
import traceback

import grpc

import mysql_grpc_pb2
import mysql_grpc_pb2_grpc

# from common.mysql_conn import MySQLClient
# from . import mysql_rpc_pb2, mysql_rpc_pb2_grpc

from get_users import get_mysql_user
from get_mysql import get_mysql_info
from get_database import get_database_details

try:
    names = globals()
    if names.get('logger', None) is None:
        logging.basicConfig(filename='mysqlclient.log',
                            format='%(asctime)s -%(name)s-%(levelname)s-%(module)s.%(funcName)s:%(lineno)d:%(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S %p',
                            level=logging.DEBUG)
        logger = logging.getLogger()
except:
    raise

class MySQLGRPC(mysql_grpc_pb2_grpc.MySQLGRPCServicer):

    def GetUsers(self, request, context):
        try:
            # raise Exception("unknown error")
            # print("request.dbconn: ", request.dbconn)
            # print("request.user: ", request.user)

            _result = get_mysql_user(request.dbconn, request.user)

            response = dict(dbconn=request.dbconn, result=_result)
            # print("response: ", response)
            return mysql_grpc_pb2.UsersResponse(**response)
        except ValueError as e:
            logger.error("GetUsers ValueError: {e}".format(e=traceback.format_exc()))
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details(str(e))
            raise
        except Exception as e:
            logger.error("GetUsers ValueError: {e}".format(e=traceback.format_exc()))
            context.set_code(grpc.StatusCode.UNKNOWN)
            context.set_details(str(e))
            raise

    def GetMySQL(self, request, context):
        try:
            print("request.dbconn: ", request.dbconn)
            print("request.database: ", request.database)

            _result = get_mysql_info(request.dbconn, request.database)

            response = dict(dbconn=request.dbconn, result=_result)
            print("response: ", response)
            return mysql_grpc_pb2.MySQLResponse(**response)
        except ValueError as e:
            logger.error("GetMySQL ValueError: {e}".format(e=traceback.format_exc()))
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details(str(e))
            raise
        except Exception as e:
            logger.error("GetMySQL ValueError: {e}".format(e=traceback.format_exc()))
            context.set_code(grpc.StatusCode.UNKNOWN)
            context.set_details(str(e))

    def GetDatabase(self, request, context):
        try:
            print("request.dbconn: ", request.dbconn)
            print("request.database: ", request.database)

            _result = get_database_details(request.dbconn, request.database)

            response = dict(dbconn=request.dbconn, result=_result)
            print("response: ", response)
            return mysql_grpc_pb2.DatabaseResponse(**response)
        except ValueError as e:
            logger.error("GetDatabase ValueError: {e}".format(e=traceback.format_exc()))
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details(str(e))
            raise
        except Exception as e:
            logger.error("GetDatabase ValueError: {e}".format(e=traceback.format_exc()))
            context.set_code(grpc.StatusCode.UNKNOWN)
            context.set_details(str(e))


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=8))
    mysql_grpc_pb2_grpc.add_MySQLGRPCServicer_to_server(MySQLGRPC(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
