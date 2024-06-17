import csv
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# file I/O for countries.csv also receive random country for the week
countryList = []

with open('countries.csv', 'r') as countries:
    csv_reader = csv.reader(countries)
    
    next(csv_reader)

    for line in csv_reader:
        countryList.append(line[1])
    
countryName = random.choice(countryList)
languageList = []

with open('language.csv',encoding="utf8") as phrases:
    csv_reader = csv.reader(phrases)

    next(csv_reader)

    for line in csv_reader:
        if (line[1] == countryName):
            languageList.append(line[0])
            languageList.append(line[1])
            languageList.append(line[2])
            languageList.append(line[3])
            languageList.append(line[4])
            languageList.append(line[5])
            languageList.append(line[6])
#Path is where the chrome driver is located
PATH = "C:\Program Files (x86)\chromedriver.exe"
options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(PATH, options=options)

print(countryName)

driver.get("https://open.spotify.com/search/" + countryName + "/playlists")
time.sleep(3)

input = driver.find_element(By.XPATH, '//a[@title=\"Top 50 - ' + countryName + '\"]').get_attribute('href')
playlistLink = input
#print(playlistLink)

for i in countryName:
    if i == ' ':
        countryName.replace(' ', '-')

print(countryName)

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
temp1 =""
temp2 =""
for i in range (0, len(food) - 4):
    if (food[i] == 'C') & (food[i+1] == 'u') & (food[i+2] == 'i') & (food[i+3] == 's') & (food[i + 4] == 'i'):
        for x in range (-300,6900):
            if (x > -1):
                temp1 = temp1 + food[i + x]
            else:
                temp = temp + food[i + x]
        break
#creating a list to store the data in: link, cuisine, description, and link description
food_list = []
#print(temp)
#index of the link start
link_index_start = temp.find("img src=")
if (temp.find(".jpg") == -1):
    link_index_end = temp.find(".png")
else:
    if (temp.find(".png") == -1):
        link_index_end = temp.find(".jpg")
    else :
        if (temp.find(".png") != -1 & temp.find(".jpg") != -1):
            if (temp.find(".png") > temp.find(".jpg")):
                link_index_end = temp.find(".jpg")
            else:
                link_index_end = temp.find(".png")
#print(link_index_start)
#print(link_index_end)

food_list.append(temp[link_index_start + 9:link_index_end + 4:1])

#index of the description start
food_description_start = temp1.find("<p>") + 3
food_description_end = temp1[food_description_start + 3: len(temp1) : 1].find("</p>") + food_description_start +3
#food list list is in the format
#link url, description of the food
food_list.append(temp1[food_description_start: food_description_end:1])
print("THE COUNTRY OF THE WEEK IS: " + countryName)
print("\n")
print("This is the Spotify Playlist Link for The Top 50 songs of " + countryName)
print(playlistLink)
print("\n")
print("Food options in " + countryName)
for x in food_list:
    print(x)
print("\n")
for x in fact_sheet:
    print(x)
print("\n")
counter = 0
for x in languageList:
    if counter == 0:
        print("The language they speak is " + x)
    if counter == 2:
        print("Hello is " + x + " in " + countryName)
    if counter == 3:
        print("Goodbye is " + x + " in " + countryName)
    if counter == 4:
        print("Thank you is " + x + " in " + countryName)
    if counter == 5:
        print("I have to go to the bathroom is" + x + " in " + countryName)
    if counter == 6:
        print("I'm hungry is " + x + " in " + countryName)
    counter = counter + 1

#quit the driver
driver.quit()