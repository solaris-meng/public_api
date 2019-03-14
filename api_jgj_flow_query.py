
import requests
import datetime
import json
import hmac
import base64
import hashlib
import pprint

from uuid import uuid4

#
# 客户端调用接口的权限参数
#   (要保密)
#
AppKey = '25831867'
AppSecret = '87f1cce5e5cd7162fe852e3c4c0c8971'


#
# 以下为测试代码，演示如何调用查询接口
#
# 接口URL
url = 'http://api.yanshanjiance.cn/api/flow'

# POST请求的JSON格式参数
data_post = {
    "plate_number": "京AAR670",
}
data_post_json = json.dumps(data_post)

nonce = uuid4().hex

# HTTP请求HEADER
headers = {}
headers['X-Ca-Key'] = AppKey
headers['X-Ca-Nonce'] = nonce  # 避免重复攻击
headers['X-Ca-Signature-Headers'] = 'X-Ca-Key,X-Ca-Nonce'


# 生成加密签名，该签名最终放在HEADER中
#   stringToSign - 为签名字符串
#   sign         - 为签名
stringToSign = ''
stringToSign += 'POST'+'\n'
stringToSign += '*/*\n'
stringToSign += '\n'
stringToSign += 'application/json\n'
stringToSign += '\n'
stringToSign += 'X-Ca-Key:'+AppKey+'\n'
stringToSign += 'X-Ca-Nonce:'+nonce+'\n'
stringToSign += '/api/flow'

# 生成签名
sign = stringToSign.encode('utf-8')
aks = AppSecret.encode('utf-8')
h = hmac.new(aks, sign, hashlib.sha256)
sign = base64.b64encode(h.digest())
sign = sign.decode()

print('stringToSign - %s, sign - %s' % (stringToSign, sign))
headers['X-Ca-Signature'] = sign


# 发送请求
r = requests.post(url, headers=headers, json=data_post)

print('请求返回的HEADER:\n')
pprint.pprint(r.headers)
print('\n\n\n请求返回的数据:\n')
pprint.pprint(r.json())
