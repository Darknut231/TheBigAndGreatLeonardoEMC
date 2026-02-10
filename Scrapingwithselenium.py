# -*- coding: utf-8 -*-

import selenium
from selenium import webdriver#importing things
from pandas import pd #helpful for exporting data

url= 'https://www.youtube.com/@veritasium/videos'# setting our url
driver=webdriver.Chrome()#defining what webdriver we want to use
driver.get(url)#opens the url we told it earlier


style-scope ytd-rich-item-renderer# the class of the section of the page which contains all the nessecary info
//*[@id="video-title"]#copied 'xpath' of the location of the title of the vid when inspecting the page
//*[@id="metadata-line"]/span[1]#copied xpath of the views of the video
//*[@id="metadata-line"]/span[2]#copied xpath of the age of the video

videos=driver.find_elements_by_class_name('style-scope ytd-rich-item-renderer')#finds all the things (elements) within the class: style.scope ect

for video in videos #this loops through all the videos in the page and collects the info from them
    title= video.find_element_by_xpath('.//*[@id="video-title"]').text#within all elements that match our class name, store it in videos, then for each one in videos, store it in video. Then look in the variable video for the element which matches the id thing. Dont forget the dot. The .text allows us to only get the text out of it rather than anything else
    veiws= video.find_element_by_xpath('.//*[@id="metadata-line"]/span[1]').text #same again for veiws
    age= video.find_element_by_xpath('.//*[@id="metadata-line"]/span[2]').text#and again for age

#print(title,veiws,age)#just checking it works

    #Now for using panda to export stuff
    video_list[]
    vid_item ={#storing all the info into a 'dictionary'
        'title': title,
        'veiws': veiws,
        'age': age
        }
    video_list.append(vid_item)#adding the dictionary stuff to a list

df= pd.DataFrame(video_list)
print(df)