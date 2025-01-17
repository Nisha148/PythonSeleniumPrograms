import pytest
import allure
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

@allure.title("Webtable")
@allure.description("verifying webtable")
def test_webtable():
    driver=webdriver.Chrome()
    driver.get("https://awesomeqa.com/webtable.html")
    #driver.maximize_window()
    #Row->  // table[ @ id = "customers"] / tbody / tr
    #Column->  //table[@id="customers"/tbody/tr[2]/td

    row=driver.find_elements(By.XPATH,"// table[ @ id = 'customers'] / tbody / tr")
    total_rows=len(row)
    print(total_rows)

    column=driver.find_elements(By.XPATH,"//table[@id='customers']/tbody/tr[2]/td")
    total_columns=len(column)
    print(total_columns)

    #// table[ @ id = "customers"] / tbody / tr[7] / td[1]
    #// table[ @ id = "customers"] / tbody / tr[
    # 7
    # ] / td[
    # 1
    # ]
    #(tr[7] - 7 is dynamic in nature
    #/
    #td[1])- 1 is dynamic in nature

    first_path="// table[ @ id = 'customers'] / tbody / tr["
    second_path="] / td["
    third_path="]"
    for i in range(2,total_rows+1):
        for j in range(1,total_columns+1):
            dynamic_path=f"{first_path}{i}{second_path}{j}{third_path}"
            data=driver.find_element(By.XPATH,dynamic_path).text
            if "Helen Bennett" in data:
                country_path=f"{dynamic_path}/following-sibling::td"
                country_text=driver.find_element(By.XPATH,country_path).text
                print(f"Helen Bennett is in {country_text}")

