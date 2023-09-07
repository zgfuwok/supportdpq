import os,sys
from datetime import datetime
import time
from threading import Thread
try:
    import requests
except:
    os.system('pip install requests')
    import requests
dem = 0
list_token = []
def clear():
    os.system("cls" if os.name == "nt" else "clear")

ban = """

\033[1;37m██╗   ██╗██╗██████╗ ███████╗██╗  ██╗ █████╗ ██████╗ ███████╗
\033[1;33m██║   ██║██║██╔══██╗██╔════╝██║  ██║██╔══██╗██╔══██╗██╔════╝
\033[1;36m██║   ██║██║██████╔╝███████╗███████║███████║██████╔╝█████╗  
\033[1;34m╚██╗ ██╔╝██║██╔═══╝ ╚════██║██╔══██║██╔══██║██╔══██╗██╔══╝  
\033[1;31m ╚████╔╝ ██║██║     ███████║██║  ██║██║  ██║██║  ██║███████╗
\033[1;35m  ╚═══╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝                                                            
\033[1;34m        \ Tool được tổng hợp bởi Dương Phú Quốc / 
\033[1;34m        \ FACEBOOK: facebook.com/100042415576964 /
"""
def banner():
  os.system("clear")
  for h in ban:
    sys.stdout.write(h)
    sys.stdout.flush()
    time.sleep(0.003)    
banner()

def run_share(id_post,token):
#     # sharepost = requests.get(f'https://graph.facebook.com/me/feed?method=POST&link=https://m.facebook.com/{id_post}&published=0&access_token={token}').json()
#     # if 'id' in sharepost:
#     #     idshare = sharepost['id']
#     #     print(f'{datetime.now().strftime("%H:%M:%S")} : Quoccdeptryvcl : SUCCESS : {idshare}')
#     # else:
#     #     print(f'{datetime.now().strftime("%H:%M:%S")} : Quoccdeptryvcl : FALSE')
    try:
        sharepost = requests.get(f'https://graph.facebook.com/me/feed?method=POST&link=https://m.facebook.com/{id_post}&published=0&access_token={token}').json()
        print(f'{datetime.now().strftime("%H:%M:%S")} : DuonggPhuQuocc_Cuti_Vcl : SUCCESS : {sharepost["id"]}')
    except Exception as e:
        print(f'{datetime.now().strftime("%H:%M:%S")} :  DuonggPhuQuocc_Cuti_Vcl  : FALSE')
        
