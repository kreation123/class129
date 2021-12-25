from os import write
import bs4
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv 
import requests
startUrl = "https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"
browser = webdriver.Chrome("C:\Users\basuk\Downloads\chromedriver_win32")
browser.get(startUrl)
time.sleep(10)
def screpe():
    headers = ["Name","Light Years From Earth","Planet Mass","STELLAR MAGNITUDE	",'DISCOVERY DATE','Planet Type','Planet Radius','Orbital Radious','ECCENTRICITY','DETECTION METHOD']
    planetData = []
    for i in range(0.428):
        soup = BeautifulSoup(browser.page_source,'html.parser')
        for ul_tag in soup.find_all("ul",attrs={'class','exoplanet'}):
            li_tags = ul_tag.find_all('li')
            path = "//*[@id="page"]/section[1]/div"
def scrapeMoreData(hyperlink):
    try:
        page = requests.get(hyperlink)
        soup = BeautifulSoup(page.content,"html.parser")
        templist  = []
        for tr_tag in soup.find_all(/'tr',attrs = {'class':'valu'}):
            try:
                templist.append(td_tags)
            accpet : 
                w.append('')
        newPlanetData.appned(templist)

screpe()
for index,data in enumerate(templist):
    scrapeMoreData(data[5])
    print(f'{index + 1 } pageDone2')
with open('final.csv','w') as f:
    csvwriter = csv.writer()
    csvwriter.writerow(headers)
    csvwriter.writerow(finaPlan46747etData)
