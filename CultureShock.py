import csv
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
# file I/O for countries.csv also receive random country for the week
countryList = []

with open('countries.csv', 'r') as countries:
    csv_reader = csv.reader(countries)
    
    next(csv_reader)

    for line in csv_reader:
        countryList.append(line[1])
    
countryName = random.choice(countryList)

#Path is where the chrome driver is located
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.maximize_window()

driver.get("https://www.worldcountriesforkids.com/" + countryName + "/")
fact = driver.find_element(By.CLASS_NAME,"brief-history-left").text
#print(fact)
fact_list = []
temp = ""
for x in range(0,len(fact)):
    if fact[x] == '\n':
        fact_list.append(temp)
        temp = ""
    else:
        temp = temp + fact[x]
fact_sheet = []
for y in fact_list:
    fact_sheet.append([y.lstrip()])
print(fact_sheet)
driver.quit()
