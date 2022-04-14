# -*- coding: utf8 -*-
from importlib import import_module
import requests
from requests.packages import urllib3

def abc():
	url1 = "https://api1.mimikko.cn/client/love/ExchangeReward?code=nemuri"
	url2 = "https://api1.mimikko.cn/client/RewardRuleInfo/SignAndSignInformationV3"
	url3 = "https://api1.mimikko.cn/client/roll/RollReward"
	url4 = "https://api1.mimikko.cn/client/mission/ReceiveMemberLevelWelfare"
	payload = {}
	headers = {
			"Cache-Control":"no-cache",
			"AppID":"wjB7UIO2sYkaNKLD",
			"Version":"3.3.3",
			"Authorization":"123d13sd-2132-1234-1234-123412341234",
			"Host":"api1.mimikko.cn",
			"Connection":"Keep-Alive",
			"Accept-Encoding":"gzip",
			"User-Agent":"okhttp/3.12.1",
	}

	response1 = requests.request("GET", url1, headers=headers, data=payload)
	response2 = requests.request("GET", url2, headers=headers, data=payload)
	response3 = requests.request("POST", url3, headers=headers, data=payload)
	response4 = requests.request("POST", url4, headers=headers, data=payload)
	print(response1.text)
	print(response2.text)
	print(response3.text)
	print(response4.text)
	data = "签到成功\n" + response1.text + response2.text + response3.text + response4.text
	urllib3.disable_warnings()
	requests.get('https://tdtt.top/send',params={'title':'%s'%('兽耳签到通知'),'content':'%s'%(data),'alias':'%s'%('IlineI')} ,verify=False)
def main_handler(event=None, context=None):
	abc()
