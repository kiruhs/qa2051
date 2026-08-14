from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://vinothqaacademy.com/alert-and-popup/")
sleep(6)
driver.find_element(By.NAME,'alertbox').click()
sleep(2)
alert_obj = driver.switch_to.alert
print(alert_obj.text)
alert_obj.accept()
sleep(3)

driver.find_element(By.NAME, 'confirmalertbox').click()
sleep(1)
confirm_obj = driver.switch_to.alert
print(confirm_obj.text)
confirm_obj.dismiss()
sleep(3)

driver.find_element(By.NAME, 'promptalertbox1234').click()
sleep(1)
prompt_obj = driver.switch_to.alert
print(prompt_obj.text)
prompt_obj.send_keys("Yes")
sleep(2)
prompt_obj.accept()
answer = driver.find_element(By.ID, 'demoone')
print(answer.text)
sleep(3)