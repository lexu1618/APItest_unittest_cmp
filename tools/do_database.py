import pymssql
import json
from tools.read_config import ReadConfig
from dataconfig.project_path import *


class DoDatabase:
    def __init__(self):
        # self.comn = pymssql.connect(server="172.16.20.61", user="sa", password="sa", database="SHHDSN",as_dict=True)  # 获取连接
        # self.cur = self.comn.cursor()  # 获取光标
        # 读取数据库的配置文件
        db_config = eval(ReadConfig.get_sql())
        # 获取数据库连接
        self.comn = pymssql.connect(**db_config)
        # 获取游标
        self.cur = self.comn.cursor()

    def search(self, sql, state="all"):  # 查询只有一个结果用fetchone，返回的是一个元祖，多个结果用fetchall，返回的是嵌套元祖的 列表

        # 执行查询语句
        self.cur.execute(sql)
        if state == 1:
            result = self.cur.fetchone()    #返回一个元祖
        else:
            result = self.cur.fetchall()

        # 关闭游标
        self.cur.close()
        # 关闭连接
        self.comn.close()
        return json.dumps(result)


if __name__ == '__main__':
    operadb = DoDatabase()
    result = operadb.search("SELECT * FROM [SHHDSN].[dbo].[Dsn_admin]",1)
    print(result)
    print(type(result))