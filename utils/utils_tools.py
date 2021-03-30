# -*- coding: utf-8 -*-
__author__ = 'shijin'

import sys
import inspect
from django.contrib.auth.models import User, Group
from django.db.models import Q
import re
import socket
import json
from urllib import request, error

import logging
logger = logging.getLogger('django.ops')

class DoPostError(Exception): pass
class DoGetError(Exception): pass


def get_current_function_name():
    # print(sys._getframe().f_code.co_name) #返回 get_current_function_name 函数名
    # print(inspect.stack()[0][3])  #返回 自身的函数信息
    return inspect.stack()[1][3]  # 返回 调用的上一级方法或函数信息


def get_class_name(class_obj):  # 返回传入的对象实例 的类型名称
    if isinstance(class_obj, (object,)):
        return class_obj.__class__.__name__


def isdigit(number):
    try:
        number = int(number)
        return isinstance(number, int)
    except Exception:
        return False


def search_username(fullname):
    """ search User for first_name and last_name user"""
    _fullname = ''.join(str(fullname).split())
    users = User.objects.all()
    try:
        user_qs = users.filter(username=_fullname)
        if user_qs: return user_qs

        if len(_fullname) == 2:
            user_qs = users.filter(last_name=_fullname[0], first_name=_fullname[1])
            if user_qs:
                return user_qs
            else:
                return None
        elif len(_fullname) > 2:
            q = Q(last_name=_fullname[0:1], first_name=_fullname[1:]) | Q(last_name=_fullname[0:2],
                                                                          first_name=_fullname[2:])
            user_qs = users.filter(q)
            if user_qs:
                return user_qs
            else:
                return None
    except  Exception as e:
        logger.error("{f} search {n} error: {e}".format(f="search_username", n=str(fullname), e=repr(e)))
        print(repr(e))
        return None


def get_port(ports, return_type='str'):
    """ check ports and return str or list"""
    port_list = list()
    try:
        if ports and isinstance(ports, str):
            # port_list = ports.split(',')
            port_list = re.split(',|，|、', ports)
        elif ports and isinstance(ports, list):
            pass
        else:
            raise ValueError("变量端口数据类型不合法！")

        if port_list:
            port_list = list(set(list(filter(None, port_list))))
            _port_list = list(filter(isdigit, port_list))
            if len(port_list) == len(_port_list):
                if return_type == 'str':
                    return ','.join(_port_list)
                else:
                    return _port_list
            else:
                raise ValueError("变量端口中包含非法字符！")
        else:
            raise ValueError("变量端口为空值！")
    except ValueError:
        raise
    except Exception:
        raise Exception("get ports errors!")


def get_hostname():
    """ :return hostname """
    try:
        return socket.gethostname()
    except:
        return None


def get_host_ip(connect_ip, connect_port):
    """ :param connect_ip connect remote host ip
               connect_port connect remote host port
        :return ip or None
    """
    s = None
    ip = None
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect((connect_ip, connect_port))
        ip = s.getsockname()[0]
    finally:
        if s is not None:
            s.close()
        return ip


def _do_post(url, **kwargs):
    """
        request post method
    """

    kwargs = kwargs if kwargs else {}
    data = bytes(json.dumps(kwargs), encoding='utf-8')
    req = request.Request(url=url, data=data, method="POST")

    for i in range(3):
        _timeout = 3 * i + 3
        try:
            res = request.urlopen(req, timeout=_timeout)
            if res:
                # print('##'*30)
                # print('res:', res)
                # print('**' * 30)
                # print('res.read(): ', str(res.read(), encoding='utf-8'))
                # print('##' * 30)
                return json.loads(str(res.read(), encoding='utf-8'))
            else:
                continue
        except error.HTTPError as e:
            logger.error("post request failed, url: {u}, code: {c}!".format(u=url, c=e.code))
            continue
        except error.URLError as e:
            logger.error("post request failed, url: {u}, code: {c}!".format(u=url, c=e.reason))
            continue
        except Exception as e:
            logger.error("post request failed, url: {u}, {e} !".format(u=url, e=repr(e)))
            continue
    else:
        raise DoPostError('_do_post error,request failed !')


def _do_get(url, **kwargs):
    """
        request get method
    """

    value = None
    if kwargs:
        value_list = ['{0}={1}'.format(k, v) for k, v in kwargs.items()]
        value = '&'.join(value_list)

    url = url + value if value else url
    req = request.Request(url=url)

    for i in range(3):
        _timeout = 3 * i + 3
        try:
            res = request.urlopen(req, timeout=_timeout)
            if res:
                return json.loads(str(res.read(), encoding='utf-8'))
            else:
                continue
        except error.HTTPError as e:
            logger.error("get request failed {0}, {1}!".format(url, e.code))
            continue
        except error.URLError as e:
            logger.error("get request failed {0}, {1}!".format(url, e.reason))
            continue
        except Exception as e:
            logger.error("get request failed {0}, {1} !".format(url, repr(e)))
            continue
    else:
        raise DoGetError('_do_get error,request failed !')
