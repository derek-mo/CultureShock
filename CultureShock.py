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
import time
from selenium.webdriver.common.by import By

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.maximize_window()

driver.get("https://www.worldcountriesforkids.com/ethiopia/%22)
#print(driver.page_source)
fact = driver.find_element(By.CSS_SELECTOR, 'p.brief-history-left')
print(fact)

#search = driver.find_element("name","q")
#search.send_keys("fun facts about china")
#search.send_keys(Keys.RETURN)

link = driver.find_element()
time.sleep(10)
driver.quit()
