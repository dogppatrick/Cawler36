from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import warnings
import requests
import pandas as pd
import math
warnings.filterwarnings("ignore")


url = "https://www.ptt.cc/bbs/Gossiping/M.1552728565.A.639.html"
print(url)
response = requests.get(url, cookies={"over18": "1"})
html = BeautifulSoup(response.text)