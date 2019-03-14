# 车检状态查询代码演示

## 运行DEMO
```
python api_jgj_flow_query.py 
```

## 返回结果

```
请求返回的HEADER:

{
  'Server': 'Tengine', 
  'Date': 'Thu, 14 Mar 2019 13:53:59 GMT', 
  'Content-Type': 'application/json; charset=UTF-8', 
  'Content-Length': '503', 
  'Connection': 'keep-alive', 
  'Access-Control-Allow-Origin': '*', 
  'Access-Control-Allow-Methods': 'GET,POST,PUT,DELETE,HEAD,OPTIONS,PATCH', 
  'Access-Control-Allow-Headers': 'X-Requested-With,X-Sequence,X-Ca-Key,X-Ca-Secret,X-Ca-Version,X-Ca-Timestamp,X-Ca-Nonce,X-Ca-API-Key,X-Ca-Stage,X-Ca-Client-DeviceId,X-Ca-Client-AppId,X-Ca-Signature,X-Ca-Signature-Headers,X-Ca-Signature-Method,X-Forwarded-For,X-Ca-Date,X-Ca-Request-Mode,Authorization,Content-Type,Accept,Accept-Ranges,Cache-Control,Range,Content-MD5', 
  'Access-Control-Max-Age': '172800', 
  'X-Ca-Request-Id': '72AEE0E6-93EC-405A-AB7D-29607E393988'
 }



请求返回的数据:

{'data': [{'datetime': '2019-03-11 13:58:51',
           'plate_number': '京AAR670',
           'status': '登记完成'},
          {'datetime': '2019-03-11 13:58:55',
           'plate_number': '京AAR670',
           'status': '等待尾气检测'},
          {'datetime': '2019-03-13 15:44:24',
           'plate_number': '京AAR670',
           'status': '环保审核'},
          {'datetime': '2019-03-13 16:35:23',
           'plate_number': '京AAR670',
           'status': '检字已发'}],
 'plate_number': '京AAR670',
 'result': 'success'}

```
