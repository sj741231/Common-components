# -*-coding=utf8-*-
import os, sys, re

from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

from utils.utils_tools import _do_post, _do_get, DoGetError, DoPostError
from ..env.settings import APPKEY, SSOServerDomain, SSOauthURL, SSOClientDomain, SSO_API_URL

import traceback

import logging

logger = logging.getLogger('django.ops')


def re_mail(mail):
    if isinstance(mail, (str,)):
        re_mail = re.compile('[\w]+[\w.]*@credithc.com$', flags=re.I)  # 邮件正则
        return re_mail.match(mail)
    elif isinstance(mail, (bytes,)):
        mail = str(mail, encoding='utf-8')
        re_mail = re.compile('[\w]+[\w.]*@credithc.com$', flags=re.I)  # 邮件正则
        return re_mail.match(mail)
    else:
        return


def re_mobile(mobile):
    if isinstance(mobile, (str,)):
        re_mobile = re.compile('^[1][3,4,5,7,8][0-9]{9}$')  # 手机号正则
        return re_mobile.match(mobile)
    elif isinstance(mobile, (bytes,)):
        mobile = str(mobile, encoding='utf-8')
        re_mobile = re.compile('^[1][3,4,5,7,8][0-9]{9}$')  # 手机号正则
        return re_mobile.match(mobile)
    else:
        return


UserModel = get_user_model()

"""  
    本地密码+动态口令联合验证  
    定义验证类HCSSOAuth，添加到settings配置中AUTHENTICATION_BACKENDS       
"""
class DynamicPassword_Auth(ModelBackend):

    def get_dynamic_conf(self):
        """ get settings VALIDATE_SECRET configuration"""
        try:
            if bool(SSO_API_URL.get('VALIDATE_SECRET').get('enable')) is True:
                return SSO_API_URL.get('VALIDATE_SECRET')
        except  Exception as e:
            logger.warning("invalid VALIDATE_SECRET configuration")
            return

    def verify_dynamic_password(self, request, username, dynamic_password, validate_secret, **kwargs):
        """ verify dynamic password, return True or raise  """
        try:
            if str(dynamic_password).isdigit() is False:
                raise ValueError("dynamic password invalid:{d}".format(d=str(dynamic_password)))
            if re_mail(username) is None:
                username = validate_secret.get('default_account')

            _data = {'usermail': username,
                     'appkey': APPKEY,
                     'secret': dynamic_password}

            _url = validate_secret.get('url')
            result = _do_post(_url, **_data)

            if result.get('code') in [200, '200']:
                return True
            else:
                raise Exception("dynamic password error, code: {code}, errmsg: {errmsg}".format(**result))
        except (ValueError, DoPostError):
            raise
        except Exception as e:
            logger.error("verify_dynamic_password error: {e}".format(e=traceback.format_exc()))
            raise

    def authenticate(self, request, username=None, password=None, **kwargs):
        """ inherit for verify dynamic password
            password + dynamic password no less than 14
            dynamic password is 6 bit digit
        """
        _validate_secret = self.get_dynamic_conf()
        if _validate_secret is None:
            return super(DynamicPassword_Auth, self).authenticate(request, username=username, password=password,
                                                                  **kwargs)
        else:
            if not isinstance(password, str) or len(str(password).strip()) < 14:
                return None
            else:
                try:
                    _password = str(password).strip()[0:-6]
                    _dynamic_password = str(password).strip()[-6:]
                    if self.verify_dynamic_password(request, username=str(username).strip(),
                                                    dynamic_password=_dynamic_password,
                                                    validate_secret=_validate_secret, **kwargs):
                        return super(DynamicPassword_Auth, self).authenticate(request, username=username,
                                                                              password=_password,
                                                                              **kwargs)
                except:
                    logger.error("authenticate error: {e}".format(e=traceback.format_exc()))
                    return

    # def authenticated() 的源代码
    # if username is None:
    #     username = kwargs.get(UserModel.USERNAME_FIELD)
    # try:
    #     user = UserModel._default_manager.get_by_natural_key(username)
    # except UserModel.DoesNotExist:
    #     # Run the default password hasher once to reduce the timing
    #     # difference between an existing and a non-existing user (#20760).
    #     UserModel().set_password(password)
    # else:
    #     if user.check_password(password) and self.user_can_authenticate(user):
    #         return user
