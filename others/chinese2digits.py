
#-*- coding: cp936 -*-
'''

import re
import string
common_used_numerals_tmp ={'零':0, '一':1, '二':2, '两':2, '三':3, '四':4, '五':5, '六':6, '七':7, '八':8, '九':9, '十':10, '百':100, '千':1000, '万':10000, '亿':100000000}
common_used_numerals = {}
for key in common_used_numerals_tmp:
  common_used_numerals[key] = common_used_numerals_tmp[key]
def chinese2digits(uchars_chinese):
  total = 0
  r = 1              #表示单位：个十百千...
  for i in range(len(uchars_chinese) - 1, -1, -1):
    val = common_used_numerals.get(uchars_chinese[i])
    if val >= 10 and i == 0:  #应对 十三 十四 十*之类
      if val > r:
        r = val
        total = total + val
      else:
        r = r * val
        #total =total + r * x
    elif val >= 10:
      if val > r:
        r = val
      else:
        r = r * val
    else:
      total = total + r * val
  return total

print(chinese2digits('三百四十五万两千六百七十一')) # 这个打印出来会出错，原因在于没有处理好’万‘这个单位以后的字节
print( "-------------------------")
print(chinese2digits('十二'))
print ("-------------------------")
print (chinese2digits('一亿零八万零三百二十三'))

'''
##############################################################


CN_NUM = {

    '〇': 0, '一': 1, '二': 2, '三': 3, '四': 4, '五': 5, '六': 6, '七': 7, '八': 8, '九': 9, '零': 0,

    '壹': 1, '贰': 2, '叁': 3, '肆': 4, '伍': 5, '陆': 6, '柒': 7, '捌': 8, '玖': 9, '貮': 2, '两': 2,

}

CN_UNIT = {

    '十': 10,

    '拾': 10,

    '百': 100,

    '佰': 100,

    '千': 1000,

    '仟': 1000,

    '万': 10000,

    '萬': 10000,

    '亿': 100000000,

    '億': 100000000,

    '兆': 1000000000000,

}


def chinese_to_arabic(cn):#def chinese_to_arabic(cn:str):-> int:

    unit = 0  # current

    ldig = []  # digest

    for cndig in reversed(cn):

        if cndig in CN_UNIT:

            unit = CN_UNIT.get(cndig)

            if unit == 10000 or unit == 100000000: #将‘万’或’亿‘入栈
                ldig.append(unit)

                unit = 1

        else:

            dig = CN_NUM.get(cndig)

            if unit:
                dig *= unit

                unit = 0

            ldig.append(dig)

    if unit == 10:
        ldig.append(10)

    val, tmp = 0, 0

    for x in reversed(ldig):

        if x == 10000 or x == 100000000:

            val += tmp * x

            tmp = 0

        else:

            tmp += x

    val += tmp

    return val


print(chinese_to_arabic('三百四十五万零六百七十一'))

print("-------------------------")

print(chinese_to_arabic('十八'))

print("-------------------------")

print(chinese_to_arabic('一亿零一'))
