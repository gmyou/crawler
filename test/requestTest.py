#!/usr/bin/env python
# coding=utf-8

import requests

r = requests.get('https://www.ppomppu.co.kr/zboard/login_check.php', auth=('hanidrap', 'unicad10'))

print r.status_code
print r.headers['content-type']
print r.encoding
print r.text.encode('utf-8')
