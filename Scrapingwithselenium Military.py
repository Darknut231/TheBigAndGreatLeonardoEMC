
import selenium
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images": 2}
options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(options=options)
row_list=[]

driver.get('https://www.helis.com/database')
WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, '//*[@class="fc-button fc-cta-consent fc-primary-button"]'))).click()

#A109LUH,
for page in range(1, 2):  # this loops through all the pages and collects the data from them
    url = f"https://www.helis.com/database/model/A109LUH/cn?pag={page}"
    driver.get(url)

    rows = driver.find_elements(By.XPATH, "//tr[starts-with(@id,'trcnmod')]")

    for row in rows: 
        
        #MODEL
        model=driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/h1').text
        
        #code = row.find_element(By.XPATH, ".//td[5]/b").text  
        
        #YEAR
        if len(row.find_element(By.XPATH, ".//td[3]").text) > 0:
            year = row.find_element(By.XPATH, ".//td[3]").text
        else:
            year='NA'                                           
        

        #COUNTRY, This bit is ai so idk how it works sry
        imgs = row.find_elements(By.XPATH, ".//td[4]/img")

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

        #ADDING THE DATA TO THE DATA FRAME
        vid_item ={
            #'Tail Number': code,
            'Country': countries,
            'Year': year,
            'Still Operational':operable,
            'Model': model
            }
        row_list.append(vid_item)

#AW101 610, No CN page,
for page in range(1):  # this loops through all the pages and collects the data from them
    url = f"https://www.helis.com/database/model/1193/{page}"
    driver.get(url)

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

        #ADDING THE DATA TO THE DATA FRAME
        vid_item ={
            #'Tail Number': code,
            'Country': countries,
            'Year': year,
            'Still Operational':operable,
            'Model': model
            }
        row_list.append(vid_item)

#AW101 611, No CN page,
for page in range(1):  # this loops through all the pages and collects the data from them
    url = f"https://www.helis.com/database/model/HH-101A-Caesar/{page}"
    driver.get(url)

    rows = driver.find_elements(By.XPATH, "//tr[starts-with(@id,'trcnmod')]")

    for row in rows: 
        
        #MODEL
        model=driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/h1').text
        
        #TAIL NUMBER
        #code = row.find_element(By.XPATH, ".//td[5]/b").text  
        
        #YEAR
        if len(row.find_element(By.XPATH, ".//td[3]").text) > 0:
            year = row.find_element(By.XPATH, ".//td[3]").text
        else:
            year='NA'                                           
        

        #COUNTRY, This bit is ai so idk how it works sry
        imgs = row.find_elements(By.XPATH, ".//td[4]/img")

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

        #ADDING THE DATA TO THE DATA FRAME
        vid_item ={
            #'Tail Number': code,
            'Country': countries,
            'Year': year,
            'Still Operational':operable,
            'Model': model
            }
        row_list.append(vid_item)

#AW101 612, No CN page
for page in range(1):  # this loops through all the pages and collects the data from them
    url = f"https://www.helis.com/database/model/AW101-Mk612/{page}"
    driver.get(url)

    rows = driver.find_elements(By.XPATH, "//tr[starts-with(@id,'trcnmod')]")

    for row in rows: 
        
        #MODEL
        model=driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/h1').text
        
        #TAIL NUMBER
        #code = row.find_element(By.XPATH, ".//td[5]/b").text  
        
        #YEAR
        if len(row.find_element(By.XPATH, ".//td[3]").text) > 0:
            year = row.find_element(By.XPATH, ".//td[3]").text
        else:
            year='NA'                                           
        

        #COUNTRY, This bit is ai so idk how it works sry
        imgs = row.find_elements(By.XPATH, ".//td[4]/img")

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

        #ADDING THE DATA TO THE DATA FRAME
        vid_item ={
            #'Tail Number': code,
            'Country': countries,
            'Year': year,
            'Still Operational':operable,
            'Model': model
            }
        row_list.append(vid_item)

#AW101 614, No CN page
for page in range(1):  # this loops through all the pages and collects the data from them
    url = f"https://www.helis.com/database/model/AW101-614/{page}"
    driver.get(url)

    rows = driver.find_elements(By.XPATH, "//tr[starts-with(@id,'trcnmod')]")

    for row in rows: 
        
        #MODEL
        model=driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/h1').text
        
        #TAIL NUMBER
        #code = row.find_element(By.XPATH, ".//td[5]/b").text  
        
        #YEAR
        if len(row.find_element(By.XPATH, ".//td[3]").text) > 0:
            year = row.find_element(By.XPATH, ".//td[3]").text
        else:
            year='NA'                                           
        

        #COUNTRY, This bit is ai so idk how it works sry
        imgs = row.find_elements(By.XPATH, ".//td[4]/img")

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

        #ADDING THE DATA TO THE DATA FRAME
        vid_item ={
            #'Tail Number': code,
            'Country': countries,
            'Year': year,
            'Still Operational':operable,
            'Model': model
            }
        row_list.append(vid_item)

