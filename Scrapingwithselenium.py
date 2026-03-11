
import selenium
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()
row_list=[]

driver.get('https://www.helis.com/database')
WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, '//*[@class="fc-button fc-cta-consent fc-primary-button"]'))).click()

#First Helicopter:
for page in range(1, 9):  # this loops through all the pages and collects the data from them
    url = f"https://www.helis.com/database/model/AW109/cn?pag={page}"
    driver.get(url)
    # if page==1:
    #    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@class="fc-button fc-cta-consent fc-primary-button"]'))).click()
    
    rows = driver.find_elements(By.XPATH, "//tr[starts-with(@id,'trcnmod')]")

    for row in rows: 
        
        #MODEL
        model=driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/h1').text
        
        #TAIL NUMBER
        #code = row.find_element(By.XPATH, ".//td[5]/b").text  
        
        #YEAR
        if len(row.find_element(By.XPATH, ".//td[4]").text) > 0:
            year = row.find_element(By.XPATH, ".//td[4]").text
        else:
            year='NA'                                           
        

        #COUNTRY, This bit is ai so idk how it works sry
        imgs = row.find_elements(By.XPATH, ".//td[5]/img")

        countries = [img.get_attribute("alt") for img in imgs if img.get_attribute("alt")]
        
        if not countries:
            countries= 'NA'
            #continue
        country_string = ", ".join(countries)

        #STILL OPERABLE
        try:
            variable=row.find_element(By.XPATH,".//td[2]/i")
            operable='False'
        except NoSuchElementException:
            operable='True'

        #Exporting The Data
        vid_item ={
         #   'Tail Number': code,
            'Country': countries,
            'Year': year,
            'Still Operational':operable,
            'Model': model
            }
        row_list.append(vid_item)

#Diferent Helicopter
# for page in range(1, 9):  # this loops through all the pages and collects the data from them
#     url = f"https://www.helis.com/database/model/AW109/cn?pag={page}"
#     driver.get(url)
#     time.sleep(3) #Press Consent

#     rows = driver.find_elements(By.XPATH, "//tr[starts-with(@id,'trcnmod')]")

#     for row in rows: 
        
#         #MODEL
#         model=driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/h1').text
        
#         #TAIL NUMBER
#         #code = row.find_element(By.XPATH, ".//td[5]/b").text  
        
#         #YEAR
#         if len(row.find_element(By.XPATH, ".//td[4]").text) > 0:
#             year = row.find_element(By.XPATH, ".//td[4]").text
#         else:
#             year='NA'                                           
        

#         #COUNTRY, This bit is ai so idk how it works sry
#         imgs = row.find_elements(By.XPATH, ".//td[5]/img")

#         countries = [img.get_attribute("alt") for img in imgs if img.get_attribute("alt")]
        
#         if not countries:
#             countries= 'NA'
#             #continue
#         country_string = ", ".join(countries)

#         #STILL OPERABLE
#         try:
#             variable=row.find_element(By.XPATH,".//td[2]/i")
#             operable='False'
#         except NoSuchElementException:
#             operable='True'

#         #Exporting The Data
#         vid_item ={
#             #'Tail Number': code,
#             'Country': countries,
#             'Year': year,
#             'Still Operational':operable,
#             'Model': model
#             }
#         row_list.append(vid_item)

df= pd.DataFrame(row_list)
print(df)
df.to_excel(r"C:\Users\alexw\OneDrive\Documents\EMS\EMC\Data Dump- Tests\EMCDATA.xlsx", index=False)# this will now go in the folder, to change the name change teh EMCDATA0 to smh else
