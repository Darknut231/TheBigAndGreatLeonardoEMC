# -*- coding: utf-8 -*-

import selenium
from selenium import webdriver#importing things
from selenium.webdriver.common.by import By
from pandas import pd #helpful for exporting data

url= 'https://www.helis.com/database/model/AW109E/cn'# setting our url
driver=webdriver.Chrome()#defining what webdriver we want to use
driver.get(url)#opens the url we told it earlier

#mitabla# the class of the section of the page which contains all the nessecary info
#//*[@id="trcnmod11046"]/td[4]/b#copied 'xpath' of the location of the title of the vid when inspecting the page
#//*[@id="metadata-line"]/span[1]#copied xpath of the views of the video
#//*[@id="metadata-line"]/span[2]#copied xpath of the age of the video

rows=driver.find_elements_by_class_name('mitabla')#finds all the things (elements) within the class: style.scope ect

for row in rows: #this loops through all the rows in the page and collects the info from them
   # title= row.find_element_by_xpath('.//*[@id="trcnmod11046"]/td[4]/b').text#within all elements that match our class name, store it in rows, then for each one in rows, store it in row. Then look in the variable row for the element which matches the id thing. Dont forget the dot. The .text allows us to only get the text out of it rather than anything else
    title = row.find_elements(By.XPATH, "//tr[starts-with(@id, 'trcnmod')]").text# this seems to be the new method so idk if either will work
    country= row.find_element_by_xpath('.//*[@id="trcnmod11046"]/td[4]/img').text #same again for veiws
    year= row.find_element_by_xpath('.//*[@id="trcnmod11046"]/td[3]').text#and again for age

    print(title)#just checking it works

    #Now for using panda to export stuff
    row_list=[]
    vid_item ={#storing all the info into a 'dictionary'
        'title': title,
        'Country': country,
       'Year': year
        }
    row_list.append(vid_item)#adding the dictionary stuff to a list

df= pd.DataFrame(row_list)
print(df)
