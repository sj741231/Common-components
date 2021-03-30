# -*-coding=utf8-*-

import socket, sys, time
from urllib.parse import urlparse
from utils_re import re_mail, re_mobile, isdigit, is_domain, is_ipv4, is_url

import logging

logging.basicConfig(filename='checkport.log',
                    format='%(asctime)s -%(name)s-%(levelname)s-%(module)s:%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S %p',
                    level=logging.DEBUG)


class CheckAlive(object):
    """
        check whether remote service is alive or not
        1、instance = CheckAlive(invertal, attempt),check paramse and setting property
        2、instance.execute(**kwargs)
           kwargs:  url = IP or domain or url,  required
                    port = probe port,  required
                    proto = TCP or UDP,  selected
                    timeout = socket.timeout, selected
           return: True = alive  or False = unalie
        3、Exceptions need to be caught

    """
    __allowed_protocol = {'TCP': socket.SOCK_STREAM, 'UDP': socket.SOCK_DGRAM}
    __allowed_timeout = {'min': 0.2, 'mid': 0.5, 'max': 2}
    __interval_time = 2
    __attempt_count = 3

    __slots__ = ('__interval', '__attempt')

    def __init__(self, interval=None, attempt=None):
        """
        :param interval: 设置重试等待时间间隔，默认为 interval_time = 2
        :param attempt:  设置最大尝试次数，默认为 attempt_count = 3
        最大等待时间为：interval_time*5 * attempt_count*5 = 150秒
        """
        self.get__allowed_protocol
        self.get__attempt_count
        self.get__allowed_protocol
        self.get__allowed_timeout

        # self.__interval = interval
        # self.__attempt = attempt

        self.interval = interval
        self.attempt = attempt

    @property
    def get__interval_time(self):
        if not self.__interval_time:
            raise Exception('Need to configure __interval_time!')
        if self.__interval_time < 0:
            raise Exception('Need to correct configure __interval_time!')
        return self.__interval_time

    @property
    def get__attempt_count(self):
        if not self.__attempt_count:
            raise Exception('Need to configure __attempt_count!')
        if self.__attempt_count < 1:
            raise Exception('Need to correct configure __attempt_count!')
        return self.__attempt_count

    @property
    def get__allowed_protocol(self):
        if not self.__allowed_protocol:
            raise Exception('Need to configure __allowed_protocol!')
        return self.__allowed_protocol

    @property
    def get__allowed_timeout(self):
        if not self.__allowed_timeout:
            raise Exception('Need to configure __allowed_timeout!')

        try:
            if min(self.__allowed_timeout.get('min'), self.__allowed_timeout.get('mid'),
                   self.__allowed_timeout.get('max')) < 0:
                raise Exception('Need to Correct configure min、mid、max!')
        except:
            raise Exception('Need to Correct configure __allowed_timeout!')

        return self.__allowed_timeout

    @property
    def interval(self):
        return self.__interval

    @property
    def attempt(self):
        return self.__attempt

    @interval.setter
    def interval(self, interval):
        try:
            if not isinstance(interval, (int,)):
                self.__interval = self.__interval_time
            elif interval < 0:
                self.__interval = 0
            elif interval > self.__interval_time * 5:
                self.__interval = self.__interval_time * 5
            else:
                self.__interval = interval
        except:
            self.__interval = self.__interval_time

    @attempt.setter
    def attempt(self, attempt):
        try:
            if not isinstance(attempt, (int,)):
                self.__attempt = self.__attempt_count
            elif attempt < 0:
                self.__attempt = 1
            elif attempt > self.__attempt_count * 5:
                self.__attempt = self.__attempt_count * 5
            else:
                self.__attempt = attempt
        except:
            self.__attempt = self.__attempt_count

    def execute(self, **kwargs):
        """
        :param kwargs: url = 域名，必填
        :param kwargs:  port = 端口，必填
        :param kwargs: proto = TCP或UDP，选填，默认TCP
        :param kwargs: timeout = socket.timeout，选填 默认 allowed_timeout
        :return:
        """
        try:

            params = self.check_params(**kwargs)

            params_ip = self.set_params_ip(**params)

            alive = self.attempts(**params_ip)
            return alive

        except Exception as e:
            message = "execute:{0}".format(str(e))
            print(message)
            raise

    def set_params_ip(self, **params):
        """
        :param params: ip added to params
        :return: new params
        """
        _url = params.get('url')

        try:
            if self.check_ipaddress(_url):
                params['ip'] = _url
                return params

            elif self.check_domain(_url):
                _domain = self.check_domain(_url)
                params['ip'] = self.get_ip(_domain)
                return params

            elif self.check_urlnetloc(_url):
                _domain = self.check_urlnetloc(_url)
                params['ip'] = self.get_ip(_domain)
                return params

            else:
                raise Exception("url is not valid params:{0}".format(str(_url)))

        except Exception as e:
            message = "set_params_ip Failed:{0}".format(str(e))
            print(message)
            raise Exception(message)

    def get_ip(self, host):
        """
        :param host: IP or Domain
        :return: IP
        """
        if self.check_ipaddress(host):
            return self.check_ipaddress(host)

        elif self.check_domain(host):
            for i in range(3):
                try:
                    _ip = self.get_domain_ip(self.check_domain(host))
                    return _ip
                except:
                    _timeout = min(self.__interval, 2)
                    time.sleep(_timeout)
                    continue
            else:
                message = "Domain Name Resolution Failed:{0}".format(str(host))
                print(message)
                raise Exception(message)

        else:
            raise Exception("input params is not IP or Domain:{0}".format(str(host)))

    def attempts(self, **params):
        """
        appempt conncet , test service status
        :param params:
        :return:
        """
        alive = False

        n = 0
        while n < self.__attempt:
            try:
                sock = self.generate_socket(**params)

            except Exception as e:
                message = "generate_socket:{0}".format(str(e))
                print(message)
                raise Exception(message)

            try:
                statuscode = self.check_service(sock, **params)
                if statuscode == 0:
                    sock.close()
                    alive = True
                    break
                else:
                    sock.close()
                    n += 1
                    time.sleep(self.__interval)

            except Exception as e:
                sock.close()
                message = "check_service:{0}".format(str(e))
                print(message)
                raise Exception(message)

        return alive

    def get_domain_ip(self, domain):
        """
        :param domain:  domain
        :return:  ip
        """
        try:
            ip = socket.gethostbyname(domain)
            if ip:
                return ip
            else:
                message = 'invalid domain: {0}'.format(str(domain))
                print(message)
                raise Exception(message)

        except  Exception as e:
            message = 'get domain ip error: {0}'.format(str(e))
            print(message)
            raise

    def check_domain(self, domain):
        """
        :param domain: domain
        :return:  domain or None
        """
        if is_domain(domain):
            return domain
        else:
            return

    def check_urlnetloc(self, url):
        """
        :param url: url
        :return:  url.netloc: domain or ip
        """
        if is_url(url):
            parsed = urlparse(url)
        else:
            url = 'http://' + url
            parsed = urlparse(url)

        if parsed.netloc:
            _netloc_list = parsed.netloc.split(':')
            if _netloc_list:
                return _netloc_list[0]
            else:
                raise Exception("resolve params is invalid url:{0}".format(str(url)))
        else:
            raise Exception("input params is invalid url:{0}".format(str(url)))

    def check_ipaddress(self, ip):
        """
        :param ip:  ip
        :return:   ip or None
        """
        if is_ipv4(ip):
            return ip
        else:
            return

    def check_params(self, **kwargs):
        """
        :param kwargs:  url: IP、Domain、Url,must be selected
                        port: 1-65535,must be selected
                        proto: TCP or UDP,optional
                        timeout: S,optional
        :return: checked params
        """
        _url = kwargs.get('url')
        _port = kwargs.get('port')
        _proto = kwargs.get('proto')
        _timeout = kwargs.get('timeout')

        if _url and isinstance(_url, (str,)):
            kwargs['url'] = _url.strip()
        else:
            message = 'need input invalid url'
            raise Exception(message)

        if isdigit(_port):
            _port = int(_port)

            if _port < 1 or _port > 65535:
                message = 'port invalid: {0}'.format(str(_port))
                raise Exception(message)
            kwargs['port'] = _port

        else:
            message = 'need input port(1 - 65535),error:{0}'.format(str(_port))
            raise Exception(message)

        if isinstance(_proto, (str,)):
            _proto = _proto.strip().upper()
            _type = self.__allowed_protocol.get(_proto) if self.__allowed_protocol.get(_proto) else socket.SOCK_STREAM
            kwargs['type'] = _type

        else:
            kwargs['type'] = socket.SOCK_STREAM

        if isdigit(_timeout):
            _timeout = float(_timeout)
            if _timeout > self.__allowed_timeout.get('max'):
                kwargs['timeout'] = self.__allowed_timeout.get('max')

            elif _timeout < self.__allowed_timeout.get('min'):
                kwargs['timeout'] = self.__allowed_timeout.get('min')

            else:
                kwargs['timeout'] = _timeout

        else:
            kwargs['timeout'] = self.__allowed_timeout.get('mid')

        return kwargs

    def generate_socket(self, **params):
        """
        :param params: generate socket instance
        :return: instance
        """
        _family = socket.AF_INET
        _type = params.get('type')
        _timeout = params.get('timeout')

        sock = socket.socket(_family, _type)
        sock.settimeout(_timeout)

        return sock

    def check_service(self, sock, **params):
        """
        :param sock: socket instance
        :param params:  params
        :return:  statuscode
        """
        _sock = sock

        if not params.get("ip", None):
            if self.check_ipaddress(params.get('url')):
                params['ip'] = self.check_ipaddress(params.get('url'))
            else:
                raise Exception("no parameter ip found")

        if not params.get("port", None):
            raise Exception("no parameter port found")

        _ip_port = (params.get('ip'), params.get('port'))

        try:
            statuscode = _sock.connect_ex(_ip_port)

        except Exception as e:
            message = "check_service error:{0}".format(str(e))
            print(message)
            sock.close()
            raise Exception(message)

        if statuscode == 0:
            print("service is running !")
        else:
            print("service isn't working correctly !")

        return statuscode


