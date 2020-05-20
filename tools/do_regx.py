import re
from tools.get_global_data import GetData
from tools.read_config import ReadConfig

# s = "www.lefix.com"  #目标字符串
# res = re.match("(w)(ww).*",s)  #全匹配   头部匹配  只匹配一次
# print(res)
# print(res.group())  #分组 根据括号里的正则表达式去分组   group() == group(0)  拿到匹配的全字符
# print(res.group(1))    #（）就是分组，group（1）就是拿第一个括号里的内容
# print(res.group(2))
#
# res = re.findall('(le)(fix)',s)  #返回的是列表
# #如果有分组，就是以元祖的形式表现，列表嵌套元祖
# print(res)
#
# #替换一个
# s = '{"username":"${user}","password":"passwd"}'    #字符串
#
# #search  每次只匹配一个
# res = re.search('\$\{(.*)\}',s)
# print(res.group())
#
# res = re.search('\$\{(.*?)\}',s)   # .*？  匹配到第一个就停止       （）就是分组，group（1）就是拿第一个括号里的内容
# print(res)
# key = (res.group(0))
# value = (res.group(1))
# print(key,value)
# new_s = s.replace(key,str(getattr(GetData,"admin_user")))
# print(new_s)


PATTERN = eval(ReadConfig.get_regx())
class DoRegx:
#替换包多个字符串

    @staticmethod
    def do_regx(s):
        #search  每次只匹配一个
        # while re.search('\$\{(.*?)\}',s):
        #     key =re.search('\$\{(.*?)\}',s).group(0)
        #     value = re.search('\$\{(.*?)\}',s).group(1)
        #     s = s.replace(key,str(getattr(GetData,value)))

        res = re.findall(PATTERN,s)
        for item in range(len(res)):
            s = s.replace("${"+res[item]+"}", str(getattr(GetData, res[item])))
                                            # 也可以把要替换的数据写到config中，这里就换成读取配置文件的写法

        return s
if __name__ == '__main__':
    s = '{"username":"${admin_user}","password":"${admin_passwd}"}'
    print(DoRegx.do_regx(s))


    # import re
    # from tools.get_global_data import GetData
    # PATTERN = '\$\{(.*?)\}'
    # s = '{"username":"${admin_user}","password":"${admin_passwd}"}'
    # res = re.findall(PATTERN,s)
    # print(res)
    # print(res[1])
    # print(getattr(GetData,res[1]))
    #
    # for item in range(len(res)):
    #     print(res[item])
    #     s = s.replace("${"+res[item]+"}", str(getattr(GetData, res[item])))
    # print(s)