def sasa_done():
    import time
    from selenium import webdriver

    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.options import Options

    import pandas as pd

    from selenium.webdriver import ActionChains
    from decouple import config

    from datetime import datetime
    from bs4 import BeautifulSoup as soup
    from lxml import html

    from selenium_stealth import stealth
    from selenium.webdriver.chrome.options import Options

    # from database import connect, insertDf , create_table
    # set chrome
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument("--no-sandbox")

    
    driver = webdriver.Chrome(options=chrome_options)
    #driver = webdriver.Chrome()

    stealth(driver,
        languages=["zh-HK"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )



    # READ URL 
    with open(r'C:\Users\user\Desktop\JDE7\mid-term\urls.txt','r') as file:
        urls = file.readlines()

    # hdr = {'User-Agent': 'Mozilla/5.0', 'Accept': 'text/html, application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
    categorys = ['Shampoo', 'Body wash', '洗面奶', 'GEL', 'Cream', 'Conditioner', '漱口水', '牙膏', 'Hand wash', '姨媽巾']

    # LOOP URL
    for i, url in enumerate(urls):
        url = url.strip() 
        driver.get(url)
        time.sleep(4)
        
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        time.sleep(4)


        restock = []
        product_name = []
        price = []
        discount_price = []
        product_link = []
        img = []
        review =[]
        stars = []

        xpath = "//li[@class='column-grid-container__column']"
        product_list = driver.find_elements(By.XPATH, xpath)

        # wait = WebDriverWait(driver, 10)  # 最多等待10秒
        # elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, xpath)))

        for product in product_list:
            # print(product.text)
            # print('-'*30)
            try:
                restock.append(product.find_element(By.XPATH , ".//span[@class = 'sc-KLwla faHVMN']").text)
            except:
                restock.append('N/A')

            try:
                product_name.append(product.find_element(By.XPATH , ".//div[@class = 'sc-hELUyY fagHXO']").text)
            except:
                product_name.append('N/A')
            
            try:
                price.append(product.find_element(By.XPATH , ".//div[@class = 'sc-KzItE gfAAIo']").text)
            except:
                price.append('N/A')

            try:
                discount_price.append(product.find_element(By.XPATH , ".//div[@class = 'sc-gIeZgt hGDdRh']").text)
            except:
                discount_price.append('N/A')

            try:
                product_detail_link = product.find_element(By.XPATH ,".//a[@class = 'sc-hQlIKd jnYvQx product-card__vertical product-card__vertical--hover new-product-card']" ).get_attribute('href')
                product_link.append(product_detail_link)
            except:
                product_link.append('N/A')
            
            # for link in product_link:
                    

            try:
                img.append(product.find_element(By.XPATH , ".//img[@class = 'product-card__vertical__media product-card__vertical__media-tall' ]").get_attribute('src'))
            except:
                img.append('N/A')
            
            
            
            # try:
            #     req = urllib.request.Request(product_detail_link, headers=hdr)
            #     html_page = urllib.request.urlopen(req, timeout=10)
            #     html_soup = soup(html_page, "html.parser")
            #     # html_tree = html.fromstring(html_page.read())

            #     # # get review and rating
            #     # review_text = html_tree.xpath(".//div[@class = 'star-rate-summary-content']/a")[0].text
            #     # stars_text = html_tree.xpath(".//div[@class = 'star-rate-summary-content']/span")[0].text.replace(' ', '').replace('(', '')
            #     review_text = html_soup.find('div', class_ = 'star-rate-summary-content').find('a').get_text()
            #     stars_text = html_soup.find('div' , class_ = 'star-rate-summary-content').find('span').get_text().replace(' ', '').replace('(', '')

            #     review.append(review_text)
            #     stars.append(stars_text)

            # except Exception as e:
            #     review.append('N/A')
            #     stars.append('N/A')

            ## 用新分頁開啟product        -------------METHOD 1 要逐條逐條click on99-------------
            # product_detail_link = product.find_element(By.XPATH, ".//a[@class = 'sc-fzmOIZ iAAIZv product-card__vertical product-card__vertical--hover new-product-card']").get_attribute('href')
            # driver.execute_script(f"window.open('{product_detail_link}', '_blank');")
            # driver.switch_to.window(driver.window_handles[1])

            # # run try 
            # driver.implicitly_wait(5)
            # try:
            #     review.append(driver.find_element(By.XPATH, ".//div[@class = 'star-rate-summary-content']/a").text)
            # except:
            #     review.append('N/A')

            # try:
            #     stars.append(driver.find_element(By.XPATH, ".//div[@class = 'star-rate-summary-content']/span").text.replace(' ', '').replace('(', ''))
            # except:
            #     stars.append('N/A')

            # # close and切換回原始分頁
            # driver.close()
            # driver.switch_to.window(driver.window_handles[0])


        
        time.sleep(3)


    # print(len(restock))
    # print(len(product_name))
    # print(len(price))
    # print(len(discount_price))

        print(f'num_of_result : {len(product_list)}')
        print('DONE')

    # filled_data = zip_longest(restock, product_name, price, discount_price, fillvalue=None)
    # df = pd.DataFrame(filled_data, columns=['restock', 'product name', 'price', 'discount price'])
        df = pd.DataFrame({'restock': restock, 'product_name': product_name,
                            'price': price, 'discount_price': discount_price,
                            'URL':product_link , 'IMG':img})
                            # 'review': review, 'stars': stars})



        date = datetime.today().date()
        today = date.strftime("%m-%d")
        print(df)

        # for output in categorys:
        df.to_csv(f'{today}{categorys[i]}_{i}.csv', index=False)

        if i == 0:
            # 第一次執行時使用 'w+' 模式，清空檔案內容並寫入新的結果
            with open('product_detail_list.txt', 'w+') as ff:
                for link in product_link:
                    ff.write(link + '\n')
                    
        else:
            # 第二次及後續的執行使用 'a' 模式，附加結果到檔案末尾
            with open('product_detail_list.txt', 'a') as ff:
                for link in product_link:
                    ff.write(link + '\n')

        with open('product_detail_list.txt', 'a') as ff:
            ff.write('-'*30 + 'DONE' + '-'*30 + '\n')
    

    driver.close()

if __name__ == '__main__':
    sasa_done()
    # connection = connect()

    # create_table()

    # resp = insertDf(connection , df , 'sasa')

