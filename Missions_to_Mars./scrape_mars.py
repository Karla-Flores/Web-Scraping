# Import dependencies and set up
from bs4 import BeautifulSoup as bs
import pandas as pd
import requests
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
from pprint import pprint as pp

# Set Executable Path & Initialize Chrome Browser
def init_browser():
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

# NASA Mars News Site Web Scraper
def mars_news(browser):
    # Visit the NASA Mars News Site
    url = 'https://redplanetscience.com'
    browser.visit(url)

    # Get First title and paragraph
    browser.is_element_present_by_css("div.list_text", wait_time=0.5)
    
    html = browser.html
    news_soup = Beautifulsoup(html, "html.parser")

    try:
        element = news_soup.select_one("div.list_text")
        element.find("div", class_="content_title")
        
        title = element.find('div', class_='content_title').get_text()
        paragraph = element.find('div', class_='article_teaser_body').get_text()
    
    except AttributeError:
        return None, None

    return print(f'Title: {title}/n'), print(f'Paragraph: {paragraph}')
