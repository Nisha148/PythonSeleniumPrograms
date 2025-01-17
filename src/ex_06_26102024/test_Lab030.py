import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import allure
import pytest

@allure.title("Webtable")
@allure.description("verifying webtable")
def test_webtable():
    driver=webdriver.Chrome()
    driver.get("https://awesomeqa.com/webtable1.html")
    #// table[ @ summary = "Sample Table"] / tbody /tr
    table=driver.find_element(By.XPATH,"// table[ @ summary = 'Sample Table'] / tbody")
    row_table=table.find_elements(By.TAG_NAME,"tr")


    for row in row_table:
        column_table = driver.find_elements(By.TAG_NAME,"td")
        for e in column_table:
            print(e.text)


