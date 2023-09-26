# SASA E-Commerce Data Crawler

## Project Overview
This project encompasses a suite of Python scripts developed to crawl and scrape valuable data from the SASA e-commerce website. Designed with market analysts and data scientists in mind, this tool automates the extraction of product details, customer reviews, and ratings. Data collected can be stored in a SQL database for further analysis, thereby providing a robust resource for competitive intelligence, market research, and customer sentiment analysis.

## Core Features

- **Automated Product Data Crawling**: Leverages Selenium to systematically collect product details like name, price, and description from the SASA platform.
- **Comprehensive User Feedback Scraper**: Scrapes user reviews and ratings to offer an in-depth understanding of customer opinions and product quality.
- **SQL Database Integration**: Features a built-in functionality for storing crawled data in a SQL database, enabling scalable and organized data storage.
- **Configurable Crawling Settings**: Customizable script parameters allow users to tailor the crawling process to specific analytical or business needs.

## Installation and Usage

### Pre-requisites

1. **Clone the Repository**: 
   ```bash
   git clone https://github.com/manhinreal/sasa-web-crawler.git
   ```

2. **Install Required Packages**: 
   ```bash
   cd sasa-web-crawler
   pip install -r requirements.txt
   ```

### Steps for Data Collection

1. **Prepare the URLs List**: 
    Before running the crawlers, add the URLs of the products you wish to scrape into a file named `urls.txt`. Each URL should be on a new line. This file serves as the input for the subsequent crawling tasks.

2. **Run Product Data Crawler**: 
   ```bash
   python sasa_scraper.py
   ```
   This script uses Selenium to navigate through the SASA website and scrape essential product details such as name, price, and description. A `.csv` file will be generated containing these details for each product URL listed in `urls.txt`.

3. **Scrape User Reviews and Ratings**: 
   ```bash
   python sasa_reviewRating_scraper.py
   ```
   This script focuses on extracting user reviews and product ratings. It navigates to each product page's review section and scrapes the content. The collected data is then stored in a separate `.csv` file.

4. **Finalize Data Storage**: 
   ```bash
   python connect_SQLdb.py
   ```
   This is the concluding step where all the scraped data gets inserted into a SQL database. Run this script only after successfully completing the previous data scraping steps. It uses pymysql to connect to the database and populate it with the scraped data.

## Contribution Guidelines

1. **Fork the Repository**: Start by forking this repository to make your own copy.
2. **Create a Feature Branch**: Work on your contributions in a separate branch.
3. **Adhere to Code Quality Standards**: Ensure your code complies with the project's coding standards.
4. **Test Thoroughly**: Before committing, test your changes rigorously.
5. **Submit a Pull Request**: Detail your changes and submit for review.

## Licensing and Contact

- **License**: MIT License. Refer to the [LICENSE.md](LICENSE.md) file for more details.
- **Contact Information**: For further inquiries or to report issues, contact JasonTSOI at email.
