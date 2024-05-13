import pytest
import time
from secrets import LOGIN_NAME, PASSWORD
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope='session')
def start():
    driver = webdriver.Firefox()
    driver.get("http://ads.vk.com")
    # driver.maximize_window()
    yield driver
    # time.sleep(30)
    driver.quit()

@pytest.fixture(scope='session')
def login(start):  
        driver = start
        login_button = driver.find_element(By.CLASS_NAME,"ButtonCabinet_primary__LCfol")
        login_button.click()
        
        OAuthBut = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, ".//button[@data-test-id='oAuthService_mail_ru']"))
        )
        OAuthBut.click()

        OAuthLogin = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
        OAuthLogin.send_keys(LOGIN_NAME)
        OAuthSubmitBut = driver.find_element(By.CLASS_NAME, "submit-button-wrap")
        OAuthSubmitBut.click()

        OAuthLogin = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "password"))
        )
        OAuthLogin.send_keys(PASSWORD)
        OAuthSubmitBut = driver.find_element(By.CLASS_NAME, "submit-button-wrap")
        OAuthSubmitBut.click()

        return driver