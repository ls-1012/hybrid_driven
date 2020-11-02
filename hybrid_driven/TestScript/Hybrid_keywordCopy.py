#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# File:         KeyWordCore.py
# Author:       ls
# Date:         2020/10/23 13:21
# -------------------------------------------------------------------------------
import re

from selenium.common.exceptions import ElementNotInteractableException

from Util.operator_Excel import *
from Action.Action import *
from Util.Log import *



wb=""
pattern=re.compile(r"\${(.*?)}")
my_log = MyLog()
log = my_log.get_logger()


def get_sheet_content(sheetname):
    global wb
    wb.set_sheet_by_sheetname(sheetname)
    return wb.getExcelContent()

# 获取联系人测试数据，组装成字典保存到列表中
def get_test_data(sheetname):
    sheet_content=get_sheet_content(sheetname)
    test_data_dict=[]
    for line in sheet_content[1:]:
        test_data_dict.append(dict(zip(sheet_content[0],line)))

    return test_data_dict


# def get_value_by_varname(varname,value):
#     if re.search(r"\${.*?}",value):
#         key=re.search(r"\${(.*?)}").group(1)

# 拿到sheet中是否执行为y的测试数据，并组装成字典格式保存到列表中
# def get_test_cases(sheetname):
#     test_cases=get_test_data(sheetname)
#     result=[]
#     for i in test_cases:
#         if i["是否执行"] !='y':
#             continue
#         result.append(i)
#     return result

# 获取测试步骤，执行测试逻辑
def excute_test_case(xls_file_path,sheetname):
    global wb
    wb = OPExcel(xls_file_path)
    test_case_summarys=get_sheet_content(sheetname)
    for i in range(len(test_case_summarys)):
        flag=True
        test_case_desc=test_case_summarys[i][login_info_sheet_test_description]
        test_case_step_sheetname=test_case_summarys[i][login_info_sheet_step_sheet]
        test_case_data_sheetname = test_case_summarys[i][login_info_sheet_data_sheet]
        test_case_is_run = test_case_summarys[i][login_info_sheet_is_run]

        if (test_case_step_sheetname not in wb.get_sheetnames()) or (test_case_data_sheetname not in wb.get_sheetnames()):
            continue
        if test_case_is_run.lower() !='y':continue

        # 获取测试数据
        test_data=get_test_data(test_case_data_sheetname)
        # 获取测试步骤内容
        test_step_content=get_sheet_content(test_case_step_sheetname)
        for j in range(len(test_data)):
            if test_data[j]['是否执行'].lower() != 'y':
                continue
            if test_case_desc is not None:
                wb.create_sheet(test_case_desc)
            else:
                test_case_desc="测试结果"+str(i+1)

            wb.set_sheet_by_sheetname(test_case_desc)
            # 写入标题栏
            wb.write_row_data(test_step_content[0])
            wb.set_cell_style(wb.get_max_rows(), fgColor="BCEE68")
            driver = None
            # 遍历测试步骤内容
            for k in range(1, len(test_step_content)):
                if test_step_content[k][test_case_step_is_run].lower() != 'y':
                    continue

                keyword = test_step_content[k][test_case_step_keywords]
                locator = test_step_content[k][test_case_step_locator_exp]
                value = test_step_content[k][test_case_step_opete_value]

                if locator is not None and value is not None:
                    value = str(value)
                    # print(value,type(value))
                    if pattern.search(value):
                        key = pattern.search(value).group(1)
                        value = test_data[j][key]

                    command = '%s("%s","%s")' % (keyword, locator, value)
                    log.debug("操作值不为空，执行的命令是：%s" %(command))
                elif locator is None and value is not None:
                    value = str(value)
                    if pattern.search(value):
                        key = pattern.search(value).group(1)
                        value = test_data[j][key]

                    command = '%s("%s")' % (keyword, value)
                elif locator is not None and value is None:
                    command = '%s("%s")' % (keyword, locator)
                else:
                    command = keyword + "()"
                test_step_content[k][test_case_step_opete_value] = value

                try:
                    log.debug("替换后要执行的命令：%s" %command)
                    if "open_browser" in command:
                        driver = eval(command)
                    else:
                        log.info("command的字符串：%s"%command)
                        eval(command)
                    test_step_content[k][test_case_step_excute_time] = TimeUtil().get_datetime()
                    test_step_content[k][test_case_step_excute_result] = "success"
                except ElementNotInteractableException:
                    log.warning("%s 在页面不存在" %test_step_content[k][test_case_step_name_step_description])
                except Exception:
                    captureScreen()
                    flag = False
                    # print(j+1,test_case_step_excute_result,test_case_step_excute_time)
                    # 取消直接写入执行结果单元格
                    # wb.writeContent(k + 1, test_case_step_excute_result, "fail")
                    test_step_content[k][test_case_step_excute_result] = "fail"
                    test_step_content[k][test_case_step_excute_time] = TimeUtil().get_datetime()
                    wb.write_row_data(test_step_content[k])
                    # wb.set_cell_style()
                    log.warning(traceback.format_exc())

                    if driver:
                        driver.quit()
                    break
                else:
                    # print(j + 1, test_case_step_excute_result)
                    # wb.writeContent(k + 1, test_case_step_excute_result, "success")

                    wb.write_row_data(test_step_content[k])
            wb.set_cell_style()
            # 切换sheet页
            wb.set_sheet_by_sheetname(test_case_data_sheetname)
            if flag == True:
                wb.writeContent(j + 2, test_case_data_excute_result, "success")
            else:
                wb.writeContent(j + 2, test_case_data_excute_result, "fail")
            wb.writeContent(j + 2, test_case_data_excute_time, TimeUtil().get_datetime())
        wb.set_sheet_by_sheetname(login_info_sheet)
        if flag == True:
            wb.writeContent(i + 1, login_info_sheet_excute_result, "success")
        else:
            wb.writeContent(i + 1, login_info_sheet_excute_result, "fail")
        wb.writeContent(i + 1, login_info_sheet_excute_time, TimeUtil().get_datetime())


if __name__=="__main__":
    """
    版本3：跟版本一的封装差不多，增加了一个测试数据可以通过指定sheet页来读取的功能，更灵活
    """
    my_log = MyLog()
    log = my_log.get_logger()
    excute_test_case(contacts_file_path,login_info_sheet)
    # print(get_test_cases(contacts_info_sheet))