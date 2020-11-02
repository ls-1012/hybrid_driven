#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# File:         ParseConfig.py
# Author:       ls
# Date:         2020/10/20 15:42
#-------------------------------------------------------------------------------
import configparser


# 以list形式获取section名称
def read_ini_file_all_sections(ini_file_path):
    cf=configparser.ConfigParser()
    cf.read(ini_file_path,encoding='utf-8-sig')
    return cf.sections()

# 以list形式获取指定section部分的key
def read_ini_file_section_all_options(ini_file_path,section_name):
    cf=configparser.ConfigParser()
    cf.read(ini_file_path,encoding='utf-8-sig')
    return cf.options(section_name)

# 返回key对应的值
def read_ini_file_option(ini_file_path,section_name,option_name):
    cf = configparser.ConfigParser()
    cf.read(ini_file_path, encoding='utf-8-sig')
    try:
        value=cf.get(section_name,option_name)

    except:
        print("the specific section or option doesn't exit! ")
        return None
    else:
        # 返回配置文件中=右边的数据（定位表达式和定位方法）
        return value


if __name__=='__main__':
    init_file=r"C:\Users\LS\PycharmProjects\data_driven\Conf\PageElementLocator.ini"
    print(read_ini_file_all_sections(init_file))
    print(read_ini_file_section_all_options(init_file,'bbbbbbb1'))
    print(read_ini_file_option(init_file,'bbbbbbb1','s1'))