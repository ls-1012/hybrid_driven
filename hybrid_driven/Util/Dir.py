#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# File:         Dir.py
# Author:       ls
# Date:         2020/10/20 14:38
#-------------------------------------------------------------------------------
import os
from Util.DateAndTime import *
from Conf.ProjVar import *


# 创建目录
def make_dir(dir_path):
    if not os.path.exists(dir_path):
        try:
            os.makedirs(dir_path)
            print("目录'%s'创建成功"% dir_path)
        except:
            print("目录'%s'创建失败"% dir_path)
    else:
        print("目录'%s'已存在" % dir_path)

# 创建时间目录
def make_time_dir():
    date=TimeUtil().get_chinesedate()
    dir_path=os.path.join(proj_path,"ScreenPics")
    dir_path=os.path.join(dir_path,date)
    dir_path=os.path.join(dir_path,str(TimeUtil().get_hour()))
    # print(dir_path)
    make_dir(dir_path)
    return dir_path

if __name__=="__main__":
    make_time_dir()