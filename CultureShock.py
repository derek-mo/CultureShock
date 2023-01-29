import csv
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# file I/O for countries.csv also receive random country for the week
countryList = []

with open('countries.csv', 'r') as countries:
    csv_reader = csv.reader(countries)
    
    next(csv_reader)

    for line in csv_reader:
        countryList.append(line[1])
    
countryName = random.choice(countryList)

PATH = "C:\Program Files (x86)\chromedriver.exe"
options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(PATH, options=options)


driver.get("https://open.spotify.com/search/" + countryName + "/playlists")
time.sleep(3)

input = driver.find_element(By.XPATH, '//a[@title=\"Top 50 - ' + countryName + '\"]').get_attribute('href')
playlistLink = input
print(playlistLink)

driver.quit()
