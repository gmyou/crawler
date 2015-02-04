# -*- coding:utf-8 -*-
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

f = open('../resource/KMug.html')
td  = f.read()

m = re.compile("<a[^>]*>([^<]+)</a>")
sbj = m.findall(str(td))
print str(unicode(sbj))
