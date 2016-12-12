# -*- coding: utf-8 -*-
import urllib

params = urllib.urlencode({'blogId': 'wonsukdream', 'logNo': 30132356702, 'categoryNo': 0})
f = urllib.urlopen("http://blog.naver.com/OpenMagazineViewer.nhn?%s" % params)
print f.read()

