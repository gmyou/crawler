# -*- coding: utf-8 -*-
import re

# string = '1,000,000원 10점'
# string = '1000000'
# string = '1000000원'
# string = '100만원'
# string = '삼성 노트북 NT450R5J-X85M (i5-4210u, 8기가램, ssd128, GT 820m) 팝니다. (액정 교체 제품) - 57만'

def getPrice(string, pattern):
    priceCheck = re.compile(pattern)
    if ( bool(priceCheck.search(string)) ):
        match = priceCheck.search(string)
        return match.group()

# string = '샘소나이트 서류가방 판매합니다. - 5 만원'
# pattern = r'[0-9]+.만'
# print getPrice(string, pattern)
