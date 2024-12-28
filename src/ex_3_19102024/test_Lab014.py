from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import allure
import time

@allure.description("verifying anchor tag")
def test_anchor_tag():
    driver=webdriver.Chrome()
    driver.get("https://awesomeqa.com/ui/index.php?route=account/register")
    #< button
    #type = "submit"
    # id = "js-login-btn"
    # class ="btn btn--positive btn--inverted W(100%) H(48px) Fz(16px)"
    # onclick="login.login(event)"
    # data-qa="sibequkica"
