from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from pprint import pprint
import csv



driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.globes.co.il/portal/instrument.aspx?instrumentId=60&mode=trades")
sleep(5)

deals = driver.find_element(By.XPATH, '//*[@id="divTrade"]/table[2]')
# //*[@id="tableTop"]/following::table[1]
# print(deals.text)

data = []

for row in deals.find_elements(By.TAG_NAME, 'tr'):
    cols = row.find_elements(By.TAG_NAME, "td")
    data.append({f'column{c+1}': cols[c].text for c in range(len(cols))})
    # dct = {}
    # for c in range(len(cols)):
    #     dct[c+1] = c
    # data.append(dct)
# pprint(data)

titles= driver.find_element(By.XPATH, '//*[@id="tableTop"]')
data1 = []
row = titles.find_element(By.TAG_NAME, 'tr')
cols = row.find_elements(By.TAG_NAME, 'th')
data1.append({f'column{c+1}': cols[c].text for c in range(len(cols))})

for rows in data:
    data1.append(rows)

with open("globes.csv", 'w', newline='', encoding='utf8') as file:
    my_fields = [f'column{c+1}' for c in range(len(cols))]
    writer = csv.DictWriter(file, fieldnames=my_fields)
    writer.writerows(data1)
