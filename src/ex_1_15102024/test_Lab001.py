from selenium import webdriver
import pytest
import allure

@allure.title("Verify the Title of the webpage app.vwo.com")
def test_sample():
    driver= webdriver.Chrome()
    driver.get("https://sdet.live")