from requests import get
from cv2 import imread
from wordcloud import WordCloud,random_color_func
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

Urls = {
    'sina': 'https://s.weibo.com/top/summary/',
    'zhihu': 'https://tophub.today/',
    'baidu': 'http://top.baidu.com/buzz?b=1&fr=topindex'
}


def grab_info(site,lists):
    url = Urls[site]
    header = {'User-Agent': str(UserAgent().random)}   #Use fake headers
    r = get(url, headers=header)

    soup = BeautifulSoup(r.content, 'lxml')
    parser = Parsers.get(site)
    parser(soup,lists['title'],lists['val'],lists['link'])

def wb_parse(soup: BeautifulSoup, titles,vals,links):
    pattern = soup.find_all('td', 'td-02')  #解析对应内容
    for s in pattern:
        key = s.find('a')
        val = s.find('span')
        links.append("https://s.weibo.com" + key.get('href'))
        key = key.text
        titles.append(key)
        vals.append(val.text if val else str(val))


def zh_parse(soup: BeautifulSoup,titles,vals,links):
    div = soup.find('div',id='node-6')
    table = div.find('div','cc-cd-cb-l nano-content')
    # print(table.text)
    items = table.find_all('a')
    for s in items:
        links.append(s.get('href'))
        key = s.find('span','t').text
        val = s.find('span', 'e').text
        if val[-3:] == '万热度':
            val = val[:-4] + 'w'
        titles.append(key)
        vals.append(val)
    

def bd_parse(soup:BeautifulSoup,titles,vals,links):
    tr = soup.find_all('tr')
    for s in tr:
        key = s.find('td', 'keyword')
        val = s.find('td', 'last')
        if (key):
            key = key.find('a', 'list-title')
            val=val.find('span').text
            links.append(key.get('href'))
            key = key.text
            titles.append(key)
            vals.append(val)


Parsers = {
    'sina': wb_parse,
    'zhihu': zh_parse,
    'baidu': bd_parse
}

def generat_img(freq):

    mask_image = imread(r".\img\heart1.jpg")
    try:
        mask_image.shape
    except Exception as e:
        print(e)
    # print(freq)

    wordcloud = WordCloud(font_path='simhei.ttf', background_color="#37414F",mask=mask_image, color_func=random_color_func).generate_from_frequencies(freq)

    wordcloud.to_file('./img/wordcloud.jpg')
    return True


if __name__ == "__main__":
    lists = dict()
    lists['title'] = []
    lists['val'] = []
    lists['link'] = []
    grab_info('sina', lists)
    # vals=list(map(int,lists['val']))
    vals = [int(x) if x.isdigit() else 1 for x in lists['val']]
    print(vals)
    freq=dict(zip(lists['title'],vals))
    generat_img(freq)