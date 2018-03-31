# -*- coding:utf-8 -*-
#
import re
import codecs

#
file = codecs.open("./hanyu_output_dp.txt", "r", "utf-8")
string = file.read()
file.close()
# print(string)
#
juzi = re.findall('.*?\r\n\r\n',string,re.S)

# #
n = 1
for x in juzi:
    number = str(n).zfill(5)
    s = 'S'+number+'\r\n'+x
    print(s)
    file1 = codecs.open("./hanyu_output_dp_id.txt", "a", "utf-8")
    file1.write(s)
    file1.close()
    n +=1
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