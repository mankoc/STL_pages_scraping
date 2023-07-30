import requests

url="http://www.gambody.com/api/model/list"


headers={
    'pageSize':'100',
    'page':'1'
}

req=requests.request("GET",url,headers=headers)

aa=0