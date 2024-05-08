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
        finally:
            driver.quit()

        try:
            loginForm = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "login"))
            )
            loginForm.send_keys(login)
            loginSubmit = driver.find_element(By.CLASS_NAME,"vkuiButton__content")
            loginSubmit.click()
        finally:
            driver.quit()
        
        # self.assertIn("Python", driver.title)
        # elem = driver.find_element(By.NAME,"q")
        # elem.send_keys("pycon")
        # assert "No results found." not in driver.page_source
        # elem.send_keys(Keys.RETURN)

    # def tearDown(self):
    #     time.sleep(5)
    #     self.driver.close()

if __name__ == "__main__":
    unittest.main()