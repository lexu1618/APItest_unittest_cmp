import os
import time

#读取位置
project_path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]

#测试数据路径
test_case_data_path = os.path.join(project_path,"test_data","case.xlsx")

#配置文件路径
config_path = os.path.join(project_path,"dataconfig","config.ini")

#用例执行控制路径
caseList_path = os.path.join(project_path,"dataconfig","caselist.txt")

#测试用例路径
test_case_path = os.path.join(project_path,"testcase")


#测试报告路径
now = time.strftime("%Y-%m-%d %H-%M-%S")
report_path = os.path.join(project_path,"test_result","html_report",now+"-"+"api_test.html")

#日志输出路径
log_path = os.path.join(project_path,"test_result","log","runlog.log")


if __name__ == '__main__':
    print(project_path)
    print(report_path)
    print(config_path)
    print(log_path)
    print(caseList_path)
    print(test_case_data_path)