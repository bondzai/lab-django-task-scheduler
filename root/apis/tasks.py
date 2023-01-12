from __future__ import absolute_import, unicode_literals
from celery import shared_task
import requests
from bs4 import BeautifulSoup


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def line_btc():
    url = 'https://notify-api.line.me/api/notify'
    token = 'HSjKlkm6ylCcZoHgtaAbk37EZqOdW52lrXuIw1CFqNb'
    headers = {'content-type': 'application/x-www-form-urlencoded',
               'Authorization': 'Bearer ' + token}

    message = 'Celery Scheduler (executed every 5 minutes)'

    r = requests.post(url, headers=headers, data={
        'message': message,
    })
    return r
