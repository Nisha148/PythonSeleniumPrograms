from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def test_verify_katalon_url_title():
    driver=webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    assert driver.current_url=="https://katalon-demo-cura.herokuapp.com/"
    driver.quit()

def test_edge():
    driver=webdriver.Edge()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    assert driver.current_url=="https://katalon-demo-cura.herokuapp.com/"
    driver.quit()

def test_fire():
    driver=webdriver.Firefox()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    assert driver.current_url=="https://katalon-demo-cura.herokuapp.com/"
    driver.quit()