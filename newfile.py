import requests,uuid,secrets
print("""——————————————————By :𝐒𝐈𝐑 DAKSAR
 """)
print("--------------------------")
print("Follow me instagram @dak.sr")
print("--------------------------")                                     
 
from time import sleep
uid = uuid.uuid4()
 
 
 
 
r = requests.Session()
cookie = secrets.token_hex(1)*0
username = input('username:')
password = input('  password :')
target = input('username :')
sle = int(input('slep 7on1:'))
def login():
    global username
    global password
    url = 'https://www.instagram.com/accounts/login/ajax/'
    headers = {"user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36', 'x-csrftoken': 'missing', 'mid': cookie}
    data = {'username':username,
            'enc_password': '#PWD_INSTAGRAM_BROWSER:0:1589682409:{}'.format(password),
            'queryParams': '{}',
            'optIntoOneTap': 'false',}
    req_login = r.post(url,headers=headers,data=data)
    if ("userId") in req_login.text:
        r.headers.update({'X-CSRFToken': req_login.cookies['csrftoken']})
        print('login True')
        url_id = 'https://www.instagram.com/{}/?__a=1'.format(target)
        req_id = r.get(url_id).json()
        user_id = str(req_id['logging_page_id'])
        idd = user_id.split('_')[1]
        done = 1
        while True:
            url_report = 'https://www.instagram.com/users/{}/report/'.format(idd)
            datas = {'source_name':'','reason_id':1,'frx_context':''} #spam
            report = r.post(url_report,data=datas)
            print('done spam {}'.format(done))
            sleep(sle)
            done += 1


    else:
        print('login false')
        exit()
 


login()