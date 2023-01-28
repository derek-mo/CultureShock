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
fact_list = []
temp = ""

#accesses the fact file
for x in range(0,len(fact)):
    if fact[x] == '\n':
        fact_list.append(temp)
        temp = ""
    else:
        temp = temp + fact[x]
fact_sheet = []

#removes the whitespace to the list
for y in fact_list:
    fact_sheet.append([y.lstrip()])

#access food element
food = driver.page_source
temp = ""
for i in range (0, len(food) - 4):
    if (food[i] == 'C') & (food[i+1] == 'u') & (food[i+2] == 'i') & (food[i+3] == 's') & (food[i + 4] == 'i'):
        for x in range (-500,700):
            temp = temp + food[i + x]
        break

#creating a list to store the data in: link, cuisine, description, and link description
food_list = []

#index of the link start
link_index_start = temp.find("img src=")
link_index_end = temp.find(".png")
food_list.append(temp[link_index_start + 9:link_index_end + 4:1])
print(food_list)

#index of the description start
food_description_start = temp.find("<p>")
food_description_end = temp[food_description_start + 10: len(temp): 1].find("<p>")
#print(temp[food_description_start:food_description_end:1])
print(food_description_start)
print(food_description_end)
print(temp[food_description_start: food_description_end:1])
#print(temp[food_description_start: food_description_end:1])
#print(temp)
#quit the driver
driver.quit()
