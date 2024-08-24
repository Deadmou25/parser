import requests
from pprint import pprint
from bs4 import BeautifulSoup


class Weather:
    def __init__(self, link="https://rp5.ru/Погода_в_России"):
        self.link=link
        self.r = requests.get(self.link).text
        self.soup = BeautifulSoup(self.r, "lxml")
        self.main_block_tag = {}

    def get_main_block_tag(self):
        return self.soup.find_all('div', {'class': 'RuLinks'})

    def return_home_page(self):
        self.add_link_in_dict()

    def add_link_in_dict(self):
        all_links = self.get_main_block_tag()
        for link in all_links:
            if link.find_next('b'):
                link = link.find_next('a')
                self.main_block_tag[link.get_text()] = 'https://rp5.ru' + link['href']
    
    def parse_next(self, link):
        soup=Weather(link).soup
        if soup.find('div', {'id': 'archiveString'}):
            data = soup.find('div', {'id': 'archiveString'})
            temp = data.find_next('span', {'class': 't_0'}).get_text()
            return temp
        else:
            data = soup.find('div', {'class', 'countryMap'})
            data = data.find_all("a")
            links = {}

        for tag in data:
            links[tag.get_text()] = "https://rp5.ru" + tag['href']
        return links


if __name__ == "__main__":
    weather = Weather()
    weather.add_link_in_dict()
    print(weather.parse_next('https://rp5.ru/Погода_в_Нижнем_Новгороде'))
