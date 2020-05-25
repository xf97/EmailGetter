#!/usr/bin/python
#-*- coding:utf-8 -*-

import requests



class getEmail:
	def __init__(self, _tokenFile):
		self.page = 1
		self.serach_str = "https://api.github.com/users/perfectmak"
		#self.serach_str = "https://api.github.com/search/users?q=smart+contract"
		self.token = self.getToken(_tokenFile)
		self.headers = {'User-Agent':'Mozilla/5.0', 'Authorization':'token ' + str(self.token), 'Content-Type':'application/json', 'method':'GET', 'Accept':'application/json'}
		
	def getToken(self, _tokenFile):
		f = open(_tokenFile, "r", encoding = "utf-8")
		token = f.read()
		f.close()
		return token

	def getText(self):
		r = requests.get(self.serach_str, timeout = 50, headers = self.headers)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		return r.text

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
	g = getEmail("token_win10.txt")
	text = g.getText()
	f = open("html.txt", "w", encoding = "utf-8")
	f.write(text)
	f.close()
	#g.run(658)