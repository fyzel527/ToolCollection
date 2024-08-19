import requests
import json


# 目标URL
url = 'https://devapi.qweather.com/v7/indices/1d'

# 请求参数
params = {
    'type': '1,2',          # 指数类型，多个类型用逗号分隔
    'location': '101010100', # 地区ID
    'key': '79990a8beb284ad1a06b8e3566c697b9'        # 替换为你的实际API密钥
}


# 发出GET请求
response = requests.get(url, params=params)

# 将返回的字典格式化为JSON字符串，并使用双引号
formatted_json = json.dumps(response.json(), indent=4, ensure_ascii=False)
print(formatted_json)
#
# # 显示返回的JSON数据
# print(response.json())