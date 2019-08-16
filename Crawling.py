import bs4
import urllib.request
import json
from collections import OrderedDict

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

url = "https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=cur&date=20190808"
html = urllib.request.urlopen(url)
bsObj = bs4.BeautifulSoup(html, "html.parser")
json_data = OrderedDict()
num = 1
listA = list()

ranking = bsObj.find("tbody")
ranking = bsObj.find_all("div", {"class":"tit5"})

# for movie_name in ranking:
    # print(movie_name.text)

for movie in ranking:
    listA.append(movie.text)

for movie in listA:
    json_data[num] = movie
    num += 1

print(json.dumps(json_data, ensure_ascii=False, indent="\t"))