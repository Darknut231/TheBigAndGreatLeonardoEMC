
import selenium
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

url= 'http://helis.com/database/model/AW109E/cn'
driver=webdriver.Chrome()
driver.get(url)
time.sleep(3) #Press Consent

row_list=[]
rows = driver.find_elements(By.XPATH, "//tr[starts-with(@id,'trcnmod')]")

for row in rows: 
    
    #TAIL NUMBER
    code = row.find_element(By.XPATH, ".//td[4]/b").text  
    
    #YEAR
    if len(row.find_element(By.XPATH, ".//td[3]").text) > 0:
        year = row.find_element(By.XPATH, ".//td[3]").text
    else:
        continue                                           
    
    #COUNTRY, This bit is ai so idk how it works sry
    imgs = row.find_elements(By.XPATH, ".//td[4]/img")

    countries = [img.get_attribute("alt") for img in imgs if img.get_attribute("alt")]
    if not countries:
       continue

    country_string = ", ".join(countries)

    #Exporting The Data
    vid_item ={
        'Tail Number': code,
        'Country': countries,
        'Year': year
        }
    row_list.append(vid_item)
df= pd.DataFrame(row_list)
print(df)
df.to_excel(r"C:\Users\alexw\OneDrive\Documents\EMS\EMC\Data Dump- Tests\EMCDATA0.xlsx", index=False)# this will now go in the folder, to change the name change teh EMCDATA0 to smh else