print('\033[1;32mMỌI VẤN ĐỀ KHI CHẠY TOOL IB TRỰC TIẾP FACEBOOK HỖ TRỢ !')
print('TOKEN PROFILE REG LÂU NHỚ XÓA TRÁNH DÙNG TOKEN PROFILE CŨ BỊ DIE')
id_post = input('ID POST : ')
so_luong = int(input('SỐ LƯỢNG SHARE MUỐN TĂNG : '))
delay = int(input('DELAY GIỮA CÁC LẦN SHARE : '))
print("""
MODE 1 CHƯA CÓ TOKEN PROFILE
MODE 2 NẾU CÓ SẴN TOKEN PROFILE
[TRICK : CÓ THỂ CHỌN 1 VÀ ĐỂ NHIỀU TAB ĐỂ GET TOKEN PROFILE NHANH NHẤT NẾU CÓ NHIỀU COOKIE!]""")
mode = int(input('MODE : '))
clear()
if mode == 1:
    try:
        cookie_file =  open('token.txt','r',encoding="utf-8").read().split('\n')
        if len(cookie_file) >= 1:
            print('TÌM THẤY TOKEN TRONG FILE TOKEN.TXT HÃY CHẮC CHẮN ĐÂY LÀ TOKEN ACC MẸ CHỨA PROFILE CHỨ KHÔNG PHẢI PROFILE')
            submit = input('DÙNG TOKEN FILE NÀY CHỨ ? [Y/N]:')
            if submit == "Y" or submit =="y":
                print('XÁC NHẬN DÙNG TOKEN TRONG FILE TOKEN.TXT!')
                for get in cookie_file:
                    tokenn = requests.get('https://graph.facebook.com/me/accounts?access_token='+get).json()['data']
                    for token in tokenn:
                        token_profile = token['access_token']
                        print(f'NAME PROFILE : {token["name"]} | ID PROFILE : {token["id"]}')
                        write_token = open('token_profile.txt','a+').write(token_profile+'\n')
                open_file = open('token_profile.txt','r+',encoding="utf-8").read().split('\n')
                print(f'CÓ {len(open_file)} TOKEN PROFILE TRONG FILE TOKEN_PROFILE.TXT')

            elif submit == "quit":
                quit()
            else:
                while True:
                    try:
                        cookie_file = input(f'FILE CHỨA COOKIE : ')
                        if cookie_file == "quit":quit()
                        open_cookie_file =  open(cookie_file,'r',encoding="utf-8").read().split('\n')
                        print(f'CÓ {len(open_cookie_file)} COOKIE TRONG FILE')
                        break
                    except:
                        print(f'NHẬP FILE CHỨA VÔ ! ')
                for cookie in open_cookie_file:
                    token = requests.get('https://www.facebook.com/dialog/oauth?client_id=124024574287414&redirect_uri=https://www.instagram.com/accounts/signup/&&scope=email&response_type=token',headers={'cookie':cookie}).url
                    check_token = token.split('#access_token=')[1].split('&data_access')[0]
                    list_token.append(check_token)
                for get in list_token:
                    tokenn = requests.get('https://graph.facebook.com/me/accounts?access_token='+get).json()['data']
                    for token in tokenn:
                        token_profile = token['access_token']
                        print(f'NAME PROFILE : {token["name"]} | ID PROFILE : {token["id"]}')
                        write_token = open('token_profile.txt','a+').write(token_profile+'\n')
                open_file = open('token_profile.txt','r+',encoding="utf-8").read().split('\n')
                print(f'CÓ {len(open_file)} TOKEN PROFILE TRONG FILE TOKEN_PROFILE.TXT')    
    except:
        while True:
            try:
                cookie_file = input(f'FILE CHỨA COOKIE : ')
                if cookie_file == "quit":quit()
                open_cookie_file =  open(cookie_file,'r',encoding="utf-8").read().split('\n')
                print(f'CÓ {len(open_cookie_file)} COOKIE TRONG FILE')
                break
            except:
                print(f'NHẬP FILE CHỨA VÔ ! ')

        for cookie in open_cookie_file:
            token = requests.get('https://www.facebook.com/dialog/oauth?client_id=124024574287414&redirect_uri=https://www.instagram.com/accounts/signup/&&scope=email&response_type=token',headers={'cookie':cookie}).url
            check_token = token.split('#access_token=')[1].split('&data_access')[0]
            list_token.append(check_token)

        for get in list_token:
            tokenn = requests.get('https://graph.facebook.com/me/accounts?access_token='+get).json()['data']
            for token in tokenn:
                token_profile = token['access_token']
                print(f'NAME PROFILE : {token["name"]} | ID PROFILE : {token["id"]}')
                write_token = open('token_profile.txt','a+').write(token_profile+'\n')
        open_file = open('token_profile.txt','r+',encoding="utf-8").read().split('\n')
        print(f'CÓ {len(open_file)} TOKEN PROFILE TRONG FILE TOKEN_PROFILE.TXT')

elif mode == 2:
	cookie_file = input(f'FILE CHỨA TOKEN PROFILE : ')
	open_file = open(cookie_file,'r',encoding="utf-8").read().split('\n')
	print(f'CÓ {len(open_file)} TOKEN PROFILE TRONG FILE TOKEN_PROFILE.TXT')

time.sleep(5)
clear()
for i in range(0,so_luong,+1):
	for token in open_file:
		Thread(target=run_share,args=(id_post,token)).start()
		time.sleep(delay)
	time.sleep(1)