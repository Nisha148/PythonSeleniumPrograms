import pytest
import allure
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

@allure.title("Actions")
@allure.description("Performing keyboard actions")
def test_keyboard_actions():
    driver=webdriver.Chrome()
    driver.get("https://awesomeqa.com/practice.html")
    first_name=driver.find_element(By.XPATH,"//input[@name='firstname']")
    action_keys=ActionChains(driver=driver)
    action_keys.key_down(Keys.SHIFT).send_keys_to_element(first_name,"the testing academy")
    action_keys.key_up(Keys.SHIFT).perform()
    time.sleep(3)
    driver.quit()
