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

