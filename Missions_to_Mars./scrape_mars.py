# Import dependencies and set up
from bs4 import BeautifulSoup
import pandas as pd
import requests
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
from pprint import pprint as pp

# Set Executable Path & Initialize Chrome Browser
def scrape():
    
    # Title and paragraph
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

    # Images
    ## Visit Space Images site
    url = 'https://spaceimages-mars.com/'
    browser.visit(url)

    # Set up soup to parse html
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # Home splinter click the 'Full Image' button
    f_image = browser.links.find_by_partial_text('FULL IMAGE').click()

    # Set up soup to parse html
    html = browser.html
    soup = BeautifulSoup(html,'html.parser')

    # Retrieving image
    featured_image_url = url + soup.find('img',class_='fancybox-image')['src']
    print(f"Featured Image URL: {featured_image_url}")

    data_dict ['image'] = featured_image_url

    # Table
    # Visit Galaxy Facts site
    url = 'https://galaxyfacts-mars.com'
    browser.visit(url)

    # Set up soup to parse html
    html = browser.html
    soup = BeautifulSoup(html,'html.parser')


    # Using Pandas to scrape the table containing facts about the planet
    mars_fact = soup.find('table', class_ ='table table-striped')
    mars_fact = pd.read_html(str(mars_fact))[0]
    mars_fact.rename(columns={0: 'Characteristics', 1: 'Facts'},errors='raise', inplace=True)
    mars_fact_html = mars_fact.to_html()

    # Converting the data to a HTML table string
    data_dict['mars_fact_html'] = mars_fact_html
    print(data_dict)


    # Images
    # Loop for setting up a dictionary with the image url string and the hemisphere title to a list
    m_images = []
    u_images = []
    
    try:
        # Visit Mars Hemispheres site
        url = 'https://marshemispheres.com/'
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
            h_images = url + soup.find('li').a['href']

            # Append dictionary
            m_images.append({'title': h_name, 'img_url':h_images})

            # Print
            print(f'Hemispheres name: {h_name}')
            print(f'URL: {h_images}')
            print(f'------------------------------------------------------------------------------')

            # Back
            browser.back()
            articles_dict = {'titles':'h_images', 'img_url':'h_images'}
        
        
    except:
        m_images.append({'titles': 'Hemispheres name: Cerberus Hemisphere Enhanced'},
        {'titles': 'Schiaparelli Hemisphere Enhanced'},
        {'titles': 'Syrtis Major Hemisphere Enhanced'},
        {'titles': 'Valles Marineris Hemisphere Enhanced'})

        # m_images.append({'titles': 'Hemispheres name: Cerberus Hemisphere Enhanced', 'img_url':'https://marshemispheres.com/images/full.jpg'},
        # {'titles': 'Schiaparelli Hemisphere Enhanced', 'img_url':'URL: https://marshemispheres.com/images/schiaparelli_enhanced-full.jpg'},
        # {'titles': 'Syrtis Major Hemisphere Enhanced', 'img_url':'https://marshemispheres.com/images/syrtis_major_enhanced-full.jpg'},
        # {'titles': 'Valles Marineris Hemisphere Enhanced', 'img_url':'https://marshemispheres.com/images/valles_marineris_enhanced-full.jpg'})

        u_images.append({'img_url':'https://marshemispheres.com/images/full.jpg'},
        {'img_url':'URL: https://marshemispheres.com/images/schiaparelli_enhanced-full.jpg'},
        {'img_url':'https://marshemispheres.com/images/syrtis_major_enhanced-full.jpg'},
        {'img_url':'https://marshemispheres.com/images/valles_marineris_enhanced-full.jpg'})


    print(m_images)
    print(u_images)

    data_dict['m_images'] = articles_dict
    return data_dict