import allure
import pytest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException

@allure.title("SVG")
@allure.description("verify")
def test_svg():
    driver=webdriver.Chrome()
    driver.get("https://www.amcharts.com/svg-maps/?map=india")

    list_svg=driver.find_elements(By.XPATH,"//*[name()='svg']/*[name()='g'][7]/*[name()='g']/*[name()='g']/*[name()='path']")
    #stroke - opacity = "0.5"
    #class ="" role="menuitem" aria-label="Andaman and Nicobar Islands  " >
    for states in list_svg:
        print(states.get_attribute("aria-label"))
    try:
        if "Tripura" in states.get_attribute("aria-label"):
            states.click()
    except ElementClickInterceptedException as ecie:
          print(ecie.msg)
        
    time.sleep(5)