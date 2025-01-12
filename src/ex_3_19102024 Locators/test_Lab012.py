from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import allure
import time

@allure.description("verifying anchor tag")
def test_anchor_tag():
    driver=webdriver.Chrome()
    driver.get("https://app.vwo.com/")
    all_buttons=driver.find_elements(By.TAG_NAME,"buttons")
    print(len(all_buttons))
    for i in all_buttons:
        print(i.text)

    all_links = driver.find_elements(By.TAG_NAME, "a")
    print(len(all_links))
    for i in all_links:
        print(i.text)

        