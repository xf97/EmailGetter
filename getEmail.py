#!/usr/bin/python
#-*- coding:utf-8 -*-

import requests



class getEmail:
	def __init__(self):
		self.page = 1
		self.serach_str = "https://github.com/search?p="+str(self.page)+"&q=smart+contract&type=Users"

	def getText(self):
		try:
			r = requests.get(self.serach_str, timeout = 50)
			r.raise_for_status()
			r.encoding = r.apparent_encoding
			return r.text
		except:
			print("获得 "+_url+" 出现异常.")

	def makeUrl(self):
		self.page += 1
		self.serach_str = "https://github.com/search?p="+str(self.page)+"&q=smart+contract&type=Users"

	def run(self, _userNum):
		if _userNum % 10 == 0:
			loopNum = _userNum // 10 
		else:
			loopNum = _userNum // 10 + 1
		for i in range(1, loopNum):
			self.makeUrl()
			print(self.serach_str)


#unit test
if __name__ == "__main__":
	g = getEmail()
	text = g.getText()
	f = open("html.txt", "w", encoding = "utf-8")
	f.write(text)
	f.close()
	#g.run(658)