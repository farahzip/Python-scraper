##To run code, type PYTHON APP.PY in terminal

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os

load_dotenv()

def scrape():
    url = os.getenv('URL')
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    ##Elements to print
    title = soup.select_one('h1').text
    text = soup.select_one('p')
    link = soup.select_one('a').get('href')

    print(f'Title: {title}')
    print(f'Text: {text}')
    print(f'Link: {link}')

if __name__ == '__main__':
    scrape()