import psycopg2
import requests
from bs4 import BeautifulSoup


# Create the dollar parser


def DollarParse():
    url = "https://ru.investing.com/currencies/usd-rub"
    headers = {'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_23 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'}

    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')

    usd = soup.find('span', class_='text-2xl').text
    return usd


# Connection with Data Base

con = psycopg2.connect(
    database="hacatondata",
    user="postgres",
    password="qwerty",
    host="127.0.0.1",
    port="5432"
)

# Checking for connection

print("Database opened successfully")
cur = con.cursor()
cur.execute("SELECT Наименование, Цена, ДатаПоставки FROM base")

# Creating a class containing information about each object


class Data:

    def __init__(self, name, deliveryDates, price, amount):
        self.name = name
        self.price = price
        self.deliveryDates = deliveryDates
        self.amount = amount

    def display_info(self):
        print(self)

    def __str__(self):
        return f"Name: {self.name} Price: {self.price} Delivery Dates: {self.deliveryDates} Amount: {self.amount}"

# Creating an SQL query


cur = con.cursor()
cur.execute("SELECT Наименование, ДатаПоставки, Цена, ОбъемЗаказа FROM base ORDER BY Наименование")
rows = cur.fetchall()


# Creating an array of structures specified in the class


data = []
for row in rows:
    data.append(Data(row[0], row[1], row[2], row[3]))


# Declaration of variables


averagePrice, yearTotalPrice = 0, 0
counter, counter_1, counter_2, counter_3, counter_4, counter_5, counter_6, counter_7, counter_8 = 0, 0, 0, 0, 0, 0, 0, 0, 0
dollarStat = [60.9579, 67.0349, 58.3529, 62.7091, 64.7362, 72.1464, 73.6541]
dollarActual = float(DollarParse().replace(',', '.'))


# Product Name Introduction


name = str(input("Enter the product name: "))


# Running through the database


for i in data:
    # Checking conditions
    if i.name == name:
        counter += 1
        if i.deliveryDates[:4] == "2015" or i.deliveryDates[6:10] == "2015":
            counter_1 += 1
            averagePrice += float(i.price.replace(',','.')) / dollarStat[0]
            yearTotalPrice += float(i.price.replace(',', '.')) / dollarStat[0] * float(i.amount)

        if i.deliveryDates[:4] == "2016" or i.deliveryDates[6:10] == "2016":
            counter_2 += 1
            averagePrice += float(i.price.replace(',','.')) / dollarStat[1]
            yearTotalPrice += float(i.price.replace(',', '.')) / dollarStat[1] * float(i.amount)

        if i.deliveryDates[:4] == "2017" or i.deliveryDates[6:10] == "2017":
            counter_3 += 1
            averagePrice += float(i.price.replace(',','.')) / dollarStat[2]
            yearTotalPrice += float(i.price.replace(',', '.')) / dollarStat[2] * float(i.amount)

        if i.deliveryDates[:4] == "2018" or i.deliveryDates[6:10] == "2018":
            counter_4 += 1
            averagePrice += float(i.price.replace(',','.')) / dollarStat[3]
            yearTotalPrice += float(i.price.replace(',', '.')) / dollarStat[3] * float(i.amount)

        if i.deliveryDates[:4] == "2019" or i.deliveryDates[6:10] == "2019":
            counter_5 += 1
            averagePrice += float(i.price.replace(',','.')) / dollarStat[4]
            yearTotalPrice += float(i.price.replace(',', '.')) / dollarStat[4] * float(i.amount)

        if i.deliveryDates[:4] == "2020" or i.deliveryDates[6:10] == "2020":
            counter_7 += 1
            averagePrice += float(i.price.replace(',','.')) / dollarStat[5]
            yearTotalPrice += float(i.price.replace(',', '.')) / dollarStat[5] * float(i.amount)

        if i.deliveryDates[:4] == "2021" or i.deliveryDates[6:10] == "2021":
            counter_8 += 1
            averagePrice += float(i.price.replace(',','.')) / dollarStat[6]
            yearTotalPrice += float(i.price.replace(',', '.')) / dollarStat[6] * float(i.amount)

        if i.deliveryDates[:4] == "2021" or i.deliveryDates[6:10] == "2021":
            counter_8 += 1
            averagePrice += float(i.price.replace(',','.')) / dollarActual
            yearTotalPrice += float(i.price.replace(',', '.')) / dollarActual * float(i.amount)


# Output


averagePrice /= counter
yearTotalPrice /= counter
print(f"Среднее значение цены одного продукта <{name}> за год равно <{averagePrice}$>")
print(f"Вероятное значение цены за данное количество продукта <{name}> за год равно <{yearTotalPrice + (yearTotalPrice * 0.15)}$>")



