#!/usr/bin/python
#-*- coding:utf-8 -*-


'''
__author__ = xiaofeng
'''

import requests
import os
import platform
import sys
import json
import time




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

	def getInfo(self, _search_str):
		r = requests.get(_search_str, timeout = 50, headers = self.headers)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		#self.writeTxt("usersList.txt", r.text)
		return r.text

	def jsonToDict(self, _json):
		dic = json.loads(_json)
		#print(dic["total_count"])
		return dic

	def getText(self, _filename):
		f = open(_filename, "r", encoding = "utf-8")
		content = f.read()
		f.close()
		return content

	#unuse
	def makeUrl(self):
		self.page += 1
		self.serach_str = "https://github.com/search?p="+str(self.page)+"&q=smart+contract&type=Users"

	def writeTxt(self, _filename, _content):
		f = open(_filename, "w", encoding = "utf-8")
		f.write(_content)
		print("File " +_filename+ " has been written.")
		f.close()

	def getUsersLogin(self, _usersDict):
		userItem = _usersDict["items"]
		userLogin = list()
		for i in userItem:
			#userItem is a list
			userLogin.append(i["login"])
		print(len(userLogin))
		return userLogin



	def getUserInfo(self, _usersLogin):
		serach_user_str = "https://api.github.com/users/"
		for i in _usersLogin:
			info = self.getInfo(serach_user_str + i)
			infoDict = self.jsonToDict(info)
			print(infoDict["email"])
			time.sleep(60)
		print("get done.")

	def run(self):
		usersList = self.getInfo(self.serach_str)
		#usersList = self.getText("usersList.txt")
		usersDict = self.jsonToDict(usersList)
		usersLogin = self.getUsersLogin(usersDict)
		self.getUserInfo(usersLogin)
		

def getTokenFile():
	if "windows" in platform.system() or "Windows" in platform.system():
		return "token_win10.txt"
	elif "Linux" in platform.system():
		return "token_linux.txt"


#unit test
if __name__ == "__main__":
	g = getEmail(getTokenFile())
	text = g.run()