#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# File:         Log.py
# Author:       ls
# Date:         2020/10/14 16:07
#-------------------------------------------------------------------------------
import logging.config
import logging
from Conf.ProjVar import *
from Util.DateAndTime import *

# 没有想到更好的使用方法
# # 日志文件存放路径
# LogDir_file_path=os.path.join(proj_path,"Log")
# log_filename="log"+TimeUtil().get_datetime()
# log_file=os.path.join(LogDir_file_path,log_filename)
class MyLog():
    def __init__(self):
        self.logger=None

    def get_logger(self):
        logging.config.fileConfig(LogConf_file_path)
        self.logger=logging.getLogger("example01")
        return self.logger


    # 日志文件配置：多个logger，每个logger指定不同的handler
    # handler：设置了日志输出行的格式
    # handler：以及设定写日志到文件（是否回滚）还是到屏幕
    # handler：还设定了打印日志的级别

    def debug(self,message):
        self.logger.debug(message)


    def warning(self,message):
        self.logger.warning(message)

    def info(self,message):
        self.logger.info(message)

    def error(self,message):
        self.logger.error(message)

    def critical(self,message):
        self.logger.debug(message)


if __name__=="__main__":
    my_log = MyLog()
    log = my_log.get_logger()
    log.debug("debug info....不会打印出来")
    log.info("写入文件中的数据。。。。。")
    log.warning("输出在控制台和文件中的信息的日志信息")
    log.error("同warning.....")
