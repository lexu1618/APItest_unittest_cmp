from config.project_path import *
import pandas as pd
from tools.read_config import ReadConfig


class GetData:
    Cookie = {"ASP.NET_SessionId": "sds02zihbxd2esmxre3ddx0m"}
    # Cookie = None
    admin_user = pd.read_excel(test_case_data_path,sheet_name="init").iloc[1,1]

    admin_passwd = pd.read_excel(test_case_data_path,sheet_name="init").iloc[2,1]



if __name__ == '__main__':
    # setattr(GetData,"Cookie","123456")
    # print(getattr(GetData,"Cookie"))
    # print(hasattr(GetData,"Cookie"))
    print(getattr(GetData,"admin_user"))
    print(getattr(GetData,"admin_passwd"))

