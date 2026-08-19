from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait as WW
from selenium.webdriver.support import expected_conditions as EC


# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--headless")

# driver2 = webdriver.Edge()
# driver2.maximize_window()
# driver2.get("https://www.yahoo.com")
# sleep(5)
# driver = webdriver.Chrome(options=chrome_options)
# driver.maximize_window()
#
# driver.get("https://www.youtube.com/watch?v=voO12-fh-eU")
#
# # sleep(5)
# try:
#     elem = WW(driver, timeout=10).until(
#         EC.presence_of_element_located((By.XPATH, '//*[@id="title"]/h1/yt-formatted-string'))
#     )
# except NoSuchElementException:
#     print("sorry, no such element on this site")
#     quit(0)
#
#
#
# body = driver.find_element(By.TAG_NAME, 'body')
# while True:
#     try:
#         body.send_keys(Keys.ARROW_DOWN)
#         cnt =  driver.find_element(By.XPATH, '//h2[@id="count"]/yt-formatted-string/span[1]')
#         print(cnt.text)
#         break
#     except NoSuchElementException:
#         pass
#
# driver.execute_script("window.open('https://google.com', '_blank')")
# sleep(2)
# driver.switch_to.window(driver.window_handles[1])
# sleep(1)
# search = driver.find_element(By.ID, 'APjFqb')
# sleep(0.3)
# search.send_keys("selenium", Keys.ENTER)
# sleep(3)
#
# driver.execute_script("window.open('https://cnn.com', '_blank')")
# sleep(2)
#
# for win in driver.window_handles:
#     driver.switch_to.window(win)
#     sleep(2)