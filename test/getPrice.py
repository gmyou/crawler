# -*- coding: utf-8 -*-

import re

string = '1,000,000원'
# string = '1000000'
# string = '1000000원'
# string = '100만원'
pattern = r'(\d+),?(\d+),?(\d+)(만)?원'
priceCheck = re.compile(pattern)

if ( bool(priceCheck.match(string)) ):
    match = priceCheck.search(string)
    print match.group()
