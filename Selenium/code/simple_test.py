# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# import unittest
# import time
# from secrets import login, password
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# class PythonOrgSearch(unittest.TestCase):

#     def setUp(self):
#         self.driver = webdriver.Firefox()

#     def test_login(self):
#         driver = self.driver
#         driver.get("http://ads.vk.com")
#         login_button = driver.find_element(By.CLASS_NAME,"ButtonCabinet_primary__LCfol")
#         login_button.click()
        
#         # try:
#         #     loginForm = WebDriverWait(driver, 10).until(
#         #         EC.presence_of_element_located((By.NAME, "login"))
#         #     )
#         #     loginForm.send_keys(login)
#         #     loginSubmit = driver.find_element(By.CLASS_NAME,"vkuiButton__content")
#         #     loginSubmit.click()
#         # except:
#         #     print('login falls')

#         # try:
#         #     passwordForm = WebDriverWait(driver, 10).until(
#         #         EC.presence_of_element_located((By.NAME, "password"))
#         #     )
#         #     passwordForm.send_keys(password)
#         #     passwordSubmit = driver.find_element(By.CLASS_NAME,"vkuiButton__content")
#         #     passwordSubmit.click()
#         # except:
#         #     print('pws falls')

#         try:
#             OAuthBut = WebDriverWait(driver, 10).until(
#                 EC.presence_of_element_located((By.XPATH, ".//button[@data-test-id='oAuthService_mail_ru']"))
#             )
#             OAuthBut.click()
#         except:
#             print('oauth falls')

#         try:
#             OAuthLogin = WebDriverWait(driver, 10).until(
#                 EC.presence_of_element_located((By.NAME, "username"))
#             )
#             OAuthLogin.send_keys(login)
#             OAuthSubmitBut = driver.find_element(By.CLASS_NAME, "submit-button-wrap")
#             OAuthSubmitBut.click()
#         except:
#             print('oauth login falls')

#         try:
#             OAuthLogin = WebDriverWait(driver, 10).until(
#                 EC.presence_of_element_located((By.NAME, "password"))
#             )
#             OAuthLogin.send_keys(password)
#             OAuthSubmitBut = driver.find_element(By.CLASS_NAME, "submit-button-wrap")
#             OAuthSubmitBut.click()
#         except:
#             print('oauth password falls')

#         self.assertEqual(driver.current_url, 'https://ads.vk.com/hq/dashboard')


#     def test_nav_menu(self):
#         driver = self.driver
#         VkIco = driver.find_element(By.CLASS_NAME, "header_left__cv9bp")
#         VkIco.click()
#         self.assertEqual(driver.current_url, 'https://ads.vk.com/hq/dashboard')

#     def tearDown(self):
#         time.sleep(30)
#         self.driver.quit()

# if __name__ == "__main__":
#     unittest.main()
