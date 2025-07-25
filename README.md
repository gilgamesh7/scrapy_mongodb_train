# scrapy_mongodb_train
Web Scraping With Scrapy and MongoDB from RealPython

# Links
- [Web Scraping With Scrapy and MongoDB](https://realpython.com/web-scraping-with-scrapy-and-mongodb/?utm_source=notification_summary&utm_medium=email&utm_campaign=2024-08-29)
- [Source code from RealPython](https://github.com/realpython/materials/tree/master/web-scraping-with-scrapy-and-mongodb/)
- [Books to Scrape - Website for this exercise](https://books.toscrape.com)
- [Inspect the Site Using Developer Tools](https://realpython.com/beautiful-soup-web-scraper-python/#inspect-the-site-using-developer-tools)
- [Install MongoDB on MacOS](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-os-x/)

# Initialise uv environment
- uv init .
- uv venv
- uv add scrapy
- uv add pymongo

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

# MongoDB Commands
- Get version : mongod --version
- Start service : 
    - brew services start mongodb-community@8.0
    - mongod --config /opt/homebrew/etc/mongod.conf
- Start shell : mongosh
- Some commands
``` test> use books_db
switched to db books_db
books_db> db.createCollection("books")
{ ok: 1 }
books_db> show collections
books
books_db>
```