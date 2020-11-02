#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# File:         DirAndTime.py
# Author:       ls
# Date:         2020/10/20 14:43
#-------------------------------------------------------------------------------
import locale
import time
import datetime


class TimeUtil:
    def __init__(self,curtime=None):
        self.curtime=curtime

    def get_timestamp(self):
        return time.time()

    def get_date(self):
        return time.strftime("%Y-%m-%d")

    def get_time(self):
        return time.strftime("%H:%M:%S")

    def get_datetime(self):
        return time.strftime("%Y-%m-%d %H:%M:%S")

    def get_chinesedate(self):
        locale.setlocale(locale.LC_CTYPE,"chinese")
        strDate=time.strftime("%Y年%m月%d日",time.localtime())
        return strDate

    def get_chinesetime(self):
        locale.setlocale(locale.LC_CTYPE,"chinese")
        strTime=time.strftime("%H时%M分%S秒",time.localtime())
        return strTime

    def get_chinesedatetime(self):
        locale.setlocale(locale.LC_CTYPE, "chinese")
        strdateTime = time.strftime("%Y年%m月%d日 %H时%M分%S秒", time.localtime())
        return strdateTime

    def compute(self,day_interval):
        today=datetime.date.today()
        if isinstance(day_interval,int) and day_interval>=0:
            return today+datetime.timedelta(days=day_interval)
        if isinstance(day_interval,int) and day_interval<0:
            return today-datetime.timedelta(days=abs(day_interval))

    def timestamp_to_date(self,timestamp):
        if not isinstance(timestamp,float):
            return
        locale.setlocale(locale.LC_CTYPE, "chinese")
        time_tuple=time.localtime(timestamp)
        return str(time_tuple[0])+"年"+str(time_tuple[1])+"月"+str(time_tuple[2])+"日"

    def  timestamp_to_time(self,timestamp):
        if not isinstance(timestamp,float):
            return
        locale.setlocale(locale.LC_CTYPE, "chinese")
        time_tuple=time.localtime(timestamp)
        return str(time_tuple[3])+"时"+str(time_tuple[4])+"分"+str(time_tuple[5])+"秒"

    def timestamp_to_datetime(self,timestamp):
        return self.timestamp_to_date(timestamp)+self.timestamp_to_time(timestamp)

    def get_hour(self):
        return int(time.strftime("%H"))










