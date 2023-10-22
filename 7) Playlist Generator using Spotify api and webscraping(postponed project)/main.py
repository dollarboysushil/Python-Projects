from bs4 import BeautifulSoup
import requests


response = requests.get("https://www.billboard.com/charts/hot-100/")
response = response.text


soup = BeautifulSoup(response, "html.parser")


h3_tags = soup.find_all('h3', id="title-of-a-story")

for tags in h3_tags:

    print(h3_tags.text())
