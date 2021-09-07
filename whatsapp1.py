#program by Akshayjyoti Bordoloi
#version 1.0
#date: September 5, 2021
#WARNING: certain parts of the code have not been tested. All pyautogui coordinates are tested for 1080p display.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import pyautogui

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')

print("\n\nPlease MAXIMIZE the WhatsApp window before proceeding. Also make sure the Command Line window is NOT maximized...")
print("\n\nPlease DO NOT move the mouse cursor during the execution of the program...")
print("\n\nPlease ignore all warnings and enter number of people/groups...\n\n")

count = int(input('How many people/groups? '))
input('Enter anything after scanning QR code...')

#ctx = ssl.create_default_context()
#ctx.check_hostname = False
#ctx.verify_mode = ssl.CERT_NONE

pyautogui.moveTo(250, 500)          #valid for 1080p display only

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

tags = soup.findAll("span", {"class" : "_ccCW FqYAR i0jNr"})        #may need to be updated based on Chrome version

users = []
i = 0

while i < count:
    for tag in tags:
        name = tag.get("title")
        if name is None:
            continue
        users.append(name)
        i = i + 1
        if i == count:
            break
        if i % 18 == 0:                                              #may need to be updated based on Chrome version
            pyautogui.moveTo(800,10)                                 #valid for 1080p display only
            pyautogui.click()
            pyautogui.moveTo(250, 500)                               #valid for 1080p display only
            pyautogui.scroll(-2200)                                  #may need to be updated based on Chrome version
            time.sleep(1)
            html = driver.page_source
            soup = BeautifulSoup(html, "html.parser")
            tags = soup.findAll("span", {"class" : "_ccCW FqYAR i0jNr"})     #may need to be updated based on Chrome version
            break

msg = input('Enter your message: ')

#un-comment the following lines of code only after ensuring the code runs (try once without un-commenting).
#the next lines of code will result in mass messaging. Proceed at your own risk.

#for i in range(count):
#    try:
#        name = users[i]
#        user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
#        user.click()
#        msg_box = driver.find_element_by_xpath('//div[@data-tab = "9"]')       #may need to be updated based on Chrome version
#        msg_box.send_keys(msg)
#        button = driver.find_element_by_class_name('_4sWnG')                   #may need to be updated based on Chrome version
#        button.click()
#    except:
#        continue

print("\n\nThe message: " + msg + ", will be sent to the following people/groups:\n\n")
for user in users:
    print(user)

time.sleep(30)
driver.close()
