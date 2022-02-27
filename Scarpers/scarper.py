import requests
from bs4 import BeautifulSoup


def DollarParse():
    url = 'https://www.banki.ru/products/currency/usd/'
    headers = {'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'}

    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')

    usd = soup.find('div', class_='currency-table__large-text').text
    return usd


def EuroParse():
    url = 'https://www.banki.ru/products/currency/eur/'
    headers = {'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'}

    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')

    eur = soup.find('div', class_='currency-table__large-text').text
    return eur


first_file = open('DollarPrices.txt', 'w')
second_file = open('EuroPrices.txt', 'w')
first_file.write(DollarParse() + '\n')
second_file.write(EuroParse() + '\n')
