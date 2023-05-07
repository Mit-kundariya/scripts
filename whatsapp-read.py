from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe')
 
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)
input("enter..")

for i in range(2):
    content = driver.find_element_by_css_selector('.chat.unread')
    var1 = content.text
    print(var1)
    content.click()
    list1=var1.split('\n')
    target = list1[0].strip()
    if 'Hello' in var1 or 'nai' in var1:
        target = '"'+target+'"'
        string = "HI, Mit's bot here..!!!"
         
        x_arg = '//span[contains(@title,' + target + ')]'
        group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
        group_title.click()

        inp_xpath = '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
        input_box = wait.until(EC.presence_of_element_located((By.XPATH, inp_xpath)))
        input_box.send_keys(string + Keys.ENTER)
        
        print('msg sent to :' +target)
        time.sleep(2)