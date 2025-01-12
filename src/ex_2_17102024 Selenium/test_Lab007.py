from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By

def test_verify_katalon_url_title():
    driver=webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
   # < a
   # id = "btn-make-appointment"
   # href = "./profile.php#login"

    #class ="btn btn-dark btn-lg" >
   # Make Appointment
   # < / a >
    make_my_appointment=driver.find_element(By.ID,"btn-make-appointment")
    make_my_appointment.click()
    assert driver.current_url=="https://katalon-demo-cura.herokuapp.com/profile.php#login"
    driver.quit()