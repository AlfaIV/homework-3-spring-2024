import pytest
from secrets import login, password
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope='session')
def baseSetup():
    driver = webdriver.Firefox()
    driver.get("http://ads.vk.com")
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def login(driver):
        login_button = driver.find_element(By.CLASS_NAME,"ButtonCabinet_primary__LCfol")
        login_button.click()
        
        # try:
        #     loginForm = WebDriverWait(driver, 10).until(
        #         EC.presence_of_element_located((By.NAME, "login"))
        #     )
        #     loginForm.send_keys(login)
        #     loginSubmit = driver.find_element(By.CLASS_NAME,"vkuiButton__content")
        #     loginSubmit.click()
        # except:
        #     print('login falls')

        # try:
        #     passwordForm = WebDriverWait(driver, 10).until(
        #         EC.presence_of_element_located((By.NAME, "password"))
        #     )
        #     passwordForm.send_keys(password)
        #     passwordSubmit = driver.find_element(By.CLASS_NAME,"vkuiButton__content")
        #     passwordSubmit.click()
        # except:
        #     print('pws falls')

        try:
            OAuthBut = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, ".//button[@data-test-id='oAuthService_mail_ru']"))
            )
            OAuthBut.click()
        except:
            print('oauth falls')

        try:
            OAuthLogin = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "username"))
            )
            OAuthLogin.send_keys(login)
            OAuthSubmitBut = driver.find_element(By.CLASS_NAME, "submit-button-wrap")
            OAuthSubmitBut.click()
        except:
            print('oauth login falls')

        try:
            OAuthLogin = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "password"))
            )
            OAuthLogin.send_keys(password)
            OAuthSubmitBut = driver.find_element(By.CLASS_NAME, "submit-button-wrap")
            OAuthSubmitBut.click()
        except:
            print('oauth password falls')