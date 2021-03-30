"""gRPC Python helloworld.Greeter client with channel options and call timeout parameters."""

from __future__ import print_function
import logging
import re
import grpc
import traceback

import mysql_grpc_pb2
import mysql_grpc_pb2_grpc
from mysql_function import get_UsersResponse, get_MySQLResponse, get_DatabaseResponse

from google.protobuf.json_format import MessageToDict, MessageToJson

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


class CallMySQLGRPC(object):
    _channel = None

    # _pb2 = None
    # _pb2_grpc = None

    def __init__(self, **kwargs):
        """
        :param kwargs: Required, params target, options
        """
        self.get_grpc_insecure_channel(**kwargs)
        # self.get_pb2_pb2_grpc(**kwargs)

    # def get_pb2_pb2_grpc(self, pb2, pb2_grpc, **kwargs):
    #     """
    #     get_pb2_pb2_grpc
    #     :param pb2: package XXX_pb2
    #     :param pb2_grpc: package XXX_pb2_grpc
    #     :param kwargs:
    #     :return:
    #     """
    #     names = globals()
    #     if isinstance(pb2, str):
    #
    #     if names.get(pb2):
    #         self._pb2 = pb2
    #     else:
    #         raise ValueError("pb2 not found in the namespace")
    #
    #     if names.get(pb2_grpc):
    #         self._pb2_grpc = pb2_grpc
    #     else:
    #         raise ValueError("pb2_grpc not found in the namespace")

    def get_grpc_insecure_channel(self, **kwargs):
        """ get grpc insecure channel """
        print("kwargs: ", kwargs)
        channel_params = self.get_channel_params(**kwargs)
        self._channel = grpc.insecure_channel(**channel_params)
        return self._channel

    def get_channel_params(self, target, options, **kwargs):
        """
        get channel params
        :param target: example 'localhost:50051', '10.211.55.80:50051'
        :param options: channel options, For more channel options, please see https://grpc.io/grpc/core/group__grpc__arg__keys.html
        :param kwargs:
        :return: {'target': 'ip:port', 'options':[]}
        """
        if not target:
            raise ValueError("param target {t} is null".format(t=str(target)))
        elif re.match('^.+:\d+$', target):
            pass
        else:
            raise ValueError("param target error:{t}".format(t=str(target)))

        if options is None:
            options = [('grpc.lb_policy_name', 'pick_first'),
                       ('grpc.enable_retries', 1),
                       ('grpc.keepalive_timeout_ms', 10000)]
        elif isinstance(options, (list, tuple)):
            pass
        else:
            raise ValueError("param options error:{o}".format(o=str(options)))

        return dict(target=target, options=options)

    def get_stub(self, stub_class, **kwargs):
        """
        get stub
        :param stub_class: the name of class Stub
        :param kwargs:
        :return: stub object
        """
        try:
            return stub_class(self._channel)
            # if self._pb2_grpc:
            #     if hasattr(self._pb2_grpc, stub_class):
            #         return getattr(self._pb2_grpc, stub_class)(self.channel)
            #     else:
            #         raise NotImplementedError("{0} has not {1}".format(self._pb2_grpc, stub_class))
            # else:
            #     raise NotImplementedError("_pb2_grpc {0} is null".format(str(self._pb2_grpc)))
        except:
            logger.error("get_grpc_stub error: {e}".format(e=traceback.format_exc()))
            raise

    # def get_request(self, request_class, **kwargs):
    #     """
    #     get requst
    #     :param request_class: the name of class Request
    #     :param kwargs: params needed by class Request
    #     :return: request
    #     """
    #     try:
    #         return request_class(**kwargs)
    #         # if self._pb2:
    #         #     if hasattr(self._pb2, request_class):
    #         #         return getattr(self._pb2, request_class)(**kwargs)
    #         #     else:
    #         #         raise NotImplementedError("{0} has not {1}".format(self._pb2, request_class))
    #         # else:
    #         #     raise NotImplementedError("_pb2 {0} is null".format(str(self._pb2)))
    #     except:
    #         logger.error("get_request error: {e}".format(e=traceback.format_exc()))
    #         raise

    # def exec_func(self, stub, func, request, timeout=10):
    #     """
    #     excute remote function
    #     :param stub: stub object
    #     :param func: the name of class rpc
    #     :param request: request parameter required by class rpc
    #     :param timeout: timeout parameter required by class rpc
    #     :return:
    #     """
    #     try:
    #         if hasattr(stub, func):
    #             _func = getattr(stub, func)
    #             response = _func(request=request, timeout=timeout)
    #             return response
    #         else:
    #             raise NotImplementedError("{0} has not {1}".format(stub, func))
    #     except:
    #         logger.error("exec_func error: {e}".format(e=traceback.format_exc()))
    #         raise

    def response_to_dict(self, data):
        """
        convert message to dict
        :param data:
        :return:
        """
        return [MessageToDict(i) for i in data if i]

    def response_to_json(self, data):
        """
        convert message to json
        :param data:
        :return:
        """
        return [MessageToJson(i) for i in data if i]

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self._channel is not None:
            self._channel.close()
        return False


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    #
    # For more channel options, please see https://grpc.io/grpc/core/group__grpc__arg__keys.html
    with grpc.insecure_channel(target='localhost:50051',
                               options=[('grpc.lb_policy_name', 'pick_first'),
                                        ('grpc.enable_retries', 1),
                                        ('grpc.keepalive_timeout_ms', 30000)
                                        ]) as channel:
        stub = mysql_grpc_pb2_grpc.MySQLGRPCStub(channel)
        # Timeout in seconds.
        # Please refer gRPC Python documents for more detail. https://grpc.io/grpc/python/grpc.html
        request = {
            'dbconn': {
                'ip': '127.0.0.1',
                'port': '3306'
            },
            'user': 'ippool'
        }

        # print("mysql_rpc_pb2.UsersRequest(**request): ",mysql_rpc_pb2.UsersRequest(**request), type(mysql_rpc_pb2.UsersRequest(**request)))
        users_response = stub.GetUsers(mysql_grpc_pb2.UsersRequest(**request), timeout=10)
        # mysql_response = stub.GetMySQL(mysql_rpc_pb2.MySQLRequest(**request), timeout=10)
        # database_response = stub.GetDatabase(mysql_rpc_pb2.DatabaseRequest(**request), timeout=10)

    print("###" * 30)
    print("response.dbconn: ", users_response.dbconn)
    print("response.result: ", users_response.result)
    print("###" * 30)
    for i in users_response.result:
        print("i: ", i)
        print("dict: ", MessageToDict(i))
        # print(i.user)


