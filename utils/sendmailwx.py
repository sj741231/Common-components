#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import json
from urllib import request
from urllib.parse import urljoin,quote
from hashlib import md5


SERVER = (
    ( "http://10.10.255.196/api/",      "xxxxxxxxxxxxxxxxxxxxxxxxx" ), # 生产环境
    ( "http://10.150.26.29:8000/api/", "xxxxxxxxxxxxxxxxxxxxxxxxx")   # 测试环境
)

def get_file_md5(f):
    if not os.path.isfile(f):
        return
    myhash = md5()
    f = open(f,'rb')
    while True:
        b = f.read(1024*10240)
        if not b:
            break
        myhash.update(b)
    f.close()
    # return b64encode(myhash.hexdigest())
    return myhash.hexdigest()

def get_file_content(f,method='rb'):
    fp = open(f,method)
    s = fp.read()
    fp.close()
    return s

def get_file_size(f):
    return os.stat(f).st_size

class Client:
    uri = None

    def __init__(self,key):
        self.key = key

    def read_response(self,response):
        try:
            data = str(response.read(), encoding='utf-8')
        except UnicodeDecodeError:
            data = str(response.read(), encoding="utf-8", errors="ignore")
        try:
            return json.loads(data)
        except Exception:
            print(data)
            return json.loads(data)

    def _do_get(self,url):
        for i in range(3):
            req = request.Request(url=url,method='GET')
            try:
                res = request.urlopen(req)
                if res:
                    return self.read_response(res)
                else:
                    continue
            except Exception as e:
                print(e)
                continue
        else:raise Exception('request failed')

    def _do_post(self,url,**kwargs):
        data = bytes(json.dumps(kwargs),encoding='utf-8')
        req = request.Request(url=url,data=data,method='POST')
        for i in range(3):
            try:
                res = request.urlopen(req)
                if res:
                    return self.read_response(res)
                else:
                    continue
            except Exception as e:
                print(e)
                continue
        else:
            raise Exception('request failed')

    def _urljoin(self,shorUrl):
        return urljoin(self.uri,shorUrl)

    def _fix_args(self,**kwargs):
        return '&'.join(['{i}={j}'.format(i=str(i),j=str(j)) for i,j in kwargs.items()])

    def _make_full_url(self,shortUrl,**kwargs):
        if bool(kwargs): return self._urljoin(shortUrl) + '?' + self._fix_args(**kwargs)
        else: return self._urljoin(shortUrl)

    def _make_upload_media_header(self,_path,cid=None):
        headers = {
            # 'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6',
            'Content-MD5': get_file_md5(_path),
            'Content-Type': 'text/plain',
            'Content-Length': get_file_size(_path),
            'Content-Disposition': quote(os.path.basename(_path)),
        }
        if cid is not None:
            headers['Content-ID'] = cid
        return headers

    def upload_media(self,media_path):
        headers = self._make_upload_media_header(media_path)
        headers['key'] = self.key
        url = self._make_full_url('/v2/media/upload')
        return self._do_post(url)

    def _make_argvs(self,to,subject,body,mimetype='plain',cc=None):
        result = {
            'key': self.key,
            'to': to,
            'subject': subject,
            'body': body,
            'mimetype':mimetype
        }
        if cc is not None:
            if isinstance(cc,str):result["cc"] = [cc,]
            elif isinstance(cc,list):result["cc"] = cc
            else:raise ValueError('cc type error:{c}'.format(c=repr(cc)))
        return result

    def send_emailv2(self,to,subject,body,mimetype='plain',cc=None):
        url = self._make_full_url('v2/email')
        argvs = self._make_argvs(to,subject,body,mimetype,cc)
        return self._do_post(url,**argvs)

    def send_emailv1(self,to,subject,body,mimetype='plain',cc=None):
        url = self._make_full_url('v1/email')
        argvs = self._make_argvs(to,subject,body,mimetype,cc)
        return self._do_post(url,**argvs)

    def send_qywx(self,to,body):
        assert any([isinstance(to,str),isinstance(to,list)]) is True
        url = self._make_full_url("v2/qywxsend/text")
        return self._do_post(url,**{
            "key"  : self.key,
            "body" : body,
            "to"   : to
        })


    def send_qywx_v1(self,to,body):
        assert any([isinstance(to, str), isinstance(to, list)]) is True
        url = self._make_full_url("v1/qywxsend")
        return self._do_post(url, **{
            "key" : self.key,
            "body": body,
            "to"  : to
        })

    def send_attach_mail(self,to, subject, body, header, mimetype='plain', *cc):
        url =self._make_full_url('v2/email')
        pass

class ClientProductionEnv(Client):
    uri = SERVER[0][0]

    def __init__(self,key=SERVER[0][1]):
        super(ClientProductionEnv,self).__init__(key)

class ClientTestEnv(Client):
    uri = SERVER[1][0]

    def __init__(self,key=SERVER[1][1]):
        super(ClientTestEnv,self).__init__(key)

if __name__ == "__main__":
    message = """
从安全和负载等多方面考虑，我们对所有接口调用做了一些策略；目前策略如下：

    1.邮箱接口只对内提供服务，不接受非公司邮箱；即收件人和抄送人邮箱后缀必须是credithc.com。

    2.监控告警类业务：连续调用接口间隔时间小于10秒且累计10次的，该KEY将被冻结10分钟并返回提示信息。

    3.有集中热点时段类业务：在热点时段（申请时需要写明热点时间段）可内可连续调用接口，连续间隔时间大于1秒小于3秒，不累计次数，热点时段外按监控告警类策略处理。

    4.由于腾讯企业微信接口限制；企业微信接口对同一个成员发送消息不可超过30条/分，超过部分会被丢弃不下发。

    """
    test = ClientTestEnv()
    test.send_emailv1(to=["shijin170714@credithc.com",],subject="测试测试测试",body=message,cc=["shijin170714@credithc.com",])
    test.send_emailv2(to=["shijin170714@credithc.com",],subject="测试测试测试",body=message,cc=["shijin170714@credithc.com",])
    test.send_qywx(to=["shijin170714@credithc.com",],body=message)
    test.send_qywx_v1(to=["shijin170714@credithc.com",],body=message)