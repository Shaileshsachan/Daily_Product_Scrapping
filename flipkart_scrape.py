from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome(executable_path=r"chromedriver.exe")
products = []
prices = []
ratings = []
discounts = []

def get_content(query):
    search_query = query
    driver.get(f"https://www.flipkart.com/search?q={search_query}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=1&as-type=HISTORY&as-backfill=on")
    # driver.get("https://www.flipkart.com/search?q=nike&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
    content = driver.page_source
    return content

def funx(content):
    soup = BeautifulSoup(content, features='lxml')
    for a in soup.find_all('div', {'class': '_2kHMtA'}):
        name = a.find(class_ = '_4rR01T')
        price = (a.find(class_ ='_30jeq3 _1_WHN1')).get_text()[1:]
        rating = a.find(class_ = '_3LWZlK')
        discount = (a.find(class_ = '_3Ay6Sb'))
        if discount == None:
            pass
        else:
            discount = discount.get_text()
        products.append(name.text)
        prices.append(price)
        ratings.append(rating.text)
        discounts.append(discount)
    df = pd.DataFrame({'ProductName': products, 'Price':prices, 'Rating':ratings, 'Discount': discounts})
    df.to_csv('products3.csv', index=False, encoding='utf-8')



product_to_search = str(input("Enter a product name: "))
cont = get_content(product_to_search)
funx(cont)
