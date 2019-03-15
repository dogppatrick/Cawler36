# from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import warnings
import requests
import pandas as pd
warnings.filterwarnings("ignore")
page = 1
start_url = "https://www.ptt.cc/bbs/PC_Shopping/search?page=" + str(page) + "&q=%E8%8F%9C%E5%96%AE"
url = start_url
# r = Request(url)
# r.add_header("user-agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit"
#                            "/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36")
response = requests.get(url)
html = BeautifulSoup(response.text)
content = html.find("div", id="main-container")
articles = html.find_all("div", class_="r-ent")
print(articles[0])
