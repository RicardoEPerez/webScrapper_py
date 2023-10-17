import re
from bs4 import BeautifulSoup
from colorama import Fore
import requests

website = 'http://futanarifreak.blogspot.com'

resultado = requests.get(website)
content = resultado.text

soup = BeautifulSoup(content,'lxml')
box = soup.find_all('div', class_='post-body entry-content')

with open(f'{website}.txt', 'w') as file:
    file.write(str(box))