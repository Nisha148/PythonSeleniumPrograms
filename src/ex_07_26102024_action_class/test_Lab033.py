import pytest
import allure
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains, ActionBuilder
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.actions.mouse_button import MouseButton


@allure.title("Actions")
@allure.description("Performing mouse actions")
def test_keyboard_actions():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")

    #< div
    #id = "draggable"
    #class ="ui-widget-content ui-draggable ui-draggable-handle"
    # style="position: relative;
    # left: -4px; top: -7px;" >
    # Draggable < / div >
    box_button=driver.find_element(By.ID,"draggable")
    action=ActionChains(driver=driver)
    action.click_and_hold(on_element=box_button).perform()
    #< div
    #id = "droppable"

    #class ="ui-widget-header ui-droppable" > Droppable < / div >
    drop_button=driver.find_element(By.ID,"droppable")
    action_key=ActionChains(driver=driver)
    action_key.drag_and_drop(box_button,drop_button).perform()
    time.sleep(2)