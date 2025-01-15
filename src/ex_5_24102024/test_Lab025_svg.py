import allure
import pytest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

@allure.title("SVG")
@allure.description("verify")
def test_svg():
    driver=webdriver.Chrome()
    driver.get("https://www.flipkart.com/")
    #< input
    #class ="Pke_EE"
    # type="text"
    # title="Search for Products, Brands and More"
    # name="q"
    # autocomplete="off"
    # placeholder="Search for Products,
    # Brands and More" value="" >
    search_box=driver.find_element(By.NAME,"q" )
    search_box.send_keys("macmini")
    list_svg=driver.find_elements(By.XPATH,"//*[name()='svg']")
    list_svg[0].click()
    time.sleep(2)