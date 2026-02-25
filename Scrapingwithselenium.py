# -*- coding: utf-8 -*-

import selenium
import pandas as pd
from selenium import webdriver#importing things
from selenium.webdriver.common.by import By
import time
 #helpful for exporting data

url= 'https://www.helis.com/database/model/AW109E/cn'# setting our url
driver=webdriver.Chrome()#defining what webdriver we want to use
driver.get(url)#opens the url we told it earlier
time.sleep(3) # Sleep for 3 seconds

#mitabla# the class of the section of the page which contains all the nessecary info
#//*[@id="trcnmod11046"]/td[4]/b#copied 'xpath' of the location of the title of the vid when inspecting the page
#//*[@id="metadata-line"]/span[1]#copied xpath of the views of the video
#//*[@id="metadata-line"]/span[2]#copied xpath of the age of the video

rows=driver.find_elements(By.CLASS_NAME,'mitabla')#finds all the things (elements) within the class: style.scope ect

for row in rows: #this loops through all the rows in the page and collects the info from them
   # title= row.find_element_by_xpath('.//*[@id="trcnmod11046"]/td[4]/b').text#within all elements that match our class name, store it in rows, then for each one in rows, store it in row. Then look in the variable row for the element which matches the id thing. Dont forget the dot. The .text allows us to only get the text out of it rather than anything else
    code = row.find_element(By.XPATH, "//tr[starts-with(@id, 'trcnmod')]").text# this seems to be the new method so idk if either will work
    #title = row.find_element(By.XPATH, '//*[@id="trcnmod11046"]/td[4]/b').text
    year = row.find_element(By.XPATH, '//*[@id="trcnmod11046"]/td[3]').text
    country= row.find_element(By.XPATH,'//*[@id="trcnmod11046"]/td[4]/img').text #same again for veiws
    

    print(code)#just checking it works

    #Now for using panda to export stuff
    row_list=[]
    vid_item ={#storing all the info into a 'dictionary'
        'Tail Number': code,
        'Country': country,
       'Year': year
        }
    row_list.append(vid_item)#adding the dictionary stuff to a list

df= pd.DataFrame(row_list)
print(df)

