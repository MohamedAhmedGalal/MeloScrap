# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 11:31:41 2022

@author: mohamad.galal
"""


from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

# Specify the folder to download into
down_directory='D:\scraped_musi'


# Specify the webbrowser options:    
# 1-Create an object of options    
options = Options()
# 2-initiate the Chrome Browsing Context in headless mode without opening the browser (background operation)
options.add_argument('--headless')
#3- set default download directory of the browser (chrome) to the desired above mentioned location ('down_directory') 
prefs = {'download.default_directory' : down_directory}

# Poinys 4 and five are related to each others 
#  4-disable images in chromedriver downloaded from 
options.add_experimental_option( "prefs", {'profile.default_content_settings.images': 2})
#  5- Add above defined prefs to preferences 
options.add_experimental_option('prefs', prefs)


# 5- specify webdriver location(https://chromedriver.chromium.org/)
webdriver_path='D:\chromedriver.exe'

# 6-create a driver object as a webdriver,using the above specified options
driver = webdriver.Chrome(webdriver_path,options=options)


# Open the site to download from:
web_url='https://arab-zik.com/en/artist/2143-omar-khairat#google_vignette'
driver.get(web_url)


# To print name of melody being downloaded:
    # The functions must first get the melody download site (site_name) where it contains the melody name,second it is needed to remove all unneeded words (banned words)
    # to print the number of melody being downloaded now, we get it as input from the for loop of download (mel_no)
def download_prmpt (site_name,mel_no):
    
    # 1- Remove unneeded words (strings) from fetched site
    
    # a) define the banned words to be deleted
    bannedWord = ["https",":","arab",'zik','.','com','en','track','/','arab','zik','com','en','track']

    # b) replace all found banned words with nothing ("") (empty quotations marks)
    # For loop to iterate through all banned words,then replace/update and so on until looping ends
    for i in range(0,len(bannedWord)):
      new_string = site_name.replace(bannedWord[i],"")
      site_name=new_string
     
      # Replace (-) character with space 
    final_stripped=new_string.replace("-"," ")
    
    # remove all numbers characters:
    numbers=[item for item in range(0,10)]
    for i in range(0,len(numbers)):
      new_string = final_stripped.replace(str(numbers[i]),"")
      final_stripped=new_string
      
       # print the final stripped melody name and number of it 
    print('Downloading melody(' + str(mel_no) + ')' +final_stripped,sep="\n")




# for i in range (1,10):
    # create an empty list of hrefs scraped from site
hrefs=[]

# create an empty list of seconds, to know how many seconds needed to download each melody
seconds_list=[]


# Define a function that knows how many seconds needed to download each melody,waits until download is completed such that to close the downloading webbrowser tab after each download
# timeout variable specifies how much seconds the browser can wait and downloading before closing
def download_wait(directory, timeout, nfiles=None):
    seconds = 0
    dl_wait = True
    while dl_wait and seconds < timeout:
        time.sleep(1)
        dl_wait = False
        files = os.listdir(directory)
        if nfiles and len(files) != nfiles:
            dl_wait = True
# If the folder contains a .crdownload file,this means that the download is not finished yet

# Loop through all file names within download folder (directory)
        for fname in files:
            if fname.endswith('.crdownload'):
                dl_wait = True
                
        seconds += 1
        print(seconds)
    return seconds

# Download first 100 melodies
for i in range (1,100):
    
# i=10
    driver_2= webdriver.Chrome(webdriver_path,options=options)

    xpath_2='/html/body/div[1]/main/div/div/div[1]/div[3]/div/div[1]/div/div/table/tbody/tr[{}]/td[2]/a'.format(i)
    element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, xpath_2 )))
    
    # button=driver.find_elements(By.TAG_NAME,qq)
    # button=driver.find_elements(By.CLASS_NAME,qq)
    button=driver.find_element(By.XPATH,xpath_2)
    
    qq=button.get_attribute('href')
    
    hrefs.append(qq)
    # time.sleep(4)
    # url_2='https://arab-zik.com/en/track/42399-am-ahmd-al-msry'
    driver_2.get(qq)
    
    xpath_3='//*[@id="main-container"]/div/div/div[1]/div[3]/div/div/div/a'
    element = WebDriverWait(driver_2, 20).until(EC.presence_of_element_located((By.XPATH, xpath_3 )))

    button_2=driver_2.find_element(By.XPATH,xpath_3)
    
    wewe=button_2.get_attribute('href')
    driver_2.execute_script("window.open('');")
      
    # Switch to the new window and open new URL
    driver_2.switch_to.window(driver_2.window_handles[1])
    driver_2.get(wewe)
    
    download_prmpt(qq,i)
    
    
        
    secondsy=download_wait(down_directory,30)
    seconds_list.append(secondsy)

    
    driver_2.close()

    driver_2.switch_to.window(driver_2.window_handles[0])

    driver_2.close()

    




















