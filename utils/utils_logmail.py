from __future__ import unicode_literals
__author__ = 'shijin'

import logging
import logging.config  # needed when logging_config doesn't start with logging.config
from copy import copy

import os,sys
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(FILE_DIR)
from sendmailwx import *


""" 
    0、集成了大彬哥的发送邮件接口，直接导入了他的发送测试demo - sendmailwx，记得要修改SERVER配置
            SERVER = (
                ( "http://10.10.255.196/api/",      "xxxxxxxxxxxxxxxxxxxxxxxxx" ), # 生产环境
                ( "http://10.150.26.29:8000/api/", "xxxxxxxxxxxxxxxxxxxxxxxxx")   # 测试环境
            )
    1、utils_logmail.py 和 sendmailwx.py 放置在同一目录下，如果不是，请修改FILE_DIR
    2、设置Receivers 和 SendmailEnv 两个全局变量,作为默认值
            Receivers = ['shijin170714@credithc.com',]
            # SendmailEnv = ClientProductionEnv  #生产类，sendmailwx中定义的
            SendmailEnv = ClientTestEnv  #测试类，，sendmailwx中定义的
    3、如果有django settings.ADMINS,那么优先使用2中的设置
            ADMINS = [('shijin170714', 'shijin170714@credithc.com' )]
    4、如果上述2、3两者设置参数不全，那么不处理，不会发送任何邮件
    5、使用方式：
                a、logging模块直接使用，参见 if __name__ == "__main__":
                
                b、django中setting配置使用，见下样例
                    #####################################################
                    #管理员邮箱，接受ERROR错误邮件，可设置多个发送对象，每个对象是一个元组
                    ADMINS = [('shijin170714', 'shijin170714@credithc.com' )]
                    
                    # ### log 配置部分BEGIN ### #
                    import sys
                    sys.path.append(BASE_DIR)   #将项目根目录添加到模块路径中，为了识别加载'hccmdb.utils_logmail.SendEmailHandler'
                    
                       #handler设置，样例中只显示了自定义发送邮件接口的配置，其它配置参见官方文档
                       'handlers': {
                                    'custom_mail_handler': {  # 定义邮件handler,先要定义ADMINS和 EMAIL配置
                                        'level': 'ERROR',
                                        'class': 'hccmdb.utils_logmail.SendEmailHandler',   #自定义发送邮件通知模块的模块及类
                                        'filters': ['require_debug_false'],  # 当debug = False的时候生效，参见filter设置。
                                        'formatter': 'standard',   #参见formatter设置
                                        # 'include_html': True,  #不要使用html格式，不能按照formatter格式显示。
                                    },  # 自定义邮件报警模块
                        },
                        
                        #logger设置，样例中只显示了自定义发送邮件接口的配置，其它配置参见官方文档
                        'loggers': {  #定义了django 和django.request
                                    'django': {  
                                        'handlers': ['file_handler', 'console', 'custom_mail_handler'],  # file,console, mail 三个handler
                                        'level': 'DEBUG',
                                        'propagate': False,  #是否继承父类的log信息
                                    }, #handlers 来自于上面的 handlers 定义的内容
                    
                        }
"""

Receivers = ['shijin170714@credithc.com',]
# SendmailEnv = ClientProductionEnv  #生产类
SendmailEnv = ClientTestEnv  #测试类

class SendEmailHandler(logging.Handler):
    """An exception log handler that emails log entries to site admins.

    If the request is passed as the first argument to the log record,
    request data will be provided in the email report.
    """

    def __init__(self, include_html=False, email_backend=None):
        logging.Handler.__init__(self)
        self.include_html = include_html
        self.email_backend = email_backend

    def emit(self, record):
        try:
            request = record.request
            subject = '%s (%s IP): %s' % (
                record.levelname,
                ('internal' if request.META.get('REMOTE_ADDR') in settings.INTERNAL_IPS
                 else 'EXTERNAL'),
                record.getMessage() if len(record.getMessage()) <= 30 else record.getMessage()[0:30]
            )
        except Exception:
            subject = '%s: %s' % (
                record.levelname,
                record.getMessage() if len(record.getMessage()) <= 30 else record.getMessage()[0:30]
            )
            request = None
        subject = self.format_subject(subject)

        # Since we add a nicely formatted traceback on our own, create a copy
        # of the log record without the exception data.
        no_exc_record = copy(record)
        no_exc_record.exc_info = None
        no_exc_record.exc_text = None

        if record.exc_info:
            exc_info = record.exc_info
        else:
            exc_info = (None, record.getMessage(), None)

        if  hasattr(no_exc_record,  'msg'):
            message = "%s\n\n%s" % (self.format(no_exc_record), '')
        else:
            message = "No error message "

        self.send_mail(subject, message)

    def send_mail(self, subject, message, **kwargs):
        """sendmail"""
        _receiver = self.get_mailaddress()
        _sendmailenv = self.__get_sendmailenv

        if  _receiver and _sendmailenv:
            _sendmailenv.send_emailv2( to=_receiver, subject=subject, body=message )

    def get_mailaddress(self):
        """ get mail address"""
        names = globals()
        try:
            admin_mail = ( names.get('ADMINS') or names.get('settings').ADMINS )
            if  admin_mail:
                mails = [ i[1] for i in admin_mail if i[1] ]
                return mails
            else:
                mails = self.__get_receivers if self.__get_receivers else []

            return mails
        except:
            mails = self.__get_receivers if self.__get_receivers else []
            return mails

    @property
    def __get_receivers(self):
        """get configure info of Receivers """
        try:
            if  Receivers and isinstance(Receivers, (list,)):
                return Receivers
        except:
            return

    @property
    def __get_sendmailenv(self):
        """get  Class instance of SendmailEnv """
        try:
            if  SendmailEnv and isinstance(SendmailEnv(), (ClientProductionEnv,ClientTestEnv)):
                return SendmailEnv()
        except:
            return

    def format_subject(self, subject):
        """
        Escape CR and LF characters.
        """
        return subject.replace('\n', '\\n').replace('\r', '\\r')


if __name__ == "__main__":

    message1 = """大彬哥太猥琐，今天又坑我。。。。。。。代码BUG太多，还专怼妹子，望知悉，谢谢！"""
    message2 = """ 大彬哥好样的，今天又成功怼了一个妹子，牛X ！"""

    # 获取logger实例
    logger = logging.getLogger()
    # 创建自定义handler类实例
    mh = SendEmailHandler()
    #定义日志格式
    formatter = logging.Formatter('%(levelname)s %(asctime)s %(module)s %(funcName)s %(lineno)d: %(message)s')
    #绑定日志格式
    mh.setFormatter(formatter)
    #添加自定义handler
    logger.addHandler(mh)
    #设置log等级
    logger.setLevel(logging.ERROR)
    #发送测试
    logger.info(message1)
    logger.error(message2)

