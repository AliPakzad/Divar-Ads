from bs4 import BeautifulSoup

import requests

webpage = requests.get('https://divar.ir/s/tehran')

soup = BeautifulSoup(webpage.text, 'html.parser')

#<div class="kt-post-card__description">توافقی</div>

result = soup.find_all("div", class_="kt-post-card__body")


for i in result:
    descriptions = i.find_all("div", class_="kt-post-card__description")
    for description in descriptions:
        if description !=None and description.text == "توافقی":
            print(i.find("h2", class_ ="kt-post-card__title").text)
            print()
