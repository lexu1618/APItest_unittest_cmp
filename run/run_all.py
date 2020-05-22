import unittest
from libs.HTMLTestRunnerNew import HTMLTestRunner
from dataconfig.project_path import *

# from testcase.test_login import TestLogin
# from testcase.test_select_his import TestSelectHis



suite = unittest.TestSuite()
# # suite.addTest(TestHttpRequest("test_api"))   #测试类的实例
loader = unittest.TestLoader()
# suite.addTest(loader.loadTestsFromTestCase(TestLogin))
# suite.addTest(loader.loadTestsFromTestCase(TestSelectHis))
# with open(report_path,"wb") as fp:
#     runner = HTMLTestRunner(stream=fp,title='test_api',description="接口测试报告",tester="lexus")
#     runner.run(suite)


class AllTest:
    def __init__(self):
        self.case_list = []

    def set_case_list(self):
        """
                读取caselist.txt文件中的用例名称，并添加到caselist元素组
                :return:
                """
        with open(caseList_path) as fp:
            for value in fp.readlines():
                data = str(value)
                print(data)
                if data != '' and not data.startswith("#"):  # 如果data非空且不以#开头
                    self.case_list.append(data.replace("\n", ""))  # 读取每行数据会将换行转换为\n，去掉每行数据中的\n
                    # self.case_list.append(data)

            return self.case_list

    def set_case_suite(self):

        self.set_case_list()#通过set_case_list()拿到caselist元素组
        test_suite = unittest.TestSuite()
        suite_module = []
        for case in self.case_list:#从caselist元素组中循环取出case

            #批量加载用例，第一个参数为用例存放路径，第二个参数为路径文件名
            discover = unittest.defaultTestLoader.discover(test_case_path, pattern=case + '.py', top_level_dir=None)
            suite_module.append(discover)#将discover存入suite_module元素组
            print('suite_module:'+str(suite_module))
        if len(suite_module) > 0:#判断suite_module元素组是否存在元素
            for suite in suite_module:#如果存在，循环取出元素组内容，命名为suite
                for test_name in suite:#从discover中取出test_name，使用addTest添加到测试集
                    test_suite.addTest(test_name)
        else:
            print('else:')
            return None
        return test_suite#返回测试集



    def run(self):
        self.suite = self.set_case_suite()
        with open(report_path,"wb") as fp:
            runner = HTMLTestRunner(stream=fp,title='test_api',description="接口测试报告",tester="lexus")
            runner.run(self.suite)




if __name__ == '__main__':

    AllTest().run()