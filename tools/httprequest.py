import requests

from config.project_path import *
from tools.my_log import MyLog
my_logger = MyLog()


class HttpRequest:

    @staticmethod
    def http_request(url,data,http_method,cookie = None):
        try:
            if http_method.upper() == 'GET':
                res = requests.get(url,data,cookies = cookie)
            elif http_method.upper() == "POST":
                res = requests.post(url,data,cookies = cookie)
            else:
                my_logger.info("请求方法错误")
        except Exception as e:
            my_logger.error("请求报错了：{0}".format(e))
            raise e

        return res   #返回消息实体

if __name__ == '__main__':
    hr = HttpRequest()
    url = 'http://172.16.20.25:82/center/login'
    data ={"username":"web","password":"123"}
    res = hr.http_request(url,data,"post")
    print(res.json())