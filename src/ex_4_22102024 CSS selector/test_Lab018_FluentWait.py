from selenium import webdriver
from selenium.webdriver.common.by import By
import allure
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import (ElementNotVisibleException,ElementNotSelectableException)
from selenium.webdriver.support import expected_conditions as EC


@allure.description("Verifying")
def test_verify():
    driver=webdriver.Chrome()
    driver.get("https://app.vwo.com/")

    #< input
    #type = "email"
    #class ="text-input W(100%)"
    # name="username"
    # id="login-username"
    # data-qa="hocewoqisi" >
    username=driver.find_element(By.ID,"login-username")
    username.send_keys("abcdef@gmail.com")
    #< input
    #type = "password"
    #class ="text-input W(100%)"
    # name="password"
    # id="login-password"
    # data-qa="jobodapuxe"
    # data-gtm-form-interact-field-id="2" >
    password=driver.find_element(By.NAME,"password" )
    password.send_keys("abc12345")
    #< button
    #type = "submit"
    #id = "js-login-btn"
    #class ="btn btn--positive btn--inverted W(100%) H(48px) Fz(16px)"
    # onclick="login.login(event)"
    # data-qa="sibequkica" >
    sign_in=driver.find_element(By.ID,"js-login-btn")
    sign_in.click()

    #< div
    #class ="notification-box-description"
    # id="js-notification-box-msg"
    # data-qa="rixawilomi" >
    # Your email, password, IP address or location did not match
    # < / div >
    ignore_list=[ElementNotVisibleException,ElementNotSelectableException]
    WebDriverWait(driver=driver,poll_frequency=1,timeout=5,ignored_exceptions=ignore_list).until(EC.visibility_of_element_located((By.CLASS_NAME,"notification-box-description")))
    message=driver.find_element(By.CLASS_NAME,"notification-box-description" )
    assert message.text == "Your email, password, IP address or location did not match"

    driver.quit()


