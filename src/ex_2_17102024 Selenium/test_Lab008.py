
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By

def test_verify_katalon_url_title():
    driver=webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    make_my_appointment=driver.find_element(By.ID,"btn-make-appointment")
    make_my_appointment.click()
    assert driver.current_url=="https://katalon-demo-cura.herokuapp.com/profile.php#login"
    #< input
    #type = "text"
    #class ="form-control"
    #id="txt-username"
    # #name="username"
    # #placeholder="Username"
    # value=""
    # autocomplete="off" >
    username=driver.find_element(By.ID,"txt-username")
    username.send_keys("John Doe")
    #< input
    #type = "password"
    #class ="form-control"
    # id="txt-password"
    # name="password"
    # placeholder="Password"
    # value=""
    # autocomplete="off" >
    password=driver.find_element(By.ID,"txt-password")
    password.send_keys("ThisIsNotAPassword")
    # < button
    #id = "btn-login"
    #type = "submit"
    #class ="btn btn-default" >
    # Login < / button >
    Login=driver.find_element(By.ID,"btn-login")
    Login.click()
    assert driver.current_url=="https://katalon-demo-cura.herokuapp.com/#appointment"
    time.sleep(10)
    driver.quit()