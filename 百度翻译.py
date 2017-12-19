#!/usr/bin/env python
# coding:utf8
# author:Z time:2017/12/9
import requests
word=input('请输入单词: ')
url='http://fanyi.baidu.com/v2transapi'
data={
'from':'en',
'to':'zh',
'query':word,
'transtype':'realtime',
'simple_means_flag':3
}
response=requests.post(url,data)
data=response.json()
#音标
ph_am=data['dict_result']['simple_means']['symbols'][0]['ph_am']
ph_en=data['dict_result']['simple_means']['symbols'][0]['ph_en']
#翻译
mean_info=data['dict_result']['simple_means']['symbols'][0]['parts']
means=''

for item in mean_info:
    means=means+item['part']+''+','.join(item['means'])
print(means)