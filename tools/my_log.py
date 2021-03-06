#logging日志打印模块

import logging
from dataconfig.project_path import *

class MyLog:
    def my_log(self,msg,level):
        # 定义一个日志收集器
        my_logger = logging.getLogger()
        # 设定级别   收集和输出不指定级别会默认收集和输出warning级别以上的
        my_logger.setLevel("DEBUG")
        # 设置输出格式
        formatter = logging.Formatter(
            "%(asctime)s -%(levelname)s - %(filename)s[line:%(lineno)d] %(levelname)s-日志信息：%(message)s")
        # 创建一个我们自己的输出渠道-控制台
        ch = logging.StreamHandler()
        ch.setLevel("DEBUG")
        ch.setFormatter(formatter)
        # 指定输出到文件（追加写入）
        fh = logging.FileHandler(log_path, encoding="utf-8")
        fh.setLevel("DEBUG")
        fh.setFormatter(formatter)

        # 两者对接
        my_logger.addHandler(ch)
        my_logger.addHandler(fh)

        # 收集日志
        if level == "DEBUG":
            my_logger.debug(msg)
        elif level == "INFO":
            my_logger.info(msg)
        elif level == "WARNING":
            my_logger.warning(msg)
        elif level == "ERROR":
            my_logger.error(msg)
        elif level == "CRITICAL":
            my_logger.critical(msg)


        #关闭日志收集器  不关闭就会打印重复日志
        my_logger.removeHandler(ch)
        my_logger.removeHandler(fh)

    def debug(self,msg):
        self.my_log(msg,"DEBUG")

    def info(self,msg):
        self.my_log(msg,"INFO")

    def warning(self,msg):
        self.my_log(msg,"WARNING")

    def error(self,msg):
        self.my_log(msg,"ERROR")

    def critical(self,msg):
        self.my_log(msg,"CRITICAL")


if __name__ == '__main__':
    my_logger = MyLog()
    my_logger.debug("1")
    my_logger.info("2")
    my_logger.error("3")