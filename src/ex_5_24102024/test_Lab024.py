from selenium import webdriver
from selenium.webdriver.common.by import By
import allure
import pytest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import (ElementNotVisibleException,ElementNotSelectableException)
from selenium.webdriver.support import expected_conditions as EC

@allure.title("Dropdown")
@allure.description("verify select")
def test_drop_down():
    driver=webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/dropdown")
    #< select
    #id = "dropdown" >
    #< option
    #value = ""
    #disabled = "disabled" > Please
    #select
    #an
    #option < / option >
    #< option
    #value = "1"
    #selected = "selected" > Option
    #1 < / option >
    #< option
    #value = "2" > Option
    #2 < / option >

    #< / select >
    drop_down=driver.find_element(By.ID, "dropdown")
    select=Select(drop_down)
    select.select_by_visible_text("Option 2")
    #select.select_by_index(2)
    time.sleep(2)