# -
请自行用小黄鸟抓包兽耳桌面  
  
  
需要修改AppID:"************"引号里的内容为自己应用的APPID  
需要修改Authorization:"************************************"引号里的内容为自己应用的Authorization  
例如：  
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
  
如需小米推送  
请下载消息接收，并修改'alias':'%s'%('IlineI')中的 IlineI 为自己在消息接收中设置的别名  
例如requests.get('https://tdtt.top/send',params={'title':'%s'%('兽耳签到通知'),'content':'%s'%(data),'alias':'%s'%('IlineI')} ,verify=False)  
  
  
如无需小米推送，可以删除以下几行  
	print(response1.text)  
	print(response2.text)  
	data = "签到成功\n" + response1.text + response2.text  
	urllib3.disable_warnings()  
	requests.get('https://tdtt.top/send',params={'title':'%s'%('兽耳签到通知'),'content':'%s'%(data),'alias':'%s'%('IlineI')} ,verify=False)  
  
  
云函数触发管理可设置为	  
0 0 */6 * * * *  
或者12小时运行一次  
