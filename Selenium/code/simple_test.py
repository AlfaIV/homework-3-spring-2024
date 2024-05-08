from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest
import time
from secrets import login, password
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://ads.vk.com")
        login_button = driver.find_element(By.CLASS_NAME,"ButtonCabinet_primary__LCfol")
        login_button.click()
        
        try:
            loginForm = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "login"))
            )
            loginForm.send_keys(login)
            loginSubmit = driver.find_element(By.CLASS_NAME,"vkuiButton__content")
            loginSubmit.click()
        except:
            print('login falls')

        try:
            passwordForm = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "password"))
            )
            passwordForm.send_keys(password)
            passwordSubmit = driver.find_element(By.CLASS_NAME,"vkuiButton__content")
            passwordSubmit.click()
        except:
            print('pws falls')

    def tearDown(self):
        time.sleep(60)
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
