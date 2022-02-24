from bs4 import BeautifulSoup
import requests

url = "https://www.solotodo.cl"

page = requests.get(url)

soup =  BeautifulSoup(page.content, "html.parser")
content_titles = soup.find_all("h3,category-browse-results,price flex-grow")

for tit in content_titles:
    sub= tit.find_all('a')
    print(sub[0].attrs.get('title'))