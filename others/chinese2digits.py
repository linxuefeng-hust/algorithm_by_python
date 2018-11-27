
#-*- coding: cp936 -*-
'''

import re
import string
common_used_numerals_tmp ={'��':0, 'һ':1, '��':2, '��':2, '��':3, '��':4, '��':5, '��':6, '��':7, '��':8, '��':9, 'ʮ':10, '��':100, 'ǧ':1000, '��':10000, '��':100000000}
common_used_numerals = {}
for key in common_used_numerals_tmp:
  common_used_numerals[key] = common_used_numerals_tmp[key]
def chinese2digits(uchars_chinese):
  total = 0
  r = 1              #��ʾ��λ����ʮ��ǧ...
  for i in range(len(uchars_chinese) - 1, -1, -1):
    val = common_used_numerals.get(uchars_chinese[i])
    if val >= 10 and i == 0:  #Ӧ�� ʮ�� ʮ�� ʮ*֮��
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

print(chinese2digits('������ʮ������ǧ������ʮһ')) # �����ӡ���������ԭ������û�д���á��������λ�Ժ���ֽ�
print( "-------------------------")
print(chinese2digits('ʮ��'))
print ("-------------------------")
print (chinese2digits('һ������������ٶ�ʮ��'))

'''
##############################################################


CN_NUM = {

    '��': 0, 'һ': 1, '��': 2, '��': 3, '��': 4, '��': 5, '��': 6, '��': 7, '��': 8, '��': 9, '��': 0,

    'Ҽ': 1, '��': 2, '��': 3, '��': 4, '��': 5, '½': 6, '��': 7, '��': 8, '��': 9, '�@': 2, '��': 2,

}

CN_UNIT = {

    'ʮ': 10,

    'ʰ': 10,

    '��': 100,

    '��': 100,

    'ǧ': 1000,

    'Ǫ': 1000,

    '��': 10000,

    '�f': 10000,

    '��': 100000000,

    '�|': 100000000,

    '��': 1000000000000,

}


def chinese_to_arabic(cn):#def chinese_to_arabic(cn:str):-> int:

    unit = 0  # current

    ldig = []  # digest

    for cndig in reversed(cn):

        if cndig in CN_UNIT:

            unit = CN_UNIT.get(cndig)

            if unit == 10000 or unit == 100000000: #�����򡯻��ڡ���ջ
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


print(chinese_to_arabic('������ʮ������������ʮһ'))

print("-------------------------")

print(chinese_to_arabic('ʮ��'))

print("-------------------------")

print(chinese_to_arabic('һ����һ'))
