
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################

# Usage:
#
# $ py3 main.py
#     Name    : main.py
#     Version : 0
#     Status  : Development
#     Contact : <ekachai.suriya@gmail.com>
#     Licence : WTFPLv3.1
#
#     Copyleft (ↄ) 2022, Eakkz <ekachai.suriya@gmail.com>

################################################################

from bitkub import Bitkub 

import datetime
import os
import requests


# API info
API_HOST = 'https://api.bitkub.com'
API_KEY = '2adc3b7e1ad967abfc9fde5ad1f0796b'
API_SECRET = b'8fb4ec2e4edcdaeee9a7c4d54184ef9e'

bitkub = Bitkub()
bitkub.set_api_key(API_KEY)
bitkub.set_api_secret(API_SECRET)

timestamp = datetime.datetime.fromtimestamp(bitkub.servertime())

print(timestamp)
print(bitkub)

# This project is libre, and licenced under the terms of the
# DO WHAT THE FUCK YOU WANT TO PUBLIC LICENCE, version 3.1,
# as published by dtf on July 2019. See the COPYING file or
# https://ph.dtf.wtf/w/wtfpl/#version-3-1 for more details.


################################################################