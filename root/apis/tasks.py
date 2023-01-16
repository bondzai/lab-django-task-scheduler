from __future__ import absolute_import, unicode_literals
from celery import shared_task
import requests
from bs4 import BeautifulSoup

def get_data_from_api():
    target_url = "https://coinmarketcap.com/currencies/bitcoin/"
    res = requests.get(target_url)
    res.encoding = "utf-8"
    print(res)

    soup = BeautifulSoup(res.text, 'html.parser')
    data_all = soup.prettify()
    find_all = soup.find_all("div", {"class": "priceValue"})
    print(find_all)

    btc_value = []

    for i in find_all:
        i = str(i).split('<div class="priceValue"><span>', 1)
        i = str(i).split('</span></div>', 1)
        btc_value = i
        break

    buffer = btc_value[0].split("['', '", 1)
    output = 'BTC price = ' + buffer[1]
    return output

@shared_task
def line_notify():
    btc = get_data_from_api()
    url = 'https://notify-api.line.me/api/notify'
    token = 'VE2zPeTr3xfiESJPElym7sLp8vCtXTxhAfT7KaTNgCf'
    headers = {'content-type': 'application/x-www-form-urlencoded',
               'Authorization': 'Bearer ' + token}

    message = 'Celery Scheduler (executed every 10 mins) ' + btc

    r = requests.post(url, headers=headers, data={
        'message': message,
    })
    return r