if __name__ == '__main__':
    # logging.basicConfig()
    # run()
    with CallMySQLGRPC(target='localhost:50051',
                       options=[('grpc.lb_policy_name', 'pick_first'),
                                ('grpc.enable_retries', 1),
                                ('grpc.keepalive_timeout_ms', 30000)
                                ]) as call_mysql:

        _stub = call_mysql.get_stub(stub_class=mysql_grpc_pb2_grpc.MySQLGRPCStub)
        try:
            users_response = get_UsersResponse(stub=_stub, timeout=10,
                                               dbconn={'ip': '127.0.0.1', 'port': '3306',
                                                       'mysqluid': '12345556666'},
                                               user='ippool'
                                               )
            print("users_response: ", users_response)
            print("***" * 30)
            print("users_response.dbconn: ", users_response.dbconn)
            print("***" * 30)
            print("users_response.result: ", users_response.result)
        except Exception as e:
            logger.error("get_UsersResponse error:{e}".format(e=traceback.format_exc()))
            print(traceback.format_exc())
            print("***" * 30)
            print(e.code())
            print(e.details())
            print(e.debug_error_string())

        print("###" * 30)
        try:
            mysql_response = get_MySQLResponse(stub=_stub, timeout=10,
                                               dbconn={'ip': '127.0.0.1', 'port': '3306',
                                                       'mysqluid': '12345556666'},
                                               )
            print("mysql_response: ", mysql_response)
            print("***" * 30)
            print("mysql_response.dbconn: ", mysql_response.dbconn)
            print("***" * 30)
            print("mysql_response.result: ", mysql_response.result)
        except Exception as e:
            logger.error("get_MySQLResponse error:{e}".format(e=traceback.format_exc()))
            print(traceback.format_exc())
            print("***" * 30)
            print(e.code())
            print(e.details())
            print(e.debug_error_string())

        print("###" * 30)
        try:
            database_response = get_DatabaseResponse(stub=_stub, timeout=10,
                                                     dbconn={'ip': '127.0.0.1', 'port': '3306',
                                                             'mysqluid': '12345556666'},
                                                     database='hc_cmdb'
                                                     )
            print("database_response: ", database_response)
            print("***" * 30)
            print("database_response.dbconn: ", database_response.dbconn)
            print("***" * 30)
            print("database_response.result: ", database_response.result)
        except Exception as e:
            logger.error("get_DatabaseResponse error:{e}".format(e=traceback.format_exc()))
            print(traceback.format_exc())
            print("***" * 30)
            print(e.code())
            print(e.details())
            print(e.debug_error_string())