#AW101 640, No CN page
for page in range(1):  # this loops through all the pages and collects the data from them
    url = f"https://www.helis.com/database/model/1281/{page}"
    driver.get(url)

    rows = driver.find_elements(By.XPATH, "//tr[starts-with(@id,'trcnmod')]")

    for row in rows: 
        
        #MODEL
        model=driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/h1').text
        
        #TAIL NUMBER
        #code = row.find_element(By.XPATH, ".//td[5]/b").text  
        
        #YEAR
        if len(row.find_element(By.XPATH, ".//td[3]").text) > 0:
            year = row.find_element(By.XPATH, ".//td[3]").text
        else:
            year='NA'                                           
        

        #COUNTRY, This bit is ai so idk how it works sry
        imgs = row.find_elements(By.XPATH, ".//td[4]/img")

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

        #ADDING THE DATA TO THE DATA FRAME
        vid_item ={
            #'Tail Number': code,
            'Country': countries,
            'Year': year,
            'Still Operational':operable,
            'Model': model
            }
        row_list.append(vid_item)

#AW101 641, No CN page
for page in range(1):  # this loops through all the pages and collects the data from them
    url = f"https://www.helis.com/database/model/1209/{page}"
    driver.get(url)

    rows = driver.find_elements(By.XPATH, "//tr[starts-with(@id,'trcnmod')]")

    for row in rows: 
        
        #MODEL
        model=driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/h1').text
        
        #TAIL NUMBER
        #code = row.find_element(By.XPATH, ".//td[5]/b").text  
        
        #YEAR
        if len(row.find_element(By.XPATH, ".//td[3]").text) > 0:
            year = row.find_element(By.XPATH, ".//td[3]").text
        else:
            year='NA'                                           
        

        #COUNTRY, This bit is ai so idk how it works sry
        imgs = row.find_elements(By.XPATH, ".//td[4]/img")

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

        #ADDING THE DATA TO THE DATA FRAME
        vid_item ={
            #'Tail Number': code,
            'Country': countries,
            'Year': year,
            'Still Operational':operable,
            'Model': model
            }
        row_list.append(vid_item)

#AW101 642, No CN page
for page in range(1):  # this loops through all the pages and collects the data from them
    url = f"https://www.helis.com/database/model/1299/{page}"
    driver.get(url)

    rows = driver.find_elements(By.XPATH, "//tr[starts-with(@id,'trcnmod')]")

    for row in rows: 
        
        #MODEL
        model=driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/h1').text
        
        #TAIL NUMBER
        #code = row.find_element(By.XPATH, ".//td[5]/b").text  
        
        #YEAR
        if len(row.find_element(By.XPATH, ".//td[3]").text) > 0:
            year = row.find_element(By.XPATH, ".//td[3]").text
        else:
            year='NA'                                           
        

        #COUNTRY, This bit is ai so idk how it works sry
        imgs = row.find_elements(By.XPATH, ".//td[4]/img")

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

        #ADDING THE DATA TO THE DATA FRAME
        vid_item ={
            #'Tail Number': code,
            'Country': countries,
            'Year': year,
            'Still Operational':operable,
            'Model': model
            }
        row_list.append(vid_item)

#AW101 VVIP, No CN page
for page in range(1):  # this loops through all the pages and collects the data from them
    url = f"https://www.helis.com/database/model/AW101-VIP/{page}"
    driver.get(url)

    rows = driver.find_elements(By.XPATH, "//tr[starts-with(@id,'trcnmod')]")

    for row in rows: 
        
        #MODEL
        model=driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/h1').text
        
        #TAIL NUMBER
        #code = row.find_element(By.XPATH, ".//td[5]/b").text  
        
        #YEAR
        if len(row.find_element(By.XPATH, ".//td[3]").text) > 0:
            year = row.find_element(By.XPATH, ".//td[3]").text
        else:
            year='NA'                                           
        

        #COUNTRY, This bit is ai so idk how it works sry
        imgs = row.find_elements(By.XPATH, ".//td[4]/img")

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

        #ADDING THE DATA TO THE DATA FRAME
        vid_item ={
            #'Tail Number': code,
            'Country': countries,
            'Year': year,
            'Still Operational':operable,
            'Model': model
            }
        row_list.append(vid_item)