if __name__ == '__main__':

    try:
        chkalive = CheckAlive()
    except Exception as e:
        print(str(e))
    print('interval: ', chkalive.interval, 'attempt: ', chkalive.attempt)
    print("=====================================================")

    kwargs = dict()
    kwargs['url'] = '10.100.19.172'
    kwargs['port'] = 80
    kwargs['timeout'] = 5
    params = chkalive.check_params(**kwargs)
    print('params: ', params)
    print("=====attempt 10.100.19.172 ============================================================")
    try:
        result = chkalive.execute(**kwargs)
        print('**{0} {3} service port {1} status is {2}'.format(kwargs.get('url'), kwargs.get('port'), result, \
                                                                kwargs.get('proto') if kwargs.get('proto') else 'TCP'))
    except Exception as e:
        print(str(e))

    print("=====attempt 202.106.0.20:53============================================================")
    kwargs['url'] = '202.106.0.20:53'
    try:
        result = chkalive.execute(**kwargs)
        print('**{0} {3} service port {1} status is {2}'.format(kwargs.get('url'), kwargs.get('port'), result, \
                                                                kwargs.get('proto') if kwargs.get('proto') else 'TCP'))
    except Exception as e:
        print(str(e))

    print("=====attempt www.sina.com.cn============================================================")
    kwargs['url'] = 'www.sina.com.cn'
    try:
        result = chkalive.execute(**kwargs)
        print('**{0} {3} service port {1} status is {2}'.format(kwargs.get('url'), kwargs.get('port'), result, \
                                                                kwargs.get('proto') if kwargs.get('proto') else 'TCP'))
    except Exception as e:
        print(str(e))

    print("=====attempt www.baidu.com:443============================================================")
    kwargs['url'] = 'www.baidu.com:443'
    try:
        result = chkalive.execute(**kwargs)
        print('**{0} {3} service port {1} status is {2}'.format(kwargs.get('url'), kwargs.get('port'), result, \
                                                                kwargs.get('proto') if kwargs.get('proto') else 'TCP'))
    except Exception as e:
        print(str(e))

    print("=====attempt http://www.credithc.com============================================================")
    kwargs['url'] = 'http://www.credithc.com'
    try:
        result = chkalive.execute(**kwargs)
        print('**{0} {3} service port {1} status is {2}'.format(kwargs.get('url'), kwargs.get('port'), result, \
                                                                kwargs.get('proto') if kwargs.get('proto') else 'TCP'))
    except Exception as e:
        print(str(e))

    print("=====attempt http://www.souhu.com/index.html============================================================")
    kwargs['url'] = 'http://www.souhu.com/index.html'
    try:
        result = chkalive.execute(**kwargs)
        print('**{0} {3} service port {1} status is {2}'.format(kwargs.get('url'), kwargs.get('port'), result, \
                                                                kwargs.get('proto') if kwargs.get('proto') else 'TCP'))
    except Exception as e:
        print(str(e))

    print("=====attempt http://www.163.com:80/index.html============================================================")
    kwargs['url'] = 'http://www.163.com:80/index.html'
    try:
        result = chkalive.execute(**kwargs)
        print('**{0} {3} service port {1} status is {2}'.format(kwargs.get('url'), kwargs.get('port'), result, \
                                                                kwargs.get('proto') if kwargs.get('proto') else 'TCP'))
    except Exception as e:
        print(str(e))

    print("")
    print('****' * 30)
    print("======测试修改重试等待时间和重试次数")

    # 定义参数
    kwargs = dict()
    kwargs['url'] = '202.106.0.20'
    kwargs['port'] = 53
    kwargs['timeout'] = 2

    # 1、创建类实例
    try:
        test = CheckAlive()
    except:
        raise

    print('interval: ', test.interval, 'attempt: ', test.attempt)
    print("=====================================================")
    # 2、输入参数执行
    try:
        testresult = test.execute(**kwargs)
        print('**{0} {3} service port {1} status is {2}'.format(kwargs.get('url'), kwargs.get('port'), testresult, \
                                                                kwargs.get('proto') if kwargs.get('proto') else 'TCP'))
    except Exception as e:
        print(str(e))

    print("=====================================================")
    # 3、修改探测间隔时间、重试次数
    test.interval = 1
    test.attempt = 5
    print('interval: ', test.interval, 'attempt: ', test.attempt)
    try:
        testresult = test.execute(**kwargs)
        # print('**{0} {3} service port {1} status is {2}'.format(kwargs.get('url'), kwargs.get('port'), testresult,\
        #                                                     kwargs['proto'] if kwargs['proto'] else 'TCP'))

        print('**{0} {3} service port {1} status is {2}'.format(kwargs.get('url'), kwargs.get('port'), testresult, \
                                                                kwargs.get('proto') if kwargs.get('proto') else 'TCP'))
    except Exception as e:
        print(str(e))

    print("")
    print('****' * 30)
    print("======测试UDP检测==============")

    # 定义参数
    kwargs = dict()
    kwargs['url'] = '202.106.0.20'
    kwargs['port'] = 53
    kwargs['proto'] = 'UDP'
    kwargs['timeout'] = 2

    # 1、创建类实例
    try:
        udptest = CheckAlive(interval=2, attempt=2)
        udpresult = udptest.execute(**kwargs)
        print('**{0} {3} service port {1} status is {2}'.format(kwargs.get('url'), kwargs.get('port'), udpresult, \
                                                                kwargs.get('proto') if kwargs.get('proto') else 'TCP'))
    except:
        raise
