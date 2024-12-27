from numba.cuda.cudadrv.driver import driver
from selenium import webdriver

def test_verify_katalon_url_title():
    driver=webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    print(driver.title)
    assert driver.title=="CURA Healthcare Service"