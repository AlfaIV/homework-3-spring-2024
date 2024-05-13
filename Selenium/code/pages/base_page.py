
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")
    
    def click_to_element(self, locator, time=10):
        return self.find_element(locator, time).click()
    
    def go_to_page(self, page_url):
        return self.driver.get(page_url)

    def get_current_url(self):
        return self.driver.current_url
    
    def set(self, locator, value):
        self.find_element(locator).clear()
        self.find_element(locator).send_keys(value)

    def get_text(self, locator):
        return self.find_element(locator).text

    def get_title(self):
        return self.driver.title
    
    def change_tab(self, window):
        return self.driver.switch_to.window(window)
    
    def switch_to_iframe(self, iframe):
        return self.driver.switch_to.frame(iframe)

    def close_current_tab(self):
        return self.driver.close()

    def get_tab(self, tab_num):
        return self.driver.window_handles[tab_num]