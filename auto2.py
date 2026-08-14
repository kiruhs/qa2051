from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common import exceptions
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome()
browser.maximize_window()
try:
    url = "https://www.walla.co.il/"
    browser.get(url)
    sleep(2)
    browser.find_element(By.XPATH, "/html/body/div[5]/div/div/header/div[1]/div[1]/div[3]/div[3]/a/div[2]/div[1]").click()
    sleep(3)
    browser.find_element(By.XPATH, "/html/body/app-root/div/div/div[1]/main/div[1]/app-login/div/div/section/fieldset/a").click()
    sleep(5)
    username = browser.find_element(By.ID, "username")
    username.send_keys("test27test")
    sleep(0.5)
    password = browser.find_element(By.XPATH, "/html/body/app-root/div/div/div[1]/main/div[1]/app-register/form/fieldset/section/ul/li[2]/app-input-password/form/div[1]/input")
    password.send_keys("Alr$3#lpfrd")
    sleep(3)
    phone = browser.find_element(By.ID, "postfix")
    phone.send_keys("054577394")
    day = Select(browser.find_element(By.XPATH,"/html/body/app-root/div/div/div[1]/main/div[1]/app-register/form/fieldset/section/ul/li[6]/app-date-picker/form/div[3]/select"))
    day.select_by_value("09")
    sleep(0.8)
    month = Select(browser.find_element(By.XPATH, "/html/body/app-root/div/div/div[1]/main/div[1]/app-register/form/fieldset/section/ul/li[6]/app-date-picker/form/div[2]/select"))
    month.select_by_value("07")
    sleep(0.5)
    year = Select(browser.find_element(By.XPATH, "/html/body/app-root/div/div/div[1]/main/div[1]/app-register/form/fieldset/section/ul/li[6]/app-date-picker/form/div[1]/select"))
    year.select_by_value("1998")
    sleep(5)
    error_el = browser.find_element(By.ID, "errorPhoneInvalid")
    if error_el.is_displayed():
        print("The test is failed")
    else:
        print("The test passed")

except exceptions.NoSuchElementException:
    print("Element not found")