# -*- coding:utf-8 -*-
import re

td = '">무선 키보드 (애플 정품, 새것)</a>'

m = re.compile(ur"\p{Hangul}")
sbj = m.findall(str(td))

print sbj