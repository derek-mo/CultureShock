from bs4 import BeautifulSoup

with open("index.html") as fp:
    soup = BeautifulSoup(fp, "lxml")

#soup = BeautifulSoup
 
from selenium import webdriver
PATH = "C:\Program Files (x86)\chromedriver.exe"
