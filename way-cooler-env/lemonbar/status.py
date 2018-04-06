#! /bin/env python
# -*- coding: utf-8 -*-

BCOLOR = "#000000"
FCOLOR = "#efefef"
CRYPTOS = {
    'ETH': 'Ξ', 
    'BCH': "\uf15a",
    'LUN': "LUN",
}
SHELF_PATH = '~/.cache/bar-status.dat'

import os
import sys
import locale
import subprocess
import requests
import shelve
from datetime import datetime

def get_price_url(ticker):
    return 'https://min-api.cryptocompare.com/data/price?fsym={}&tsyms=USD'.format(ticker)

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
shelf = shelve.open(os.path.expanduser(SHELF_PATH), writeback=True)
now = datetime.now()

# Set background and foreground
print("%{{B{}}}%{{F{}}}".format(BCOLOR, FCOLOR), end='')

# Center align
print("%{c}   ", end='')

#
# Networking 
#
result = subprocess.check_output(["ip addr show enp4s0 | grep inet | awk '{ print $2; }'"], shell=True)
if result:
    ips = result.split(b'\n')
    i = 1
    for ip in ips:
        if ip != b'':
            print("{}".format(ip.decode('utf-8')), end='')
            if i < len(ips) - 1:
                print("   \u2022   ", end='')
        i += 1

# Right align
print("   %{r}   ", end='')

#
# Crypto Prices
#
first_fetch = False
if not shelf.get('prices'):
    shelf['prices'] = {}
    first_fetch = True

for tick in CRYPTOS.keys():
    jason = {}
    if (first_fetch or (now.minute % 10 == 0 and now.second == 1)) or not shelf['prices'].get(tick):
        print("getting crypto prices...", file=sys.stderr)
        resp = requests.get(get_price_url(tick))
        if resp.status_code == 200:
            jason = resp.json()
            shelf['prices'][tick] = jason
    else:
        jason = shelf['prices'].get(tick)
    
    print("{} {}   \u2022   ".format(CRYPTOS[tick], locale.currency(jason.get('USD'))), end='')

print(now.strftime('%A %b %d, %H:%M:%S'), end='')

print('%{F-}%{B-}', end='')

shelf.close()