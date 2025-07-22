# scrapy_mongodb_train
Web Scraping With Scrapy and MongoDB from RealPython

# Links
- [Web Scraping With Scrapy and MongoDB](https://realpython.com/web-scraping-with-scrapy-and-mongodb/?utm_source=notification_summary&utm_medium=email&utm_campaign=2024-08-29)
- [Source code from RealPython](https://github.com/realpython/materials/tree/master/web-scraping-with-scrapy-and-mongodb/)
- [Books to Scrape - Website for this exercise](https://books.toscrape.com)
- [Inspect the Site Using Developer Tools](https://realpython.com/beautiful-soup-web-scraper-python/#inspect-the-site-using-developer-tools)

# Initialise uv environment
- uv init .
- uv venv
- uv add scrapy

# Scrapy commands
- help : scrapy
- Generate project scaffolding : scrapy startproject books
- Test using scrapy Shell
    - scrapy shell http://books.toscrape.com
    - response.status
    - response.url
- Generate spider : 
    - cd books
    - scrapy genspider book https://books.toscrape.com/
- Crawl :
    - scrapy crawl book

# Xpath & CSS used in this project 
- Title / URL : 
    - //*[@id="default"]/div/div/div/div/section/div[2]/ol/li[1]/article/h3/a
    - body > div > div > div > div > section > div:nth-child(2) > ol > li:nth-child(1) > article > h3 > a
- Price :
    - //*[@id="default"]/div/div/div/div/section/div[2]/ol/li[1]/article/div[2]/p[1]
    - body > div > div > div > div > section > div:nth-child(2) > ol > li:nth-child(1) > article > div.product_price > p.price_color