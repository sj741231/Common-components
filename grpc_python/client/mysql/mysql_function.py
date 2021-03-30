"""gRPC Python helloworld.Greeter client with channel options and call timeout parameters."""

from __future__ import print_function
import logging
import re
import grpc
import traceback
import copy

import mysql_grpc_pb2
import mysql_grpc_pb2_grpc

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


def get_UsersRequest(**kwargs):
    request = mysql_grpc_pb2.UsersRequest(**kwargs)
    return request


def get_MySQLRequest(**kwargs):
    request = mysql_grpc_pb2.MySQLRequest(**kwargs)
    return request


def get_DatabaseRequest(**kwargs):
    request = mysql_grpc_pb2.DatabaseRequest(**kwargs)
    return request


def get_UsersResponse(stub, **kwargs):
    params = copy.deepcopy(kwargs)
    for i in kwargs.keys():
        if i not in ['dbconn', 'user']:
            params.pop(i)
    request = get_UsersRequest(**params)
    return stub.GetUsers(request, timeout=kwargs.get('timeout', 10))


def get_MySQLResponse(stub, **kwargs):
    params = copy.deepcopy(kwargs)
    for i in kwargs.keys():
        if i not in ['dbconn', 'database']:
            params.pop(i)
    request = get_MySQLRequest(**params)
    return stub.GetMySQL(request, timeout=kwargs.get('timeout', 10))


def get_DatabaseResponse(stub, **kwargs):
    params = copy.deepcopy(kwargs)
    for i in kwargs.keys():
        if i not in ['dbconn', 'database']:
            params.pop(i)
    request = get_DatabaseRequest(**params)
    return stub.GetDatabase(request, timeout=kwargs.get('timeout', 10))


if __name__ == '__main__':
    # logging.basicConfig()
    # run()
    pass
