from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import allure
import time

@allure.title("Search for Macmini")
@allure.description("Search all the Macmini from ebay")
def test_anchor_tag():
    driver=webdriver.Chrome()
    driver.get("https://www.ebay.com/b/Desktops-All-In-One-Computers/171957/bn_1643067")
    #<input type="text"
    #class="gh-tb ui-autocomplete-input"
    #aria-autocomplete="list"
    #aria-expanded="false"
    #size="50"
    # maxlength="300"
    # aria-label="Search for anything"
    # placeholder="Search for anything"
    # id="gh-ac" name="_nkw"
    # autocapitalize="off"
    # autocorrect="off"
    # spellcheck="false"
    # autocomplete="off"
    # value="macmini"
    # aria-haspopup="true"
    # role="combobox"
    # aria-owns="ui-id-1">
    input_box=driver.find_element(By.XPATH,"//input[@placeholder='Search for anything']")
    input_box.send_keys("macmini")
    #< input
    #type = "submit"
    #class ="btn btn-prim gh-spr"
    # id="gh-btn"
    # value="Search"
    # form="gh-f" >
    search_botton=driver.find_element(By.CSS_SELECTOR,"input[value='Search']")
    search_botton.click()
    #< span
    #role = "heading"
    #aria - level = "3" >
    # <!--F  # f_0-->
    # <span class="LIGHT_HIGHLIGHT">New listing</span>
    # <!--F/--><!--F#f_0-->
    # Apple Mac mini (256GB SSD, M1, 8GB)
    # Silver - MGNR3B/A (November, 2020)<!--F/-->
    # </span>
    list_of_items=driver.find_elements(By.CSS_SELECTOR,".s-item__title")
    list_of_price=driver.find_elements(By.CSS_SELECTOR,".s-item__price")

    for title,price in zip(list_of_items,list_of_price):
        print(title.text,price.text)

    driver.quit()
