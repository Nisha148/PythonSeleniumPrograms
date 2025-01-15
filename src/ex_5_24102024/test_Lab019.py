import allure
import pytest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import (ElementNotVisibleException,ElementNotSelectableException)
from selenium.webdriver.support import expected_conditions as EC

@allure.title("Alerts")
@allure.description("Handling a Normal JS alerts")
def test_normal_js_alert():
    driver=webdriver.Chrome()
    driver.get("https://awesomeqa.com/practice.html")
    #< input
    #id = "sex-1"
    #name = "sex"
    #style = "font-size: 14px;
    # margin-left:
    # 0px; margin-right: 0px; margin-top: 0px; padding: 0px; vertical-align: baseline;"
    #type = "radio"
    #value = "Female" >
    gender_button=driver.find_element(By.ID,"sex-1")
    gender_button.click()
    #< input
    #id = "profession-1"
    #name = "profession"
    #style = "font-size: 14px; margin: 0px; padding: 0px; vertical-align: baseline;"
    #type = "checkbox"
    #value = "Automation Tester" >
    profession=driver.find_element(By.ID,"profession-1")
    profession.click()
    #< input
    #id = "exp-2"
    #name = "exp"
    #style = "font-size: 14px; margin-left: 0px; margin-right: 0px;
    # margin-top: 0px; padding: 0px; vertical-align: baseline;"
    #type = "radio"
    #value = "3" >
    years_of_experience=driver.find_element(By.ID,"exp-2")
    years_of_experience.click()
    time.sleep(5)