import configparser
from config.project_path import *

cf = configparser.ConfigParser()
cf.read(config_path,encoding="utf-8")



class ReadConfig:
    @staticmethod
    def get_http(option):
        return cf["HTTP"][option]


    @staticmethod
    def get_sql():
        return cf["DB"]["db_config"]


    @staticmethod
    def get_test_data(col_name):
        return cf["DATA"][col_name]

    @staticmethod
    def get_regx():
        return cf["REGX"]["PATTERN"]

    # @staticmethod
    # def get_case_run():
    #     return cf["MODE"]["mode"]

if __name__ == '__main__':
    # from config.project_path import *
    # rd = ReadConfig()
    # case_config = rd.read_config(case_config_path,"MODE","mode")
    # print(case_config)

    print(ReadConfig.get_http("port"))
    print(ReadConfig.get_sql())
    print(type(ReadConfig.get_test_data("case_id")))
    print(ReadConfig.get_regx())