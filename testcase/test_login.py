from tools.httprequest import HttpRequest
import unittest
from tools.get_global_data import GetData
from libs.ddt import ddt,data    #列表嵌套字典、列表嵌套列表
from tools.do_excel import DoExcel
from dataconfig.project_path import *
from tools.my_log import MyLog
from tools.read_config import ReadConfig

my_logger = MyLog()
do_excel = DoExcel(test_case_data_path,"login")
test_data = do_excel.get_all_data()



@ddt
class TestLogin(unittest.TestCase):
    def setUp(self):
        pass

    @data(*test_data)
    def test_login(self,item):
        my_logger.info("用例{0}-{1}{2}------开始执行".format(item["case_id"],item["module"],item["title"]))
        res = HttpRequest.http_request(item["url"],eval(item['data']),item["http_method"])
        # self.assertEqual("200",res.json()["code"])

        try:
            self.assertIn(item["expect"], res.json())  # 存在excel里的不是数字就是字符串，请求的返回值是字符串，所以要转型
            TestResult = 'Pass'
        except AssertionError as e:
            TestResult = 'Fail'
            my_logger.error("执行用例出错：{0}".format(e))
            raise e
        finally:#不管对还是错，，finally后面代码都执行
            # do_excel.write_back(test_case_data_path,"login",item['case_id']+1,int(ReadConfig.get_test_data("result")),str(res.json())) #res 返回的是字典，要转成字符串才能写进EXCEL\
            # do_excel.write_back(test_case_data_path, "login", item['case_id']+1, int(ReadConfig.get_test_data("test_result")),TestResult)
            do_excel.write_back(item['case_id'] + 1,
                                int(ReadConfig.get_test_data("result")), str(res.json()))  # res 返回的是字典，要转成字符串才能写进EXCEL\
            do_excel.write_back(item['case_id'] + 1,
                                int(ReadConfig.get_test_data("test_result")), TestResult)
            my_logger.info("获取到的结果是:{0}".format(res.json()))
            my_logger.info("用例{0}执行结束".format(item["case_id"]))
            my_logger.info("*"*40)
    def tearDown(self):
        pass