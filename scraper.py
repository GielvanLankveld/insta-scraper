from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import os
import urllib.request
import uuid
import sys

GOOD_STRING = '\033[92m✔\033[0m'
BAD_STRING = '\033[92m❌\033[0m'

# driver = webdriver.Chrome('C:/CLI/chromedriver.exe')
# actions = ActionChains(driver)

print('What would you like to scape? Please start with a "@" for profile and a "#" for a tag')
to_scrape = input()

scrape_url = 'https://www.instagram.com/'

if to_scrape.startswith('@'):
    scrape_url += to_scrape[1:]
elif to_scrape.startswith('#'):
    scrape_url += 'explore/tags/' + to_scrape[1:]
else:
    exit(f'{BAD_STRING} NO COMPATIBLE TAG/USERNAME')

print('Starting scraper for', to_scrape)

driver = webdriver.Chrome('C:/CLI/chromedriver.exe')
actions = ActionChains(driver)
driver.get(scrape_url)

print(f'{GOOD_STRING} Started scraper for {to_scrape}..')

if len(driver.find_elements_by_xpath("//*[contains(text(), 'This Account is Private')]")) != 0:
    exit(f'{BAD_STRING} ACCOUNT IS PRIVATE CAN\'T SCRAPE')