#AW139M
for page in range(1):  # this loops through all the pages and collects the data from them
    url = f"https://www.helis.com/database/model/AW139M/cn{page}"
    driver.get(url)

    rows = driver.find_elements(By.XPATH, "//tr[starts-with(@id,'trcnmod')]")

    for row in rows: 
        
        #MODEL
        model=driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/h1').text
        
        #TAIL NUMBER
        #code = row.find_element(By.XPATH, ".//td[5]/b").text  
        
        #YEAR
        if len(row.find_element(By.XPATH, ".//td[3]").text) > 0:
            year = row.find_element(By.XPATH, ".//td[3]").text
        else:
            year='NA'                                           
        

        #COUNTRY, This bit is ai so idk how it works sry
        imgs = row.find_elements(By.XPATH, ".//td[4]/img")

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

        #ADDING THE DATA TO THE DATA FRAME
        vid_item ={
            #'Tail Number': code,
            'Country': countries,
            'Year': year,
            'Still Operational':operable,
            'Model': model
            }
        row_list.append(vid_item)

#AW149
for page in range(1):  # this loops through all the pages and collects the data from them
    url = f"https://www.helis.com/database/model/AW149/cn{page}"
    driver.get(url)

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

        #ADDING THE DATA TO THE DATA FRAME
        vid_item ={
            #'Tail Number': code,
            'Country': countries,
            'Year': year,
            'Still Operational':operable,
            'Model': model
            }
        row_list.append(vid_item)

#AW159
for page in range(1):  # this loops through all the pages and collects the data from them
    url = f"https://www.helis.com/database/model/AW159/{page}"
    driver.get(url)

    rows = driver.find_elements(By.XPATH, "//tr[starts-with(@id,'trcnmod')]")

    for row in rows: 
        
        #MODEL
        model=driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/h1').text
        
        #TAIL NUMBER
        #code = row.find_element(By.XPATH, ".//td[5]/b").text  
        
        #YEAR
        if len(row.find_element(By.XPATH, ".//td[3]").text) > 0:
            year = row.find_element(By.XPATH, ".//td[3]").text
        else:
            year='NA'                                           
        

        #COUNTRY, This bit is ai so idk how it works sry
        imgs = row.find_elements(By.XPATH, ".//td[4]/img")

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

        #ADDING THE DATA TO THE DATA FRAME
        vid_item ={
            #'Tail Number': code,
            'Country': countries,
            'Year': year,
            'Still Operational':operable,
            'Model': model
            }
        row_list.append(vid_item)

#AW159 210
for page in range(1):  # this loops through all the pages and collects the data from them
    url = f"https://www.helis.com/database/model/1367/{page}"
    driver.get(url)

    rows = driver.find_elements(By.XPATH, "//tr[starts-with(@id,'trcnmod')]")

    for row in rows: 
        
        #MODEL
        model=driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/h1').text
        
        #TAIL NUMBER
        #code = row.find_element(By.XPATH, ".//td[5]/b").text  
        
        #YEAR
        if len(row.find_element(By.XPATH, ".//td[3]").text) > 0:
            year = row.find_element(By.XPATH, ".//td[3]").text
        else:
            year='NA'                                           
        

        #COUNTRY, This bit is ai so idk how it works sry
        imgs = row.find_elements(By.XPATH, ".//td[4]/img")

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

        #ADDING THE DATA TO THE DATA FRAME
        vid_item ={
            #'Tail Number': code,
            'Country': countries,
            'Year': year,
            'Still Operational':operable,
            'Model': model
            }
        row_list.append(vid_item)

#AW159 220, 
for page in range(1):  # this loops through all the pages and collects the data from them
    url = f"https://www.helis.com/database/model/AW159-220/{page}"
    driver.get(url)

    rows = driver.find_elements(By.XPATH, "//tr[starts-with(@id,'trcnmod')]")

    for row in rows: 
        
        #MODEL
        model=driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/h1').text
        
        #TAIL NUMBER
        #code = row.find_element(By.XPATH, ".//td[5]/b").text  
        
        #YEAR
        if len(row.find_element(By.XPATH, ".//td[3]").text) > 0:
            year = row.find_element(By.XPATH, ".//td[3]").text
        else:
            year='NA'                                           
        

        #COUNTRY, This bit is ai so idk how it works sry
        imgs = row.find_elements(By.XPATH, ".//td[4]/img")

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

        #ADDING THE DATA TO THE DATA FRAME
        vid_item ={
            #'Tail Number': code,
            'Country': countries,
            'Year': year,
            'Still Operational':operable,
            'Model': model
            }
        row_list.append(vid_item)

