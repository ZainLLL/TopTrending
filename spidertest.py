import jieba.posseg as pseg
import matplotlib.pyplot as plt
from os import path
import sys
import requests
from cv2 import imread,imshow
from wordcloud import WordCloud,random_color_func
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

wb_r = 'https://s.weibo.com/top/summary/' #weibo url
tw_r = 'https://twitter-trends.iamrohit.in/' #tweet url
zh_r = 'https://www.zhihu.com/billboard/'
bd_r = 'http://top.baidu.com/buzz?b=1&fr=topindex'
test_r='https://tophub.today/'
headers= {'User-Agent':str(UserAgent().random)}
# r = requests.get(zh_r,headers=headers)
r = requests.get(test_r,headers=headers)
# print(r.content)

print(r.status_code)
soup = BeautifulSoup(r.content, "lxml")
# print(soup.contents)
table = soup.find('div','cc-cd-cb-l nano-content')
# print(table.text)
items = table.find_all('a')

print(len(items))
for s in items:
    url = s.get('href')
    key = s.find('span','t').text
    val = s.find('span', 'e').text
    # print(url)
    # print(key,val)