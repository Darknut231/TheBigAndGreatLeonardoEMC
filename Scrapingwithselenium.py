
import selenium
import pandas as pd
from selenium import webdriver#importing things
from selenium.webdriver.common.by import By
import time
 #helpful for exporting data

url= 'https://www.helis.com/database/model/AW109E/cn'# setting our url
driver=webdriver.Chrome()#defining what webdriver we want to use
driver.get(url)#opens the url we told it earlier
time.sleep(3) # Wait for 3 seconds

#mitabla the class of the section of the page which contains all the nessecary info ## this is replaced by a diferenet method of searching the url as when looping through the mitabla, it only looped through the tables rather than the rows within the table
#//*[@id="trcnmod11046"]/td[4]/b#copied 'xpath' of the location of the title of the vid when inspecting the page ##this can be simplified to .//td[4]/b as we are aleady looking in the correct row (id=trcnmod11046) using line 23
#//*[@id="metadata-line"]/span[1]#copied xpath of the views of the video, ##same for this one
#//*[@id="metadata-line"]/span[2]#copied xpath of the age of the video    ##and this one

row_list=[]# set this outside the loop so it dosent get wiped every time we run the loop 

#rows=driver.find_elements(By.CLASS_NAME,'mitabla')#finds all the things (elements) within the class: style.scope ect, however this wont work as it will only find 
rows = driver.find_elements(By.XPATH, "//tr[starts-with(@id,'trcnmod')]")

for row in rows: #this loops through all the rows in the page and collects the info from them
   
    code = row.find_element(By.XPATH, ".//td[4]/b").text  
    year = row.find_element(By.XPATH, './/td[3]').text
    country= row.find_element(By.XPATH,'.//td[4]/img') #same again for country- this isnt working as there are some countrys missing, i am working on "no such element exemption"module
    #//*[@id="trcnmod11046"]/td[4]/img

    print(code)#just checking it works

    #Now for using panda to export stuff
    vid_item ={#storing all the info into a 'dictionary'
        'Tail Number': code,
        'Country': country,
        'Year': year
        }
    row_list.append(vid_item)#adding the dictionary stuff to a list
df= pd.DataFrame(row_list)
#print(df)
