import pandas as pd
from openpyxl import load_workbook
from config.project_path import *
from tools.get_global_data import GetData
from tools.read_config import ReadConfig
from tools.do_regx import DoRegx


class DoExcel:

    def get_data(self,filename,sheetname):
        wb =load_workbook(filename)
        # mode = eval(ReadConfig.get_config(case_config_path,"MODE","mode"))
        sheet = wb[sheetname]  # 表单名
        test_data =[]

        for case_id in range(2, sheet.max_row+1):
            row_data = {}  # 字典
            is_run = sheet.cell(case_id, int(ReadConfig.get_test_data("run"))).value
            #通过 excel里的run列判断是否把数据加进DDT去执行
            if is_run == 'yes':
                row_data["case_id"] = sheet.cell(case_id, int(ReadConfig.get_test_data("case_id"))).value
                row_data["module"] = sheet.cell(case_id,int( ReadConfig.get_test_data("module"))).value
                row_data["title"] = sheet.cell(case_id, int(ReadConfig.get_test_data("title"))).value
                row_data["url"] = sheet.cell(case_id, int(ReadConfig.get_test_data("url"))).value
                # row_data["data"] = sheet.cell(case_id,int(ReadConfig.get_test_data("request_data"))).value
                #非正则字串符替换
                #替换管理员账户
                # if sheet.cell(case_id+1, int(ReadConfig.get_test_data("request_data"))).value.find("${user}") != -1 and sheet.cell(case_id, int(ReadConfig.get_test_data("request_data"))).value.find("${passwd}") != -1:  # if h后面非空  非零  成立的表达式  都为True，只要是True，if下面的代码都会执行
                #     row_data["data"] = sheet.cell(case_id, int(ReadConfig.get_test_data("request_data"))).value.replace("${user}", getattr(GetData,"admin_user")).replace("${passwd}", str(getattr(GetData,"admin_passwd")))
                # else:
                #     row_data["data"] = sheet.cell(case_id+1, int(ReadConfig.get_test_data("request_data"))).value

                #正则字符串替换   一行替代多行
                row_data["data"] = DoRegx.do_regx(sheet.cell(case_id, int(ReadConfig.get_test_data("request_data"))).value)

                row_data["http_method"] = sheet.cell(case_id,int(ReadConfig.get_test_data("http_method"))).value

                # sql 语句中的字符串替换
                # if sheet.cell(case_id+1, int(ReadConfig.get_test_data("check_sql"))).value !=None:
                #     if sheet.cell(case_id+1,int(ReadConfig.get_test_data("check_sql"))).value.find("${normal_tel}") != -1:
                #         row_data["data"] = sheet.cell(case_id+1, int(ReadConfig.get_test_data("request_data"))).value.replace("${user}", getattr(GetData, "admin_user"))
                # else:
                #     row_data["data"] = sheet.cell(case_id+1, int(ReadConfig.get_test_data("request_data"))).value

                row_data["check_sql"] = sheet.cell(case_id, int(ReadConfig.get_test_data("check_sql"))).value
                row_data["expect"] = sheet.cell(case_id, int(ReadConfig.get_test_data("expect"))).value
                row_data["sheet_name"] = sheetname
                test_data.append(row_data)

            # else:
            #     row_data = {}  # 字典
            #     row_data["case_id"] = sheet.cell(case_id+1, 1).value
            #     row_data["username"] = sheet.cell(case_id+1, 2).value
            #     row_data["password"] = sheet.cell(case_id+1, 3).value
            #     row_data["email"] = sheet.cell(i, 4).value
            #     row_data["sheet_name"] = sheetname
            #     test_data.append(row_data)

        return test_data

    @staticmethod
    def write_back(filename,sheetname,row,col,result):#回写数据
        wb = load_workbook(filename)
        sheet = wb[sheetname]
        sheet.cell(row,col).value = result
        wb.save(filename)#保存结果



if __name__ == '__main__':
    pass