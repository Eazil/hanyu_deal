# -*- coding:utf-8 -*-
#
import re
import codecs
import os
import xlrd

def kb_line(kb_l):
    if "Volume" in kb_l:
        return re.search('.*?Volume [^ ]+',kb_l)[0]
    elif "Lesson" in kb_l:
        return re.search('.*?Lesson [^ ]+', kb_l)[0]
    elif "Unit" in kb_l:
        return re.search('.*?Unit [^ ]+', kb_l)[0]
    else:
        return kb_l

data = xlrd.open_workbook('课本等级标注-0413.xlsx')
kb = data.sheets()[0]             #通过索引顺序获取
kb = data.sheet_by_index(0)       #通过索引顺序获取
kb = data.sheet_by_name(u'Sheet1') #通过名称获取
nrow= kb.nrows
#
kb_level_dict = {}
level_change = {'E1':1,'E2':2,'I1':3,'I2':4,'AD':5}
for i in range(1,nrow):
    kb_name = kb.cell(i, 0).value
    kb_level = level_change.get(kb.cell(i, 1).value)
    kb_level_dict[kb_name.strip()]=kb_level

file1 = codecs.open('语法结构形式难度等级汇总-0331.txt','r',"utf-8")
yfjg_txt = file1.read()
file1.close()


yf_level = {}
yfAndLevle = re.findall('.*?\|.*?\|(.*?)\|.*?\|.*?\|(.)\r\n',yfjg_txt,re.S)
for yANdL in yfAndLevle:

    if ' ' in yANdL[0]:
        key = yANdL[0].split(' ')[0]

    else:
        key = yANdL[0]
    yf_level[key]=int(yANdL[1])

file = codecs.open('hanyu-output-ID-0403.txt','r',"utf-8")
hanyu = file.read()
file.close()
#
#
exist_dict = {}
s_list = re.findall('(.*?)\r\n',hanyu)
for line in s_list:
    list = line.strip('\r\n').split('|')
    number = list[0]
    # print(list[5])
    kb_s = kb_line(list[5])
    # print(kb_s)
    yfjg_list = re.findall(number+'\|.*?\|.*?\|(.*?)\|.*?\r\n',hanyu,re.S)

    if len(yfjg_list) > 1:
        if number in exist_dict:
            yfjgxs_l = exist_dict[number]
        else:
            max_l = 0
            # print(number)
            for yf in yfjg_list:
                # print(yf)
                max_l = max(yf_level[yf.strip()],max_l)
            yfjgxs_l = max_l
            exist_dict[number] = yfjgxs_l
    else:
        # print(number)
        yfjgxs_l = yf_level[yfjg_list[0].strip()]
    kb_l = kb_level_dict[kb_s]
    weight_l = round((kb_l+yfjgxs_l)*1.0/2,1)
    total = line+'|'+str(yfjgxs_l)+'|'+str(kb_l)+'|'+str(weight_l)+'\r\n'
    file1 = codecs.open("./hanyu_yfndjs.txt", "a", "utf-8")
    file1.write(total)
    file1.close()
    print(total)












