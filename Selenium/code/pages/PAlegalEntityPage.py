from pages.base_page import BasePage
from conftest import *

from selenium.webdriver.common.by import By

class PAlegalEntityLocators:
    LOCATOR_VK_ICO = (By.CLASS_NAME, "header_left__cv9bp")
    LOCATOR_USER_NAME = (By.CLASS_NAME, "AccountSwitch_changeAccountButton__o5T9V")
    LOCATOR_BELL = (By.CLASS_NAME, "header_bellNotifications__vAHeR")
    LOCATOR_USER_ICO = (By.CLASS_NAME, "userMenu_avatar__oCUFq")
    LOCATOR_LOG_OUT = (By.XPATH, "//div[@class='vkuiPopover__in']/div[1]/div[@role='button']")

class PAlegalEntityTopNavbar(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)

    def click_to_VK_ico(self):
        self.click_to_element(PAlegalEntityLocators.LOCATOR_VK_ICO)

    def click_to_user_name(self):
        self.click_to_element(PAlegalEntityLocators.LOCATOR_USER_NAME)

    # def check_to_user_name(self):
        #  self.click_to_element(PAlegalEntityLocators.LOCATOR_USER_NAME)

    def click_to_bell(self):
        self.click_to_element(PAlegalEntityLocators.LOCATOR_BELL)
    
    def check_bell_text_field(self):
        assert self.get_text((By.XPATH, ".//div[contains(@class, 'vkuiHeader__main')]/h2/span[1]/span[1]")) == "Уведомления"
        assert self.get_text((By.XPATH, ".//div[contains(@class, 'EmptyPlaceholder_wrapper__8LcAC')]/div[1]/h2")) == "Нет уведомлений"
        assert self.get_text((By.XPATH, ".//h4/span[1]/span[1]")) == "Как только у вас появятся уведомления, они отобразятся здесь"

    def click_to_user_ico(self):
        self.click_to_element(PAlegalEntityLocators.LOCATOR_USER_ICO)

    def user_log_out(self):
        self.click_to_user_ico()
        self.click_to_element(PAlegalEntityLocators.LOCATOR_LOG_OUT)