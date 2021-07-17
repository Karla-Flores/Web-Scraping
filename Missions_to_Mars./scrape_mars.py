# Import dependencies and set up
from bs4 import BeautifulSoup
import pandas as pd
import requests
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
from pprint import pprint as pp

# Set Executable Path & Initialize Chrome Browser
def scrape():
    # Open browser to NASA Mars News Site
    url = 'https://redplanetscience.com'
    
    data_dict = {}

    # Seting up splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # Open url
    browser.visit(url)

    # HTML Object
    html = browser.html

    # Parse HTML with Beautiful Soup
    news_soup = BeautifulSoup(html, 'html.parser')

    # Retrieve the latest element that contains news title
    title = news_soup.select_one('div.list_text')
    title = title.find('div', class_='content_title').get_text()

    # Retrieve the latest element that contains news paragraph
    paragraph = news_soup.select_one('div.list_text')
    paragraph = paragraph.find('div', class_='article_teaser_body').get_text()
    
    # Print results
    print(f'News Title: {title}')
    print(f'News Paragraph: {paragraph}')
    
    article_dict = {'title': title, 'paragraph': paragraph}
    data_dict ['news'] = article_dict
    print(data_dict)

    # Visit Galaxy Facts site
    url = 'https://galaxyfacts-mars.com'
    browser.visit(url)

    # Set up soup to parse html
    html = browser.html
    soup = BeautifulSoup(html,'html.parser')

    # Using Pandas to scrape the table containing facts about the planet
    mars_fact = soup.find('table', class_ ='table table-striped')
    mars_fact = pd.read_html(str(mars_fact))[0]
    mars_fact_html = mars_fact.to_html()
    # Converting the data to a HTML table string

    data_dict['mars_fact_html'] = mars_fact_html


    # Loop for setting up a dictionary with the image url string and the hemisphere title to a list
m_images = []

# Visit Mars Hemispheres site
url = 'https://marshemispheres.com'
browser.visit(url)



for i in range(4):
    # Set up soup to parse html
    html = browser.html
    soup = BeautifulSoup(html,'html.parser')
    
    # Find Hemisphere name
    h_name = soup.find_all('h3')[i].text
    
    # Home splinter click the Hemisphere name button
    browser.links.find_by_partial_text(h_name).click()
    
    # Set up soup to parse html
    html = browser.html
    soup = BeautifulSoup(html,'html.parser')
    
    # Image address
    h_images = url + '/' + soup.find('li').a['href']
    
    # Append dictionary
    m_images.append({'title': h_name, 'img_url':h_images})
    
    # Print
    print(f'Hemispheres name: {h_name}')
    print(f'URL: {h_images}')
    print(f'------------------------------------------------------------------------------')
    
    # Back
    browser.back()

    return data_dict

