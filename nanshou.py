# -*- coding:utf-8 -*-
#
import re
import codecs
import os

#
# file = codecs.open("./hanyu_output_dp.txt", "r", "utf-8")
# string = file.read()
# file.close()
# # print(string)
# #
# juzi = re.findall('.*?\r\n\r\n',string,re.S)
#
# # #
# n = 1
# for x in juzi:
#     number = str(n).zfill(5)
#     s = 'S'+number+'\r\n'+x
#     print(s)
#     file1 = codecs.open("./hanyu_output_dp_id.txt", "a", "utf-8")
#     file1.write(s)
#     file1.close()
#     n +=1
# s = juzi[0]
# # file1 = codecs.open("./hanyu_qChong.txt", "a", "utf-8")
# # file1.write(s)
# # file1.close()
# number = 0
# for i in juzi:
#     if i != s:
#         file1 = codecs.open("./hanyu_qChong.txt", "a", "utf-8")
#         file1.write(s+'|'+str(number)+'\r\n')
#         file1.close()
#         print(s)
#         number = 1
#         s=i
#     else:
#         number += 1
# #
# file = codecs.open("./hanyu_qChong.txt", "r", "utf-8")
# string = file.read()
# file.close()
#
# file1 = codecs.open("./hanyu_number.txt", "r", "utf-8")
# s = file1.read()
# file1.close()
#
# juzi1 = re.findall('(.*?\|.*?\|.*?)\|(.*?)\r\n',string)
#
# for i in juzi1:
#     s1 = i[0]
#     n1 = i[1]
#
#     sw = s1.replace('|', '\|')
#     sw = sw.replace('+', '\+')
#     sw = sw.replace('?', '\?')
#     sw = sw.replace('(', '\(')
#     sw = sw.replace(')', '\)')
#     # print(sw)
#     juzi2 = re.findall(sw + '\|(.*?)\|(.*?)\r\n', s)
#     if len(juzi2) == 0:
#         file1 = codecs.open("./hanyu_false_1.txt", "a", "utf-8")
#         file1.write(s1+'\r\n')
#         file1.close()
#         continue
#     url = juzi2[0][0]
#     n2 = juzi2[0][1]
#     if n1 == n2:
#         continue
#     else:
#         to=s1+'|'+url+'|'+n1+'|'+n2+'\r\n'
#         file1 = codecs.open("./hanyu_false_1.txt", "a", "utf-8")
#         file1.write(to)
#         file1.close()
#

# import pynlpir
#
# file1 = codecs.open("./汉语/hanyu_unique_output.txt", "r", "utf-8")
# s = file1.read()
# file1.close()
#
# list = re.findall('.*?\|(.*?)\n',s)
# pynlpir.open()
# # pynlpir.segment(s, pos_tagging=False)
#
# for line in list:
#     string = ''
#     s=pynlpir.segment(line,pos_tagging=False)
#     i = 1
#     for word in s:
#         if i == 1:
#             string += word
#             i += 1
#         else:
#             string+= ' '+word
#     string = string + '\r\n'
#     print(string)
#     file2 = codecs.open("./hanyu_ouput_fenci.txt", "a", "utf-8")
#     file2.write(string)
#     file2.close()
#
# pynlpir.close()

#计算标点句的个数sentence及标点句平均词数 word_v

# def panduan(word):
#     biaodian_list = ['，', '。', '；', '', '：', '？', '！', '——', '……']
#     for biaodian in biaodian_list:
#         if word == biaodian:
#             return True
#     return False
# year=str(2002)
# input="H:\\cws\\"+year+"_cws\\version_3_cws"
# # total=''
# for parents, folders, filenames in os.walk(input):
#     for filename in filenames:
#         file = os.path.join(input,filename)
#         # print(file)
#         file1 = codecs.open(file, "r", "utf-8")
#         s = file1.read()
#         file1.close()
#         word_list = s.split(' ')
#         biaodian_list = ['，','。','；','','：','？','！','——','……']
#         n = 0
#         for word in word_list:
#             if panduan(word):
#                 n+=1
#                 # print(word)
#         sentence = n
#         word_v = round((len(word_list) - sentence) / sentence,1)
#         total = file+"\r\n"+"CL-107-V3|"+str(sentence)+"\r\nCL-108-V3|"+str(word_v)+"\r\n\r\n"
#         file1 = codecs.open('./'+year+"_CL-107and108.txt", "a", "utf-8")
#         file1.write(total)
#         file1.close()
#
#

#给与新工具的中间文件id
file1 = codecs.open('./hanyu_unique_output.txt', "r", "utf-8")
s = file1.read()
file1.close()

file2= codecs.open('G:\code\汉语\hanyu_unique_output.txt.parsed.txt', "r", "utf-8")
s1 = file2.read()
file2.close()

s_list = s1.split('\r\n\r\n')

for i in range(1,len(s_list)):
    s2 = s_list[i]


    r = re.findall('(.*?)\t.*?\t.*?\t.*?', s2)
    string = ''
    for word in r:
        string += word
    # string = string.replace('(', '\(')
    # string = string.replace(')', '\)')
    # string = string.replace('.', '\.')
    # string = string.replace('?', '\?')
    if string in s:
        # number = re.search('(.*?)\|'+string,s)
        print(string)
        # print(number[1])
    else:
        print('False:'+s2)
