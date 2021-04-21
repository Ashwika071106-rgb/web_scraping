from selenium import webdriver
from bs4 import BeautifulSoup
#importing time to make our code sleep for some time so that the webpage could load properly before scraping it
import time
#importing csv so that we can export ths data that we scrape into csv
import csv

START_URL = "https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"

browser = webdriver.Chrome("C:/Users/DELL/Desktop/scraper/venv/chromedriver.exe")

browser.get(START_URL)

time.sleep(10)

def scrape():
    headers = ["name","light_years_from_earth","planet_mass","stellar_magnitude","discovery_date"]
    planet_data = []
    for i in range(0,428):
        #to read the webpage as html
        soup = BeautifulSoup(browser.page_source,"html.parser")
        #to find all the ul tags with class exoplanet
        for ul_tag in soup.find_all("ul",attrs = {"class","exoplanet"}):
            li_tags = ul_tag.find_all("li")
            temp_list = []
            for index,li_tag in enumerate(li_tags):
                if(index == 0):
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tag.contents[0])
                    except:
                        temp_list.append("")
            planet_data.append(temp_list)
        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
    with open("scraper_2.csv","w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(planet_data)
scrape()