#AW159 WildCat AH1, 
for page in range(1):  # this loops through all the pages and collects the data from them
    url = f"https://www.helis.com/database/model/Wildcat-AH1/cn{page}"
    driver.get(url)

    rows = driver.find_elements(By.XPATH, "//tr[starts-with(@id,'trcnmod')]")

    for row in rows: 
        
        #MODEL
        model=driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/h1').text
        
        #TAIL NUMBER
        #code = row.find_element(By.XPATH, ".//td[5]/b").text  
        
        #YEAR
        if len(row.find_element(By.XPATH, ".//td[3]").text) > 0:
            year = row.find_element(By.XPATH, ".//td[3]").text
        else:
            year='NA'                                           
        

        #COUNTRY, This bit is ai so idk how it works sry
        imgs = row.find_elements(By.XPATH, ".//td[4]/img")

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

        #ADDING THE DATA TO THE DATA FRAME
        vid_item ={
            #'Tail Number': code,
            'Country': countries,
            'Year': year,
            'Still Operational':operable,
            'Model': model
            }
        row_list.append(vid_item)

#AW159 WildCat HMA2, 
for page in range(1):  # this loops through all the pages and collects the data from them
    url = f"https://www.helis.com/database/model/Wildcat-HMA2/cn/{page}"
    driver.get(url)


    rows = driver.find_elements(By.XPATH, "//tr[starts-with(@id,'trcnmod')]")

    for row in rows: 
        
        #MODEL
        model=driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/h1').text
        
        #TAIL NUMBER
        #code = row.find_element(By.XPATH, ".//td[5]/b").text  
        
        #YEAR
        if len(row.find_element(By.XPATH, ".//td[3]").text) > 0:
            year = row.find_element(By.XPATH, ".//td[3]").text
        else:
            year='NA'                                           
        

        #COUNTRY, This bit is ai so idk how it works sry
        imgs = row.find_elements(By.XPATH, ".//td[4]/img")

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

        #ADDING THE DATA TO THE DATA FRAME
        vid_item ={
            #'Tail Number': code,
            'Country': countries,
            'Year': year,
            'Still Operational':operable,
            'Model': model
            }
        row_list.append(vid_item)

#AW169 Skids, 
for page in range(1):  # this loops through all the pages and collects the data from them
    url = f"https://www.helis.com/database/model/AW169-skids/{page}"
    driver.get(url)


    rows = driver.find_elements(By.XPATH, "//tr[starts-with(@id,'trcnmod')]")

    for row in rows: 
        
        #MODEL
        model=driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/h1').text
        
        #TAIL NUMBER
        #code = row.find_element(By.XPATH, ".//td[5]/b").text  
        
        #YEAR
        if len(row.find_element(By.XPATH, ".//td[3]").text) > 0:
            year = row.find_element(By.XPATH, ".//td[3]").text
        else:
            year='NA'                                           
        

        #COUNTRY, This bit is ai so idk how it works sry
        imgs = row.find_elements(By.XPATH, ".//td[4]/img")

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

        #ADDING THE DATA TO THE DATA FRAME
        vid_item ={
            #'Tail Number': code,
            'Country': countries,
            'Year': year,
            'Still Operational':operable,
            'Model': model
            }
        row_list.append(vid_item)

#AW169M, 
for page in range(1):  # this loops through all the pages and collects the data from them
    url = f"https://www.helis.com/database/model/AW169M/{page}"
    driver.get(url)


    rows = driver.find_elements(By.XPATH, "//tr[starts-with(@id,'trcnmod')]")

    for row in rows: 
        
        #MODEL
        model=driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/h1').text
        
        #TAIL NUMBER
        #code = row.find_element(By.XPATH, ".//td[5]/b").text  
        
        #YEAR
        if len(row.find_element(By.XPATH, ".//td[3]").text) > 0:
            year = row.find_element(By.XPATH, ".//td[3]").text
        else:
            year='NA'                                           
        

        #COUNTRY, This bit is ai so idk how it works sry
        imgs = row.find_elements(By.XPATH, ".//td[4]/img")

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

        #ADDING THE DATA TO THE DATA FRAME
        vid_item ={
            #'Tail Number': code,
            'Country': countries,
            'Year': year,
            'Still Operational':operable,
            'Model': model
            }
        row_list.append(vid_item)


#EXPORTING OUR DATA FRAME
df= pd.DataFrame(row_list)
print(df)
#CHANGE THE LOCATION TO THE LOACATION OF YOUR FOLDER WHERE YOU WANT THE FILE TO BE PLACED
df.to_excel(r"C:\Users\alexw\OneDrive\Documents\EMS\EMC\Data Dump- Tests\EMCDATA,Military.xlsx", index=False)# 
