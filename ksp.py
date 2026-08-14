from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()
url = "https://ksp.co.il/"
driver.get(url)
sleep(1)
driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div/button[1]").click()
sleep(1)
driver.find_element(By.XPATH, '//*[@id="site-header"]/div/div/div[1]/div[2]/button').click()
sleep(0.5)
first = driver.find_element(By.XPATH, '/html/body/main/div/div[3]/div[1]/div[3]/div/div/div[1]/div[2]/div/ul[1]/li[1]')
ActionChains(driver).move_to_element(first).perform()
sleep(3)
second = driver.find_element(By.XPATH, '/html/body/main/div/div[3]/div[1]/div[3]/div/div/div[1]/div[2]/div/ul[2]/li[3]')
ActionChains(driver).move_to_element(second).perform()
sleep(1)
third = driver.find_element(By.XPATH, '/html/body/main/div/div[3]/div[1]/div[3]/div/div/div[1]/div[2]/div/ul[3]/li[1]')
third.click()
sleep(4)
# item = driver.find_element(By.XPATH, '/html/body/main/div/div[3]/div[5]/div/div/div[2]/div[2]/div[3]/div/div[27]/div/div[1]/div[5]/h3/a')
page_height = driver.execute_script("return document.body.scrollHeight")
# print(page_height)
try:
    item = driver.find_element(By.XPATH,
                               '/html/body/main/div/div[3]/div[5]/div/div/div[2]/div[2]/div[3]/div/div[27]/div/div[1]/div[5]/h3/a')

    print("The item found")
    item.click()
except NoSuchElementException:
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        driver.implicitly_wait(3)
        sleep(3)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if page_height == new_height:
            break
        page_height = new_height


        try:
            item = driver.find_element(By.XPATH,
                               '/html/body/main/div/div[3]/div[5]/div/div/div[2]/div[2]/div[3]/div/div[27]/div/div[1]/div[5]/h3/a')
            print("The item found")
            sleep(2)
            # item.click()
            href = item.get_attribute("href")
            driver.get(href)
            sleep(3)
            break
        except NoSuchElementException:
            sleep(5)