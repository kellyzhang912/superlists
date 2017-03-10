#!/usr/bin/env python
#_*_coding:utf-8 _*_
__author__ = 'zhangxin'

import requests
#
headers = {
    #"token": token,
    "Host": "192.168.10.225:9898",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Accept-Encoding": "gzip, deflate",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Requested-With": "XMLHttpRequest",
    "Connection": "keep-alive",
    "Content-Length": "18",
    "charset": "UTF-8",
    "Content-Length": "36",
    #"Referer": "http://192.168.10.228:38090/wu_rcs_web/admin/login/",
   # "cookie": "token=" + token
 }

s=requests.session()
ac ={'j_username':'zhangxin','j_password':'wss808791','from':'/','json':'{"j_username": "zhangxin", "j_password": "wss808791", "remember_me": false, "from": "/"}','Submit':'登录'}
p1={'from':'/'}
#r=s.post('http://192.168.10.225:9898/login',data=p1,headers=headers)
r=s.post('http://192.168.10.225:9898/j_acegi_security_check',data=ac,headers=headers)
r=s.post('http://192.168.10.225:9898/view/xin/job/rcs/build?delay=0sec')
print(r.status_code)

