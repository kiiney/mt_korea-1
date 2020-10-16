import requests

url = 'http://apis.data.go.kr/1400000/service/cultureInfoService/mntInfoOpenAPI?serviceKey=cRhBhi3sxVClCIks%2FemvBBGZgcYv5HaKvFr26Ov5Q5nor0WtrgUNO9rwfYO6FkLUif9SefP0BK%2B18mBFvV8%2FCw%3D%3D&searchWrd=%EB%B6%81%ED%95%9C%EC%82%B0'

response = requests.get(url)
print(response.status_code)
print(response.text)

import bs4
from bs4 import BeautifulSoup

soup = BeautifulSoup(response.content, 'html.parser')
data = soup.find_all('item')

for item in data:
    mntiname = item.find('mntiname')
    mntiadd = item.find('mntiadd')
    mntidetails = item.find('mntidetails')
    print(mntiname.get_text(), mntiadd.get_text(), mntiname.get_text())


