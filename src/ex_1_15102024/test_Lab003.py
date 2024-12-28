from numba.cuda.cudadrv.driver import driver
from selenium import webdriver

def test_verify_katalon_url_title():
    driver=webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    page_source_data=driver.page_source
    assert "CURA Healthcare Service" in page_source_data
    driver.quit()