from selenium import webdriver
from selenium.webdriver.common.by import By
import allure
import pytest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import (ElementNotVisibleException,ElementNotSelectableException)
from selenium.webdriver.support import expected_conditions as EC


@allure.title("Alerts")
@allure.description("Handling a confirm JS alerts")
def test_confirm_js_alert():
    driver=webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    driver.maximize_window()
    #< button
    #onclick = "jsConfirm()" > Click
    #for JS Confirm </ button >
    input_box=driver.find_element(By.XPATH,'//button[@onclick="jsConfirm()"]')
    input_box.click()
    WebDriverWait(driver=driver,timeout=2).until(EC.alert_is_present())
    alert=driver.switch_to.alert
    #alert.accept()
    alert.dismiss()
    #< p
    #id = "result"
    #style = "color:green" > You
    #clicked: Ok < / p >
    result=driver.find_element(By.ID,"result").text
    #assert result=="You clicked: Ok"
    assert result=="You clicked: Cancel"
    time.sleep(2)
