import psycopg2
import csv
import glob
import re  
from datetime import datetime

# 連接PostgreSQL數據庫
connection = psycopg2.connect(
    user="postgres",
    password="inori",
    host="localhost",
    port="5432",
    database="sasa"
)

cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS sasa_product;")

create_table_query = """
CREATE TABLE sasa_product (
    id SERIAL PRIMARY KEY,
    category VARCHAR(255),
    restock VARCHAR(255),
    product_name VARCHAR(255),
    price VARCHAR(255),
    discount_price VARCHAR(255),
    url VARCHAR(1024),
    img VARCHAR(1024),
    reviews_count VARCHAR(255),
    stars VARCHAR(255),
    date DATE
);
"""

cursor.execute(create_table_query)
connection.commit()

# 指定包含CSV文件的文件夾路徑
folder_path = r"C:\Users\user\Desktop\JDE7"

# 循環遍歷每個CSV文件
for date_folder in glob.glob(f"{folder_path}/08??"):
    date_match = re.search(r'(\d{2})(\d{2})', date_folder[-4:])
    if date_match:
        date = f"2023-{date_match.group(1)}-{date_match.group(2)}"
        print(f"Processing date: {date}")
        for file_path in glob.glob(f"{date_folder}/*_merged*.csv"):
            category_match = re.search(
                r'(\d{4})(.*?)_merged', file_path.split('\\')[-1])
            category = category_match.group(2) if category_match else "Unknown"
            print(f"Processing category: {category}")
            print(f"Processing file: {file_path}")
            date_match = re.search(
                r'(\d{2})(\d{2})', file_path.split('\\')[-1])
            if date_match:
                date_str = f"2023-{date_match.group(1)}-{date_match.group(2)}"
                date = datetime.strptime(date_str, '%Y-%m-%d').date()
                print(date)  # Should print "2023-08-11"
                with open(file_path, 'r', encoding='utf-8-sig') as f:
                    reader = csv.reader(f)
                    next(reader)  # Skip header row
                    for row in reader:
                        # 打印正在處理的行
                        print(f"Processing row: {row}")
                        restock, product_name, price, discount_price, url, img, reviews, stars = row
                        # 將 "N/A" 替換為 None
                        restock = None if restock == 'N/A' else restock
                        price = None if price == 'N/A' else float(
                            price.replace('HK$', '').replace(',', ''))
                        discount_price = None if discount_price == 'N/A' else float(
                            discount_price.replace('HK$', '').replace(',', ''))
                        reviews = None if reviews == 'N/A' else int(
                            reviews.split(' ')[0])
                        reviews_count = None
                        if reviews != 'N/A' and reviews != 'None':
                            reviews_count = int(str(reviews).split(' ')[
                                                0].replace('None', '0'))
                        stars = None if stars == 'N/A' else float(stars)
                        # 打印準備插入的數據
                        print(
                            f"Prepared data: {category}, {restock}, {product_name}, {price}, {discount_price}, {url}, {img}, {reviews_count}, {stars}, {date}")
                        query = "INSERT INTO sasa_product (category, restock, product_name, price, discount_price, url, img, reviews_count, stars, date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
                        try:
                            cursor.execute(query, (category, restock, product_name, price,
                                            discount_price, url, img, reviews_count, stars, date))
                            connection.commit()  # 提交每個插入
                            # 打印插入成功的信息
                            print(f"Inserted data for {product_name}")
                        except Exception as e:
                            print(f"Error while inserting: {str(e)}")
                            print(f"Query: {query}")
                            print(f"Data: {row}")
                            connection.rollback()  # 如果有錯誤，回滾事務

connection.commit()
cursor.close()
connection.close()
