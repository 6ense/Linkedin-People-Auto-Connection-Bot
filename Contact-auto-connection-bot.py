"""                            @                  @                             
                               @@                @@                             
                               @@@              @ @                             
               @              &@ @@            @  @              #              
                @@            @@  @@         *@   @            @@               
                @@@@          @@   &@       @@    @          @@@(               
                 @@ (@%       @@@(             ,@@@        @  @@                
                  @&  @@@   @@@@@&   &@@@@@&   @@@@@@   @@@   @                 
        #          @   @@@     @@@      @.     @@@     @@@  *@             #    
         @@@     @@@      @@#                       @@@      @@@        @@        
          @ *@  @@        #@                         @@         @@  @ %@  #       
           ,  @@         @@                           @@         @@     #        
            @*          &@                             @/          @@           
          @@            @@                             @@            @@         
          @@            @@           S1X3NSE           @@            @@         
            @@          .@                             @           @@           
              @@         @@                           @@         @@             
                @@@        @%                        @        @@@               
                   &@@       @@                   @@       @@/                  
                       &@@@     @@@           @@@     @@@%                      
                             @@@@@@#   *#,   %@@@@@@                            
                                       


******** NOTE ********

My contribution to the project started by "Python Simplified".
    - updated the code to correct deprecated errors; 
    - added a page cycler."""   
                                       

from fileinput import close
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

#open linkedin.com
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://linkedin.com/")

time.sleep(2)

#find UN/PW fields on the page
username = driver.find_element(By.XPATH, "//input[@name='session_key']")
password = driver.find_element(By.XPATH, "//input[@name='session_password']")

#*************** STEP 1 ****************

#********************LOGIN INFORMATION****************
#Input login credentials
username.send_keys('')
password.send_keys('')

time.sleep(2)

#click the submit button to login
submit = driver.find_element(By.XPATH, "//button[@type='submit']").click()

#the number of pages to cycle through
n_pages = 8

#looping through page numbers, by adding the the range as a str at the end of the URL for page=n 
for n in range(1,n_pages):

    #*************** STEP 2 ****************

    #Enter the URL for 2nd Connections 
    driver.get("https://www.linkedin.com/search/results/people/?network=%5B%22S%22%5D&origin=FACETED_SEARCH&page=" + str(n))

    time.sleep(2)

    #find the connect button
    all_buttons = driver.find_elements_by_tag_name("button")
    connect_buttons = [btn for btn in all_buttons if btn.text == "Connect"]

    #loop through all connect buttons
    for btn in connect_buttons:
        driver.execute_script("arguments[0].click();", btn)

        time.sleep(2)

        #find and click the Send now button
        send = driver.find_element (By.XPATH, "//button[@aria-label = 'Send now']")
        driver.execute_script("arguments[0].click();", send)
        
        #if the contact has secrurity settings enabled, 
        #limiting adding to people they know, close the window and skip
        close_btn = driver.find_element (By.XPATH, "//button[@aria-label = 'Dismiss']")
        driver.execute_script("arguments[0].click();", close_btn)

        time.sleep(2)