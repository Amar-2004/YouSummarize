
#Selenium WebDriver -> Service -> ChromeDriver -> Chrome Browser
import time 

import os

from SSL_check import check_SSL

from config import download_directory

from selenium import webdriver      #This essentially imports all the needed stuff to interact with the website.

from selenium.webdriver.chrome.service import Service  #it typically handles the webdriver's connection to the browser

from selenium.webdriver.common.by import By #used to locate the elements on the webpage

from selenium.webdriver.common.keys import Keys #simulates the keyboard pressings/actions    

from selenium.webdriver.support.ui import WebDriverWait # pause till condition meets   

from selenium.webdriver.support import expected_conditions as e #some common changes that we could anticipate in the page used with the prev import 

from selenium.webdriver.chrome.options import Options #configures the chrome setting arguments similar to the one in command prompt

from webdriver_manager.chrome import ChromeDriverManager #eliminates need to manualy download and adjust the chromedriver upadte,versions and stuff for connection


try: 
    if not check_SSL():
        raise Exception("Unable to connect to the Host")
    
except Exception as e:
    raise Exception(e)

def extractor():
    options=Options()

    options.add_argument("--incognito") #opens the browser with incognito setting

    options.add_argument("--verbose") #for chrome logging

    prefs={"download.default_directory":download_directory ,"download.prompt_for_download": False,  # Prevent download prompt
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True } # Enable safe browsing to prevent blocking of downloads} #This is to make some advanced setting changes (use key as what the options in chrome are..)

    options.add_experimental_option("prefs",prefs)#use pref keyword to make chrome know that we are giving values for these advanced options

    service=Service(ChromeDriverManager().install()) #established service between the webdriver and the chromedriver(chromedriver is managed by the service)

    print(f"Using Chromedriver at: {service.path}")

    driver = webdriver.Chrome(service=service,options=options) #driver is the webdriver that we create

    try:
        driver.get("https://tactiq.io/tools/youtube-transcript") #goes to the given URL
        input_field=driver.find_element(By.ID,"yt-2")  #finds the inputfield using By.ID
        ylink=input("Enter the youtube link:") 
        input_field.send_keys(ylink)        #gives the input as the youtube link
        input_field.send_keys(Keys.ENTER) #simulates the action of enter 
        time.sleep(10)  #wait for sometime to load the dom (dynamic load problem)
        initial_files = os.listdir(download_directory)
        download=WebDriverWait(driver,60).until(e.element_to_be_clickable((By.ID,"download")))
        download.click()
        print("Download button Clicked")
        wait = WebDriverWait(driver, 60)
        wait.until(lambda driver: len(os.listdir(download_directory)) > len(initial_files)) #checking if the file got downloaded
        download_path=[os.path.join(download_directory,f) for f in os.listdir(download_directory) if f not in initial_files]
    except Exception as e:
        print(f"Exception occured {e}")
        raise Exception("Could not complete the download")

    else:
        print("The File was downloaded successfully")
        return download_path[0]
    finally:
        driver.quit()
        






