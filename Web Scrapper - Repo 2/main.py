#!/usr/bin/env python3

import requests 
from bs4 import BeautifulSoup

def main():
    
    headers = {"User-Agent": "Mozilla/5.0"}
    url = "https://quotes.toscrape.com"
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("Failed to retrieve page.")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = soup.find_all('div', class_='quote')

    for quote in quotes:
        text = quote.find('span', class_='text').text
        author = quote.find('small',class_='author').text
        tags = []
        for tag  in quote.find_all('a', class_='tag'):
            tags.append(tag.text)
        print(text, '\n-', author)
        print('Tags:', ', '.join(tags), '\n')

if __name__=="__main__":
    main()

# py -m pipenv run python main.py