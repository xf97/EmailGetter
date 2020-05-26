#!/usr/bin/python
#-*- coding:utf-8 -*-


'''
__author__ = xiaofeng
'''

import requests
import os
import platform
import sys




class getEmail:
	def __init__(self, _tokenFile):
		self.page = 1
		#self.serach_str = "https://api.github.com/users/perfectmak"
		self.serach_str = "https://api.github.com/search/users?q=smart+contract"
		self.token = self.getToken(_tokenFile)
		self.headers = {'User-Agent':'Mozilla/5.0', 'Authorization':'token ' + str(self.token), 'Content-Type':'application/json', 'method':'GET', 'Accept':'application/json'}
		
	def getToken(self, _tokenFile):
		f = open(_tokenFile, "r", encoding = "utf-8")
		token = f.read()
		f.close()
		if "\n" in token:
			return token[:-1]
		else:
			return token

	def getText(self):
		r = requests.get(self.serach_str, timeout = 50, headers = self.headers)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		writeTxt("usersList.txt", r.text)

	def makeUrl(self):
		self.page += 1
		self.serach_str = "https://github.com/search?p="+str(self.page)+"&q=smart+contract&type=Users"

	def writeTxt(self, _filename, _content):
		f = open(_filename, "w", encoding = "utf-8")
		f.write(_content)
		print("File " +_filename+ " has been written.")
		f.close()

	def run(self):
		self.getText()
		

def getTokenFile():
	if "windows" in platform.system() or "Windows" in platform.system():
		return "token_win10.txt"
	elif "Linux" in platform.system():
		return "token_linux.txt"


#unit test
if __name__ == "__main__":
	g = getEmail(getTokenFile())
	text = g.run()