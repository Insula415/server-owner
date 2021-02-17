import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
from secrets import *

quest = input("Have you entered your username and password in the secrets file? ")
opt = ["yes", "y"]
if quest.lower() in opt:
    server = input("Enter a Discord server URL: ")

else:
    username = input("Discord email or phone number: ")
    password = input("Enter password: ")
    server = input("Enter a Discord server URL: ")


a = requests.get(server)
soup = BeautifulSoup(a.text, features="html.parser")

driver = webdriver.Chrome()
driver.get(server)

print("Logging into Discord...")
try: 
    driver.find_element_by_name("email").send_keys(username) #entering username
    sleep(1)
    driver.find_element_by_name("password").send_keys(password) #entering password
    sleep(1)
    driver.find_element_by_xpath("/html/body/div/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/button[2]").click() #clicking login button
    print("Login successful")
except:
    print("Login failed")
    print("Check you have entered the correct credentials")
    exit()

try:
    ServerName = soup.find('h1', {'class':'name-1jkAdW'})
    print("Server name:",ServerName)
except:
    print("Couldn't locate server name")

try:
    for crown in soup.find_all('svg', {'aria-label':'Server Owner'}):
        for name in soup.find_all('div', {'class':'name-uJV0GL'}):
            print("Server owner:",name)
        
except:
    print("Server owner could not be found")
    print("Have you entered a correct server URL? ")
    exit()

