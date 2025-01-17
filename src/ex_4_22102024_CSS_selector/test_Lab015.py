from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import allure
import time

@allure.description("verifying anchor tag")
def test_anchor_tag():
    driver=webdriver.Chrome()
    driver.get("https://awesomeqa.com/ui/index.php?route=account/register")
    first_name=driver.find_element(By.CSS_SELECTOR,"input[placeholder='First Name']")
    first_name.send_keys("Ankitha")