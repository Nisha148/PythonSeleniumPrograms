from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import allure
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException


@allure.description("Verifying")
def test_verify():
    driver=webdriver.Chrome()
    driver.get("https://www.google.com/")
    #< textarea
    #class ="gLFyf"
    # aria-controls="Alh6id"
    # aria-owns="Alh6id"
    # autofocus="" title="Search"
    # value="" jsaction="paste:puy29d;"
    # aria-label="Search"
    # placeholder="" aria-autocomplete="both"
    # aria-expanded="false"
    # aria-haspopup="false"
    # autocapitalize="off"
    # autocomplete="off"
    # autocorrect="off"
    # id="APjFqb"
    # maxlength="2048"
    # name="q"
    # role="combobox"
    # rows="1"
    # spellcheck="false"
    # data-ved="0ahUKEwiQ5v3EzviKAxUgWUEAHWKBHVYQ39UDCA8" >
    # < / textarea >
    try:
        button=driver.find_element(By.NAME,"q")
        driver.refresh()
        button.send_keys("The Testing Academy")
    except StaleElementReferenceException as ste:
        print(ste)
        print("Stale element reference")

    time.sleep(2)


