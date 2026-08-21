from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
# import json
import pickle

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://ok.ru")
# sleep(3)
# sleep(30)
# cookies = driver.get_cookies()
# with open("ok_cookies.pkl", 'wb') as file:
#     json.dump(cookies, file, indent=4)
#     pickle.dump(cookies, file)
# print("Cookies saved to the file")
with open("ok_cookies.pkl", 'rb') as file:
    cookies = pickle.load(file)

for cookie in cookies:
    print(cookie)
    driver.add_cookie(cookie)

driver.refresh()
sleep(10)