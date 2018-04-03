# -*- coding:utf-8 -*-
#
import re
import codecs
import os
import pynlpir

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

# #给与新工具的中间文件id
# file1 = codecs.open('./hanyu_unique_output.txt', "r", "utf-8")
# s = file1.read()
# file1.close()
# s = s.replace(' ','')
#
# file2= codecs.open('G:\code\汉语\hanyu_unique_output.txt.parsed.txt', "r", "utf-8")
# s1 = file2.read()
# file2.close()
#
# s_list = s1.split('\r\n\r\n')
# n = ''
# x = ''
# for i in range(1,len(s_list)):
#     s2 = s_list[i]
#
#
#     r = re.findall('(.*?)\t.*?\t.*?\t.*?', s2)
#     string = ''
#     for word in r:
#         string += word
#     string = string.replace('(', '\(')
#     string = string.replace(')', '\)')
#     string = string.replace('.', '\.')
#     string = string.replace('?', '\?')
#     # if string in s:
#     number = re.search('(.*?)\|'+string+'\r\n',s)
#
#     # print(string)
#     if number==None:
#
#         ss = 'S'+str(int(n.strip('S'))+1).zfill(5)
#
#         if ss != x:
#             to = ss+'\r\n'+s2+'\r\n\r\n'
#             file1 = codecs.open('./hanyu_新工具.txt', "a", "utf-8")
#             file1.write(to)
#             file1.close()
#         else:
#             to= s2+'\r\n\r\n '
#             file1 = codecs.open('./hanyu_新工具.txt', "a", "utf-8")
#             file1.write(to)
#             file1.close()
#         x = ss
#
#         # if n != x:
#         #     print(string)
#         #     print('False:'+n)
#         # x = n
#
#     else:
#         n = number[1]
#
#     # else:
#     #     print('False:'+string)

# #提取niuparser子句
# file1 = codecs.open('./hanyu_新工具.txt', "r", "utf-8")
# s = file1.read()
# file1.close()
#
# list = re.findall("(S\d{5}\r\n)",s)
# print(len(list))
# file1 = codecs.open('./hanyu_output_dp_id.txt', "r", "utf-8")
# s1 = file1.read()
# file1.close()
# # for i in list:
# #     x = re.search(i+'.*?\r\n\r\n',s1,re.S)
# #     print(x[0])
# #     file1 = codecs.open('./hanyu_dp.txt', "a", "utf-8")
# #     file1.write(x[0])
# #     file1.close()

#汉语句子提取id及相应句子的去重
# file1 = codecs.open('./(新)hanyu_output(加句子ID).txt', "r", "utf-8")
# s = file1.read()
# file1.close()
#
# for i in range(1,39960):
#     number = 'S'+str(i).zfill(5)
#     string = re.search(number+'\|.*?\|.*?\|.*?\|(.*?)\|.*?\r\n',s)
#     total = number+'|'+string[1]+'\r\n'
#     print(total)
#     file1 = codecs.open('./(新)hanyu_output_qchong(加句子ID).txt', "a", "utf-8")
#     file1.write(total)
#     file1.close()


#对去重的句子进行分词
# file1 = codecs.open("./汉语/(新)hanyu_output_qchong(加句子ID).txt", "r", "utf-8")
# s = file1.read()
# file1.close()
#
#
# list = re.findall('.*?\|(.*?)\r\n',s)
# # print(len(list))
# pynlpir.open()
# pynlpir.segment(s, pos_tagging=False)
# n = 1
#
# for line in list:
#     number = 'S'+str(n).zfill(5)
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
#     file2 = codecs.open("./汉语/(新)hanyu_output_cws.txt", "a", "utf-8")
#     file2.write(string)
#     file2.close()
#     total = number + '|'+string
#     print(total)
#     file3 = codecs.open("./汉语/(新)hanyu_output_cws(加句子id).txt", "a", "utf-8")
#     file3.write(total)
#     file3.close()
#     n+=1
# pynlpir.close()

#给dp句子加上id
#
# file = codecs.open("./(新)hanyu_output_dp.txt", "r", "utf-8")
# string = file.read()
# file.close()
# # print(string)
# #
# juzi = re.findall('.*?\r\n\r\n',string,re.S)
#
# #
# # #
# n = 1
# for x in juzi:
#     number = str(n).zfill(5)
#     s = 'S'+number+'\r\n'+x
#     print(s)
#     file1 = codecs.open("(新)hanyu_output_dp_id.txt", "a", "utf-8")
#     file1.write(s)
#     file1.close()
#     n +=1

#给cp句子加上id
#
# file = codecs.open("./(新)hanyu_output_cp.txt", "r", "utf-8")
# string = file.read()
# file.close()
# # print(string)
# #
# juzi = re.findall('.*?\r\n',string,re.S)
# # print(len(juzi))
# # #
# # # #
# n = 1
# for x in juzi:
#     number = str(n).zfill(5)
#     s = 'S'+number+'\r\n'+x
#     print(s)
#     file1 = codecs.open("(新)hanyu_output_cp_id.txt", "a", "utf-8")
#     file1.write(s)
#     file1.close()
#     n +=1

#句子依存距离总和yc_total和依存距离平均值yc_v
def ycjl(string):
    number_list = re.findall('(\d*)\t.*?\t.*?\t(.*?)\t.*?\r\n',string)
    word_n = len(number_list)
    yc_total = 0
    yc_v = 0
    for n_list in number_list:
        distance = 0
        if n_list[1] != '-1':
            local = int(n_list[0])
            point = int(n_list[1])
            # print(local)
            distance = abs(point - local + 1)
            # print(distance)
            yc_total += distance
    yc_v = round(yc_total / word_n,1)
    # print(yc_v)
    return [yc_total,yc_v]


file = codecs.open("./(新)hanyu_output_dp_id.txt", "r", "utf-8")
string = file.read()
file.close()

for i in range(1,39960):
    number = 'S' + str(i).zfill(5)
    s_list = re.search(number+'\r\n(.*?\r\n)\r\n',string,re.S)
    input = s_list[1]
    list = ycjl(input)

