#!/usr/bin/env python
# coding: utf-8

# In[5]:


from bs4 import BeautifulSoup
import requests
import os
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd 
import time
import json

# browser
def browser(): 
    #Mac Users
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    return Browser('chrome', **executable_path, headless=False)

#dictionary for all the data
mars_info = {}

# NEWS
def scrape_news():
    try: 
        # Initialize browser 
        browser = init_browser()

        url = "https://mars.nasa.gov/news/
        browser.visit(url)

        html = browser.html
        soup = BeautifulSoup(html, "html.parser")

        #  news title and news_paragraph
        title = soup.find('div', class_='content_title').find('a').text
        paragraph = soup.find('div', class_='article_teaser_body').text

        # add to dictionary 
        mars_info['news_title'] = title
        mars_info['news_paragraph'] = paragraph

        return mars_info

    finally:

        browser.quit()

# IMAGEs
def scrape_images():

    try: 

        # Initialize browser 
        browser = init_browser()

        # splinter module
        image_url = 'https://spaceimages-mars.com/'
        browser.visit(image_url)

        html_image = browser.html
        soup = BeautifulSoup(html_image, 'html.parser')

        rel_image_path = soup.find_all('img',class_='headerimage fade-in')[0]["src"]
    
        feat_image_url = img_url + rel_image_path

        # Dictionary IMAGE
        mars_info['feat_image_url'] = featured_image_url
        
        return mars_info
    finally:

        browser.quit()

    
# Weather 
def scrape_facts():

    try: 

    # Initialize browser 
        browser = init_browser()

        # splinter module
        image_url = 'https://spaceimages-mars.com/'
        browser.visit(image_url)
        
        
        # Initialize browser 
        browser = init_browser()

            # FACTS
        facts_url = 'https://galaxyfacts-mars.com/'

        facts_table = pd.read_html(facts_url)

        df = facts_table[0]
        df.columns = ['Mars-Earth Comparison', 'Mars', 'Earth']
        df = df.drop(0)

        html_table = df.to_html(index=False)
        
        mars_info['html_table'] = html_table
         
    finally:

        browser.quit()

        
# HEMISPHERES
def scrape_hemispheres():

    try: 

        # Initialize browser 
        browser = init_browser()

        # Visit hemispheres website through splinter module 
        hemispheres_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
        browser.visit(hemispheres_url)
    
        hem_url = "https://marshemispheres.com/"
        browser.visit(hem_url)

        main_urls = soup.find_all('div', class_='item')

        hem_img_urls=[]

        for x in main_urls:
            title = x.find('h3').text
            url = x.find('a')['href']
            hem_img_url = hem_url + url

            browser.visit(hem_img_url)

            html = browser.html
            soup = BeautifulSoup(html, 'html.parser')

            hem_img_original = soup.find('div',class_='downloads')
            hem_img_url = hem_img_original.find('a')['href']
        
            img_data = dict({'title':title, 'img_url': hem_url + hem_img_url})
            hem_img_urls.append(img_data)
        
        # Return mars_data dictionary 
         mars_info['hem_img_urls'] = hem_img_url
        
    finally:

        browser.quit()

