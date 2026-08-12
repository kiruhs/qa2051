from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.maximize_window()
# url = "https://www.wikipedia.org/"
# url = "http://www.google.com/"
# url = "https://www.walla.co.il/"
# browser.get(url)
# sleep(2)
# browser.back()
# sleep(3)
# browser.forward()
# sleep(3)
# cur_url = browser.current_url
# assert cur_url == url, "The URL is wrong"
# print(browser.page_source)

# search = browser.find_element(By.ID, "APjFqb")
# search.click()
# search.send_keys("python")
# sleep(2)
# # browser.find_element(By.CLASS_NAME, "gNO89b").click()
# search.send_keys(Keys.ENTER)
# sleep(5)

url = "https://www.walla.co.il/"
browser.get(url)
sleep(2)
browser.find_element(By.XPATH, "/html/body/div[5]/div/div/header/div[1]/div[1]/div[3]/div[3]/a/div[2]/div[1]").click()
sleep(5)