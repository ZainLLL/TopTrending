import jieba.posseg as pseg
import matplotlib.pyplot as plt
from os import path
import sys
import requests
from cv2 import imread,imshow
from wordcloud import WordCloud,random_color_func
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

freq = dict()
urllist=list()

Urls = {
    'wb': 'https://s.weibo.com/top/summary/',
    'zh': 'https://tophub.today/',
    'bd': 'http://top.baidu.com/buzz?b=1&fr=topindex'
}



def grab_info(site,freq,urllist):
    url = Urls[site]
    header = {'User-Agent': str(UserAgent().random)}   #Use fake headers
    r = requests.get(url, headers=header)
    # print(r.status_code)
    # print(r.content.decode("utf-8"))

    soup = BeautifulSoup(r.content, 'lxml')
    parser = Parsers.get(site)
    parser(soup,freq,urllist)
    return urllist

def wb_parse(soup:BeautifulSoup,freq,urllist):
    pattern = soup.find_all('td', 'td-02')  #解析对应内容
    for s in pattern:
        key = s.find('a')
        val = s.find('span')
        urllist.append("https://s.weibo.com" + key.get('href'))
        key= key.text
        if val:
            freq[key] = int(val.text)
        else:
            freq[key] = 6000000
    # print(freq)
    # print(urllist)

def zh_parse(soup: BeautifulSoup, freq, urllist):
    div = soup.find('div',id='node-6')
    table = div.find('div','cc-cd-cb-l nano-content')
    # print(table.text)
    items = table.find_all('a')
    # print(len(items))
    for s in items:
        urllist.append(s.get('href'))
        key = s.find('span','t').text
        val = s.find('span', 'e').text
        val=val[:-4]+'w'
        freq[key]=val
    

def bd_parse(soup:BeautifulSoup,freq,urllist):
    tr = soup.find_all('tr')
    for s in tr:
        key = s.find('td', 'keyword')
        val = s.find('td', 'last')
        if (key):
            key = key.find('a', 'list-title')
            val=val.find('span').text
            urllist.append(key.get('href'))
            key = key.text
            freq[key] = val
    # print(freq)
    # print(len(urllist))


Parsers = {
    'wb': wb_parse,
    'zh': zh_parse,
    'bd': bd_parse
}

def generat_img(freq):
    #載入stopword
    # stop_words = set(line.strip() for line in open('stopwords.txt', encoding='utf-8'))
    # commentlist = comment_subjects
    # for subject in comment_subjects:
    #     if subject.isspace():continue
    #     # segment words line by line
    #     word_list = pseg.cut(subject)#分詞
    #     for word, flag in word_list:
    #         if not word in stop_words and flag == 'n':
    #             commentlist.append(word)
    
    mask_image = imread(r".\img\heart1.jpg")
    try:
        mask_image.shape
    except Exception as e:
        print(e)
    # print(freq)

    wordcloud = WordCloud(font_path='simhei.ttf', background_color="#37414F",mask=mask_image, color_func=random_color_func).generate_from_frequencies(freq)
    # Display the generated image:
    # plt.imshow(wordcloud)
    # plt.axis("off")
    wordcloud.to_file('./img/wordcloud.jpg')
    # plt.show()
    return True


if __name__ == "__main__":
    grab_info('zh',freq,urllist)
    # generat_img()