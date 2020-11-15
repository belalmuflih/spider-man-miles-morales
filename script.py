import requests,time,smtplib
from bs4 import BeautifulSoup

URL = "https://store.playstation.com/ar-sa/concept/10000649"
res = requests.get(URL)
res = BeautifulSoup(res.text, 'html.parser')
find = res.findAll(class_='psw-h3')

item = find[-1].text.split('$')
price = item[1]



sender = 'ENTER SENDER EMAIL'
rec = 'RECIVER EMAIL'
password = 'SENDER PASSWORD'
msg = """Hey the price have changed!

    https://store.playstation.com/ar-sa/concept/10000649
"""



run = True
while run:
    if price < '79.99':
        try:
            server = smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            server.login(sender,password)
            server.sendmail(sender, rec, msg)
        except Exception as e:
            print(e)
        run = False
    else:
        print("NOT YET...")
        time.sleep(86400/2)
