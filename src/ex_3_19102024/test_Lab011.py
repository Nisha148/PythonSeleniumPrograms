from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import allure
import time

@allure.description("verifying anchor tag")
def test_anchor_tag():
    driver=webdriver.Chrome()
    driver.get("https://app.vwo.com/")
    #< a
    #href = "https://vwo.com/free-trial/?utm_medium=website&amp;utm_source=login-page&amp;utm_campaign=mof_eg_loginpage"
    #class ="text-link"
    # data-qa="bericafeqo"
    # >
    # Start a free trial
    # < / a >
    link=driver.find_element(By.LINK_TEXT,"Start a free trial")
    link.click()
    link = driver.find_element(By.PARTIAL_LINK_TEXT, "Start a free trial")
    link.click()
    assert driver.current_url=="https://vwo.com/free-trial/?utm_medium=website&utm_source=login-page&utm_campaign=mof_eg_loginpage"
    driver.quit()