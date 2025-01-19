import pytest
import allure
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains,ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.support import expected_conditions as EC

@allure.title("Spice jet")
@allure.description("verifying spice jet page")
def test_spice_jet():
    driver=webdriver.Chrome()
    driver.get("https://www.spicejet.com/")
    driver.maximize_window()
    from_tab=driver.find_element(By.XPATH,"//input[@class='css-1cwyjr8 r-homxoj r-ubezar r-10paoce r-13qz1uu']")
    actions=ActionChains(driver)

    actions.click(from_tab).send_keys("del").perform()
    time.sleep(4)
