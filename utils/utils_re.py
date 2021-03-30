# -*- coding: utf-8 -*-
__author__ = 'shijin'

from io import StringIO
from datetime import datetime
import os
import re




def re_mail(mail):
    if  isinstance(mail, (str,)):
        re_mail = re.compile('[\w]+[\w.]*@credithc.com$',flags=re.I)    #邮件正则
        return  re_mail.match(mail)
    
    elif isinstance(mail, (bytes,)):
        mail = str(mail, encoding='utf-8')
        return  re_mail.match(mail)
        
    else:
        return
    
        

def re_mobile(mobile):
    if  isinstance(mobile, (str,)):
        re_mobile = re.compile('^[1][3,4,5,7,8][0-9]{9}$')              #手机号正则
        return  re_mobile.match(mobile)
    
    elif isinstance(mobile, (bytes,)):
        mobile = str(mobile, encoding='utf-8')    
        return  re_mobile.match(mobile)
    
    else:
        return
    

def re_uid(uidstr):
    if  isinstance(uidstr, (str,)):
        re_uid = re.compile('[\w.]*uid$',flags=re.I)              #UID正则
        return  re_uid.match(uidstr)
    


def isdigit(number):
    try:
        number = int(number)      
        return isinstance(number, int)
    
    except Exception:
        return False


def is_domain(domain):
    try:
        domain_regex = re.compile( \
            r'(?:[A-Z0-9_](?:[A-Z0-9-_]{0,247}[A-Z0-9])?\.)+(?:[A-Z]{2,6}|[A-Z0-9-]{2,}(?<!-))\Z', \
            re.IGNORECASE)
        return True if domain_regex.match(domain) else False

    except Exception:
        return False


def is_url(url):
    try:
        url_regex = re.compile( r'^http[s]?://', re.IGNORECASE )
        return True if url_regex.match(url) else False

    except Exception as e:
        return False


def is_ipv4(address):
    try:
        ipv4_regex = re.compile( \
            r'(?:25[0-5]|2[0-4]\d|[0-1]?\d?\d)(?:\.(?:25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}$',   \
            re.IGNORECASE)
        return True if ipv4_regex.match(address) else False

    except Exception:
        return False



  