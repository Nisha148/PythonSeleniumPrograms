from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import allure
import time

@allure.description("verifying anchor tag")
def test_anchor_tag():
    driver=webdriver.Chrome()
    driver.get("https://awesomeqa.com/ui/index.php?route=account/register")
    #< input
    #type = "text"
    #name = "firstname"
    #value = ""
    #placeholder = "First Name"
    #id = "input-firstname"
    #class ="form-control" >
    first_name=driver.find_element(By.XPATH,"//input[@placeholder='First Name']")
    first_name.send_keys("Ankitha")
    #< input
    #type = "text"
    #name = "lastname"
    #value = ""
    #placeholder = "Last Name"
    #id = "input-lastname"
    #class ="form-control" >
    last_name = driver.find_element(By.XPATH, "//input[@placeholder='Last Name']")
    last_name.send_keys("Gowda")
    #< input
    #type = "email"
    #name = "email"
    #value = ""
    #placeholder = "E-Mail"
    #id = "input-email"
    #class ="form-control" >
    email_id=driver.find_element(By.XPATH,"//input[@name = 'email']")
    email_id.send_keys("anit123@gmail.com")
    #< input
    #type = "tel"
    #name = "telephone"
    #value = ""
    #placeholder = "Telephone"
    #id = "input-telephone"
    #class ="form-control" >
    telephone_nu=driver.find_element(By.XPATH,"//input[@id = 'input-telephone']")
    telephone_nu.send_keys("1234567890")
    #< input
    #type = "password"
    #name = "password"
    #value = ""
    #placeholder = "Password"
    #id = "input-password"
    #class ="form-control" >
    password=driver.find_element(By.XPATH,"//input[@placeholder = 'Password']")
    password.send_keys("ani123456")
    #< input
    #type = "password"
    #name = "confirm"
    #value = ""
    #placeholder = "Password Confirm"
    #id = "input-confirm"
    #class ="form-control" >
    confirm_password=driver.find_element(By.XPATH,"//input[@id = 'input-confirm']")
    confirm_password.send_keys("ani123456")
    #< label
    #class ="radio-inline" >
    #< input
    #type = "radio"
    #name = "newsletter"
    #value = "0"
    #checked = "checked" >
    #No < / label >
    subscribe_button=driver.find_element(By.XPATH,"//input[@name = 'newsletter']")
    subscribe_button.click()
    #< input
    #type = "checkbox"
    #name = "agree"
    #value = "1" >
    check_box=driver.find_element(By.XPATH,"//input[@name = 'agree']")
    check_box.click()
    #< input
    #type = "submit"
    #value = "Continue"
    #class ="btn btn-primary" >
    continue_btn=driver.find_element(By.XPATH,"//input[@class ='btn btn-primary']")
    continue_btn.click()
    time.sleep(3)
    source_page=driver.page_source
    assert "Your Account Has Been Created!" in source_page
