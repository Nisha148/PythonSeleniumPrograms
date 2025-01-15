from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import allure
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


@allure.description("Verifying")
def test_verify():
    driver=webdriver.Chrome()
    driver.get("https://app.vwo.com/")
    try:
        element=driver.find_element(By.ID,"this_id_doesnt_exists")
    except NoSuchElementException as nsee:
        print(nsee.msg)

    time.sleep(2)