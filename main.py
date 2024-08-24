import requests
from tkinter import Tk, Button, Label
from pprint import pprint
from bs4 import BeautifulSoup

request = requests.get('https://rp5.ru/Погода_в_России').text

soup = BeautifulSoup(request, 'lxml')

links = {}

block = soup.find_all('div', {'class': 'RuLinks'})

# window = Tk()
# window.title("weather")
#

for i in block:
    if i.find_next('b'):
        i = i.find_next('a')
        links[i.get_text()] = 'https://rp5.ru' + i['href']
        pprint(links)


for i, (name, link) in list(links.items()):
    
