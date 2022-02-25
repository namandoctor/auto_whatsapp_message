from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from configparser import ConfigParser
import random
 
##  Initialize Config Parser and read values    ##
config_obj = ConfigParser()
config_obj.read("config.ini", encoding='utf-8')

misc = config_obj["miscellaneous"]
person = config_obj["person"]
expression_list = ['I love you','I miss you','Watchadoin?']

options = webdriver.ChromeOptions()
# options.add_argument('--headless')  #runs in background
options.add_argument("--user-data-dir=" + misc["user_data_dir"])
options.add_argument("--profile-directory=" + misc["chrome_profile"])
driver = webdriver.Chrome(executable_path = misc["chrome_driver_path"], options=options)
driver.get(misc["whatsapp"])

# driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[3]/div/header/div[2]/div/span/div[2]/div").click()
WebDriverWait(driver, 20).until(expected_conditions.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div[1]/div[3]/div/header/div[2]/div/span/div[2]/div"))).click()
driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[2]/div[1]/span/div[1]/span/div[1]/div[1]/div/label/div/div[2]").send_keys(person["name"])
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[2]/div[1]/span/div[1]/span/div[1]/div[2]/div/div/div/div[2]/div").click()                  
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]").send_keys(random.choice(expression_list) + Keys.ENTER)
time.sleep(4)