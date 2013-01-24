=============================
Human Atrocities Project
=============================

These are assorted files and scripts connected with the Human Atrocities 
Project. 

- rss_scrape.py : Foundation for the scraping of news stories to code for human
  atrocities.
- page_scrapes.py : Set of functions to scrape various news websites. Called by
  rss_scrape.py. 
- mongo_connection.py : Function to add data to the mongoDB collection. Called
  by rss_scrape.py.
- geonames_api.py : Functions to hook into the geonames API. Will be used in the
  future to aid in the automated coding of news stories. 
