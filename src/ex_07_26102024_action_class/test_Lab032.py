import pytest
import allure
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains,ActionBuilder
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.actions.mouse_button import MouseButton

@allure.title("Actions")
@allure.description("Performing mouse actions")
def test_keyboard_actions():
    driver=webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")
    # For Click for result page
    #< a
    #href = "resultPage.html"
    #id = "click" > Click
    #for Results Page </ a >
    click_result=driver.find_element(By.ID,'click')
    click_result.click()
    time.sleep(2)
    actions=ActionBuilder(driver=driver)
    actions.pointer_action.pointer_up(MouseButton.BACK)
    actions.perform()
    time.sleep(2)

