#-*- encoding:utf-8 -*-
import os
import sys   #reload()之前必须要引入模块
# reload(sys)
# sys.setdefaultencoding('utf-8')

path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(path)

import datetime
import time

class Factory_date(object):
    """
    定义工厂类，返回不同的日期格式实例
    定义后，可直接修改dateformat，修改返回日期实例类型    
    """
    def __init__(self, dateformat=None):
        """
        获得日期实例
        datetype:返回日期类型，obj,str,stamp
        输入datetype类型不存在，抛异常
        """
        self.dateformat = dateformat
        self.datetype = dict(obj=Date_obj,str=Date_str,stamp=Date_stamp)  
        
    @property           
    def get_dateinstance(self):

        try:
            return  self.datetype[self.dateformat]()
        
        except KeyError as e:
            errors = str('日期格式输入错误：')+ str(e)
            raise   errors
        
        

class Date_obj(object):
    """
    get define date
    kwargs: days= ,seconds=, microseconds=
    days、seconds、microseconds +： plus datetime
    days、seconds、microseconds -： subtract datetime
    """
    def __init__(self):
        self.now = datetime.datetime.now()
        
    def _get_datetime(self):
        return self.now
    
    def _get_interval(self, days=0, seconds=0, microseconds=0):
        
        interval = dict(days=days,seconds=seconds,microseconds=microseconds)
        
        delta = datetime.timedelta(**interval)
        
        return self.now+delta
    
   
class Date_str(object):
    """
    get define date
    kwargs: days= ,seconds=, microseconds=
    days、seconds、microseconds +： plus datetime
    days、seconds、microseconds -： subtract datetime
    """
    def __init__(self):
        self.now = datetime.datetime.now()
        
    def _get_datetime(self):
        return self.now.strftime('%Y-%m-%d %H:%M:%S')
    
    def _get_interval(self, days=0, seconds=0, microseconds=0):
    
        interval = dict(days=days,seconds=seconds,microseconds=microseconds)       
        delta = datetime.timedelta(**interval)        
        newdate = self.now+delta
        
        return newdate.strftime("%Y-%m-%d %H:%M:%S")
    
    
class Date_stamp(object):
    """
    get define date
    kwargs: days= ,seconds=, microseconds=
    days、seconds、microseconds +： plus datetime
    days、seconds、microseconds -： subtract datetime
    """
    def __init__(self):
        self.now = datetime.datetime.now()
        
    def _get_datetime(self):
        return int(time.mktime(self.now.timetuple()))
    
    def _get_interval(self, days=0, seconds=0, microseconds=0): 
  
        interval = dict(days=days,seconds=seconds,microseconds=microseconds)        
        delta = datetime.timedelta(**interval)
        newdate = self.now+delta
        datestamp = int(time.mktime(newdate.timetuple()))
        return datestamp
    
if __name__ == "__main__":
    fdate = Factory_date('stamp')
    dateinstance = fdate.get_dateinstance
    print("stamp 当前时间： ",dateinstance._get_datetime())
    
    fdate.dateformat = 'obj'
    dateinstance1 = fdate.get_dateinstance
    print("obj 当前时间： ",dateinstance1._get_datetime())
    print("obj 当前时间+30天： ",dateinstance1._get_interval(days=30))
    
    time.sleep(10)
    
    fdate.dateformat = 'str'
    dateinstance2 = fdate.get_dateinstance
    print("str 当前时间： ",dateinstance2._get_datetime())
    print("str 当前时间+3天： ",dateinstance2._get_interval(days=3))
    print("str 当前时间-3天-1小时： ",dateinstance2._get_interval(days=-3, seconds =-3600))
    
    

    