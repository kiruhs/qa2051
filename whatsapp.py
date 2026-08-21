from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://web.whatsapp.com/")
input("Press Enter after scanning QR code")
sleep(5)

driver.find_element(By.XPATH,
                    '//*[@id="app"]/div/div/div[3]/div/div[3]/header/header/div/span/div/div[1]/span/div/button/div/div/div[1]/span').click()

sleep(1.5)
search = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[3]/div/div[2]/div[1]/div/span/div/span/div/div/div[1]/div/div/div/div/div/div[2]/input')
search.send_keys('0545773947', Keys.ENTER)
sleep(1)
message = driver.switch_to.active_element
message.send_keys("Hello, friend!", Keys.ENTER)
sleep(3)