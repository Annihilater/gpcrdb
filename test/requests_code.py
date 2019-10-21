#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/10/21 17:03
# @Author: PythonVampire
# @email : vampire@ivamp.cn
# @File  : requests_code.py


import requests

url = "https://www.gpcrdb.org/structure/"

headers = {
    'Connection': "keep-alive",
    'Pragma': "no-cache",
    'Cache-Control': "no-cache",
    'Upgrade-Insecure-Requests': "1",
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
    'Sec-Fetch-Mode': "navigate",
    'Sec-Fetch-User': "?1",
    'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    'Sec-Fetch-Site': "same-origin",
    'Accept-Encoding': "gzip, deflate, br",
    'Accept-Language': "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6",
    'Cookie': "___rl__test__cookies=1571626034382; _ga=GA1.2.1899733193.1571621016; _gid=GA1.2.871165181.1571621016; sessionid=ocsgav5opw9fen51jf97s6lzyo6v8kds; csrftoken=AE5FbtmGqPRxBHPPYXqyYAaBisKtgxAK9p9qoAPhUjVMhB0ASe9eLsJjO3MfpqdT; OUTFOX_SEARCH_USER_ID_NCOO=408942309.6615702",
    'Postman-Token': "2977c777-d96f-4c6b-b109-b4ced6c7fbab,faaddb7a-e6be-4685-815a-a59033510fb2",
    'Host': "www.gpcrdb.org",
    'cache-control': "no-cache"
}

# response = requests.request("GET", url, headers=headers)
response = requests.get(url, headers=headers)

print(response.text)
