# coding=utf-8
import requests
import json
import mail

url = "http://wechat.leiting.com/weixin/gumballs/201610/gift/common/getGift.php"

payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"type\"\r\n\r\n1\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
headers = {
    'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
    'cache-control': "no-cache",
    }

response = requests.request("POST", url, data=payload, headers=headers)
jo = json.loads(response.text);
mail.SemdMail(jo);
