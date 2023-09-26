import time
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import pandas as pd

from selenium.webdriver import ActionChains
from decouple import config

from selenium_stealth import stealth
from selenium.webdriver.chrome.options import Options
import re

import threading

chrome_options = Options()
chrome_options.add_argument("--headless")  # 啟用無界面模
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("--no-sandbox")
# import sasa_done

# driver = webdriver.Chrome() 
driver = webdriver.Chrome(options=chrome_options)

stealth(driver,
        languages=["zh-HK"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )

# product_detail_List = sasa_done.product_detail_link
categories = ['Shampoo', 'Body wash', '洗面奶', 'GEL', 'Cream', 'Conditioner', '漱口水', '牙膏', 'Hand wash', '姨媽巾']
categories_index = 0
# categorys = next(categories)

with open(r'C:\Users\user\Desktop\JDE7\mid-term\urls.txt','r') as file:
    categorysList = file.readlines()
with open(r'C:\Users\user\Desktop\JDE7\product_detail_list.txt','r') as product_detail_txt:
    product_detail_List = product_detail_txt.readlines()

xpath = "//li[@class='column-grid-container__column']"
product_list = driver.find_elements(By.XPATH, xpath)

review =[]
stars = []

# # LOOP URL
# for i, categoryUrl in enumerate(categorysList):
#     categoryUrl = categoryUrl.strip() 
#     driver.get(categoryUrl)
#     time.sleep(3)

for  product_detail_url in product_detail_List:
    if not re.match('http', product_detail_url):
        if review and stars:
            df = pd.DataFrame({'review': review, 'stars': stars})
            filename = f'reviewRating_{categories[categories_index]}.csv'
            df.to_csv(filename, index=False)
            print(f'{filename} exported')
            categories_index += 1
            review = []
            stars = []
            time.sleep(2)
            if categories_index >= len(categories):
                break
        continue

    driver.get(product_detail_url)
    time.sleep(3)
    
    try:
        review.append(driver.find_element(By.XPATH, ".//div[@class = 'star-rate-summary-content']/a").text)
    except:
        review.append('N/A')

    try:
        stars.append(driver.find_element(By.XPATH, ".//div[@class = 'star-rate-summary-content']/span").text.replace(' ', '').replace('(', ''))
    except:
        stars.append('N/A')

# df = pd.DataFrame({'review':review , 'stars':stars})

print(df)

# print(driver.find_element(By.XPATH , ".//div[@class = 'star-rate-summary-content']/a").text)
driver.close()

if review and stars and categories_index < len(categories):
    filename = f'reviewRating_{categories[categories_index]}.csv'
    df = pd.DataFrame({'review': review, 'stars': stars})
    df.to_csv(f'{filename}', index=False)
    print(f'{filename} exported')
# df.to_csv(f'{categorys[i]}_{i}.csv', index=False)

# df = pd.DataFrame({'review':review , 'stars':stars})
#     df.to_csv(f'reviewStarsOutput_{categorys}.csv', index=False)