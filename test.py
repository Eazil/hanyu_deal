# -*- coding:utf-8 -*-

import re
import time
from selenium import webdriver
import codecs

browser = webdriver.Chrome()
browser.get('http://www.aihanyu.org/syntax.aspx')
yfjg = ['固定结构','介词及介词结构','特殊句式','复句']
for f in range(1,5):
    button = browser.find_element_by_css_selector('input#ctl00_MainContent_Button'+str(f))
    button.click()
    for d in range(1,3):
        yf = browser.find_elements_by_css_selector('div#ctl00_MainContent_Panel'+str(d)+' div a')
        for i in yf:
            url = i.get_attribute('href')
            yuFaDian = i.text
            driver = webdriver.Chrome()
            driver.get(url)
            click_one = driver.find_elements_by_css_selector('span.underline')
            # print(click_one.text)
            bianbie = False
            lengh = 0
            if len(click_one)>=2 and click_one[1].text == '形式类别（点击）':
                click_one[1].click()
                time.sleep(3)
                yufaJG_1=driver.find_element_by_id('2')
                yufaJG_2 = yufaJG_1.find_elements_by_css_selector('a')
                lengh = len(yufaJG_2)
                bianbie = True
                # for k in yufaJG_2:
                #     yufajg = k.text
                #     total = yfjg[f - 1] + '|' + yuFaDian + '|' + yufajg + '|' + url+'\r\n'
                #     print(total)
                #     file = codecs.open("./hanyu_c.txt", "a", "utf-8")
                #     file.write(total)
                #     file.close()
            else:
                click_two = driver.find_elements_by_css_selector('div#ctl00_MainContent_Panel1 a')[2]
                if click_two.text == '语义信息':
                    click_two.click()
                    time.sleep(3)
                    yufaJG_1 = driver.find_element_by_id('2')
                    yufaJG_2 = yufaJG_1.find_elements_by_css_selector('a')
                    lengh = len(yufaJG_2)
                    # for k in yufaJG_2:
                    #     yufajg = k.text
                    #     total = yfjg[f-1]+'|'+yuFaDian+'|'+yufajg+'|'+url+'\r\n'
                    #     print(total)
                    #     file = codecs.open("./hanyu_c.txt", "a", "utf-8")
                    #     file.write(total)
                    #     file.close()
            total = ''
            for l in range(0,lengh):
                yufaJG_1 = driver.find_element_by_id('2')
                yufaJG_2 = yufaJG_1.find_elements_by_css_selector('a')
                yufajg = yufaJG_2[l].text
                yufaJG_2[l].click()
                record = driver.find_element_by_id('ctl00_MainContent_lbRecord')
                record_n = record.text
                total = yfjg[f-1]+'|'+yuFaDian+'|'+yufajg+'|'+url+'|'+record_n+'\r\n'
                if bianbie:
                    click_one = driver.find_elements_by_css_selector('span.underline')
                    click_one[1].click()
                    time.sleep(3)
                else:
                    click_two = driver.find_elements_by_css_selector('div#ctl00_MainContent_Panel1 a')[2]
                    click_two.click()
                    time.sleep(3)
                file = codecs.open("./hanyu_number.txt", "a", "utf-8")
                print(total)
                file.write(total)
                file.close()


            driver.close()


browser.close()