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
		#self.serach_str = "https://api.github.com/search/users?q=smart+contract"
		self.getSearchStr()
		self.token = self.getToken(_tokenFile)
		self.headers = {'User-Agent':'Mozilla/5.0', 'Authorization':'token ' + str(self.token), 'Content-Type':'application/json', 'method':'GET', 'Accept':'application/json'}
	
	def getSearchStr(self):
		self.serach_str = self.getText("searchStr.txt")
		return serach_str.serach_str 

	def getToken(self, _tokenFile):
		f = open(_tokenFile, "r", encoding = "utf-8")
		token = f.read()
		f.close()
		if "\n" in token:
			return token[:-1]
		else:
			return token

	def getSearchStr(self):
		return self.serach_str

	def getInfo(self, _search_str, _model):
		r = requests.get(_search_str, timeout = 50, headers = self.headers)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		if _model == "-GL":
			self.writeTxt("usersList.txt", r.text, "w")
		return r.text

	def jsonToDict(self, _json):
		dic = json.loads(_json)
		#print(dic["total_count"])
		return dic

	def getText(self, _filename):
		f = open(_filename, "r", encoding = "utf-8")
		content = f.read()
		f.close()
		if content[-1] == "\n":
			return content[:-1]
		return content

	def writeTxt(self, _filename, _content, _mode):
		f = open(_filename, _mode, encoding = "utf-8")
		f.write(_content)
		if _mode != "a+":
			print("File " +_filename+ " has been written.")
		f.close()

	def getUsersLogin(self, _usersDict):
		userItem = _usersDict["items"]
		userLogin = list()
		for i in userItem:
			#userItem is a list
			userLogin.append(i["login"])
		print("Get "+ str(len(userLogin)) +" user logins.")
		return userLogin



	def getUserInfo(self, _usersLogin):
		serach_user_str = "https://api.github.com/users/"
		number = 0
		true_number = 0
		for i in _usersLogin:
			info = self.getInfo(serach_user_str + i, "-GI")
			#print(info)
			infoDict = self.jsonToDict(info)
			email = infoDict["email"]
			if email == None:
				number = number + 1
				print("\r" + str(number) + "/"+str(len(_usersLogin)))
				continue
			else: 
				self.writeTxt("email.txt", email + ';', "a+")
				true_number = true_number + 1
			number = number + 1
			print("\r" + str(number) + "/"+str(len(_usersLogin)))
			#print(infoDict["email"])
			time.sleep(10)
		if number == true_number:
			print("\nAll done.", " :", true_number)
		else:
			print("Only part of the users' email was obtained: ", true_number)
		print("See email addresses in email.txt")

	def run(self):
		#usersList = self.getInfo(self.serach_str)
		usersList = self.getText("usersList.txt")
		usersDict = self.jsonToDict(usersList)
		usersLogin = self.getUsersLogin(usersDict)
		#print(usersLogin)
		self.getUserInfo(usersLogin)
		

def getTokenFile():
	if "windows" in platform.system() or "Windows" in platform.system():
		return "token_win10.txt"
	elif "Linux" in platform.system():
		return "token_linux.txt"


#unit test
if __name__ == "__main__":
	g = getEmail(getTokenFile())

	if len(sys.argv) != 2:
		print("Wrong parameters number.")
	else:
		if sys.argv[1].upper() == "-GL":
			g.getInfo(g.getSearchStr(), "-GL")
		elif sys.argv[1].upper() == "-GI":
			g.run()
		else:
			print("Wrong parameters.")
