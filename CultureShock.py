import csv
import random

# file I/O for countries.csv also receive random country for the week
countryList = []

with open('countries.csv', 'r') as countries:
    csv_reader = csv.reader(countries)
    
    next(csv_reader)

    for line in csv_reader:
        countryList.append(line[1])
    
countryName = random.choice(countryList)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.maximize_window()

driver.get("https://open.spotify.com/search/" + countryName + "/playlists")
# input = driver.find_element(By.TAG_NAME, 'input')
# input.send_keys('Japan')
#input.send_keys(Keys.ENTER)

#input = driver.find_element(By.XPATH, '//a[@href]')
#input.click()
#print(input)

time.sleep(10)
driver.quit()
