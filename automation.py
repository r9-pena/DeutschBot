from logging import exception
from msilib.schema import Error
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import sys


# Check the box
def checkBox(driver):
    sleep(5)
    driver.find_element_by_xpath('//*[@id="xi-cb-1"]').click()
    sleep(2)
    driver.find_element_by_xpath('//*[@id="applicationForm:managedForm:proceed"]').click()
    sleep(5)


# Select Country
def fillForm(driver):
    select_country = Select(driver.find_element_by_name("sel_staat"))
    sleep(2)
    select_country.select_by_value('368')
    sleep(2)

    # Option 2
    select_opt1 = Select(driver.find_element_by_name("personenAnzahl_normal"))
    sleep(2)
    select_opt1.select_by_value('1')
    sleep(2)

    # Option 3
    select_opt1 = Select(driver.find_element_by_name("lebnBrMitFmly"))
    sleep(2)
    select_opt1.select_by_value('2')
    sleep(2)

    # Select Student option
    driver.find_element_by_xpath('//*[@id="xi-div-30"]/div[1]/label').click()
    sleep(2)
    driver.find_element_by_xpath('//*[@id="inner-368-0-1"]/div/div[1]/label').click()
    sleep(2)
    driver.find_element_by_xpath('//*[@id="SERVICEWAHL_DE368-0-1-3-305244"]').click()
    sleep(2)


def refresh(driver):
    # driver.find_element_by_xpath('//*[@id="applicationForm:managedForm:proceed"]').click()
    # sleep(10)
    while(driver.find_element_by_xpath('//*[@id="anton-remote-back"]')):
        driver.find_element_by_xpath('//*[@id="applicationForm:managedForm:proceed"]').click()
        sleep(10)


def main():    
    driver = webdriver.Chrome('C:/Users/Rick/Downloads/chromedriver_win32/chromedriver')
    driver.implicitly_wait(0.5)
    driver.get('https://otv.verwalt-berlin.de/ams/TerminBuchen/wizardng?sprachauswahl=en')

    input('Continue?')

    checkBox(driver)
    input('Continue?')    
    fillForm(driver)
    input('Continue?')
    refresh(driver)

    
if __name__ == '__main__':
    main()
