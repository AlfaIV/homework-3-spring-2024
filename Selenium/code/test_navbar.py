from conftest import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from secrets import USER_NAME

def testVkIcon(login):
        driver = login
        VkIco = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "header_left__cv9bp"))
        )
        VkIco.click()
        assert driver.current_url == 'https://ads.vk.com/hq/dashboard'

def testLK(login):
        driver = login
        nameIco = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "AccountSwitch_changeAccountButton__o5T9V"))
        )
        nameIco.click()
        dropBox = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "AccountSwitch_accountsDropdown__4uPNG"))
        )
        assert dropBox.find_element(By.TAG_NAME, "a").text == 'Все кабинеты'
        assert dropBox.find_element(By.XPATH, ".//div[contains(@class, 'vkuiSimpleCell__content')]/span[1]").text == USER_NAME