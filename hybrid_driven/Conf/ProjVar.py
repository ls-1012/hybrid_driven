#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# File:         ProjVar.py
# Author:       ls
# Date:         2020/10/20 14:42
#-------------------------------------------------------------------------------
import os
# 工程根目录
proj_path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ini配置文件路径
PageElementLocator_file_path=os.path.join(proj_path,"Conf","PageElementLocator.ini")

# 日志配置文件路径
LogConf_file_path=os.path.join(proj_path,"Conf","log.conf")


# 邮箱登录信息
contacts_file_path=os.path.join(proj_path,"TestData","qq邮箱联系人.xlsx")

#

login_info_sheet="qq账号"
contacts_info_sheet="联系人"
test_case_step="测试步骤"

# login_info_sheet.id=0
login_info_sheet_test_description=1
login_info_sheet_step_sheet=2
login_info_sheet_data_sheet=3
login_info_sheet_is_run=4
login_info_sheet_excute_result=5
login_info_sheet_excute_time=6


test_case_step_name_step_description=1
test_case_step_keywords=2
test_case_step_locator_exp=3
test_case_step_opete_value=4
test_case_step_is_run=5
test_case_step_assert_content=6
test_case_step_excute_result=7
test_case_step_excute_time=8

test_case_data_id=0
test_case_data_is_run=10
test_case_data_assert_value=11
test_case_data_excute_result=12
test_case_data_excute_time=13
