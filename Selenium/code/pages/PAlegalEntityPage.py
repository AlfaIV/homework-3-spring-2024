from pages.base_page import BasePage
from conftest import *

from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

class PAlegalEntityLocators:
    LOCATOR_VK_ICO = (By.CLASS_NAME, "header_left__cv9bp")
    LOCATOR_USER_NAME = (By.CLASS_NAME, "AccountSwitch_changeAccountButton__o5T9V")
    LOCATOR_BELL = (By.CLASS_NAME, "header_bellNotifications__vAHeR")
    LOCATOR_USER_ICO = (By.CLASS_NAME, "userMenu_avatar__oCUFq")
    LOCATOR_LOG_OUT = (By.XPATH, "//div[@class='vkuiPopover__in']/div[1]/div[@role='button']")
    LOCATOR_BUDGET = (By.XPATH, "//a[@data-route='budget']/div[2]")
    LOCATOR_ACCESS_RIGHT = (By.XPATH, "//a[@data-route='access_rights']/div[2]")
    LOCATOR_ADD_MANAGER = (By.XPATH, "//div[@data-testid='add-manager']/div[2]")
    LOCATOR_CLIENTS = (By.XPATH, "//a[@data-route='dashboardV2']/div[2]")
    LOCATOR_HELP_BUTTON = (By.CLASS_NAME, "Hint_hintTrigger__ixYRu")

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

    def click_to_help_button(self):
        self.click_to_element(PAlegalEntityLocators.LOCATOR_HELP_BUTTON)
    
    def redirect_to_help_button(self, link_num):
        REDIRECT_LOCATOR = (By.XPATH, f".//div[@class='Tooltip_tooltipContainer__P1b-O']/section[1]/a[{link_num}]/div[1]")
        try:
            self.click_to_element(REDIRECT_LOCATOR)
        except TimeoutException:
            self.click_to_help_button()
            self.click_to_element(REDIRECT_LOCATOR)
        # self.driver.switch_to.window(self.driver.window_handles[-1])
        # # WebDriverWait(driver, 10).until(EC.url_to_be(driver.current_url))
        # self.driver.close()
        # self.driver.switch_to.window(self.driver.window_handles[0])

    def click_to_clients(self):
        self.click_to_element(PAlegalEntityLocators.LOCATOR_CLIENTS)

    def click_to_budget(self):
        self.click_to_element(PAlegalEntityLocators.LOCATOR_BUDGET)
    
    def specify_banking_details(self):
        self.click_to_element((By.XPATH, "//div[@class='vkuiPlaceholder__action']"))
        self.click_to_element((By.XPATH, "//div[@aria-label='Закрыть']"))

    def click_to_access_right(self):
        self.click_to_element(PAlegalEntityLocators.LOCATOR_ACCESS_RIGHT)
    
    def addManager(self, name, acc):
        self.click_to_element(PAlegalEntityLocators.LOCATOR_ADD_MANAGER)
        self.set((By.XPATH, ".//input[@name='managerFio']"), name)
        self.set((By.XPATH, ".//input[@name='managerEmail']"), acc)
        self.click_to_element((By.XPATH, ".//div[@class='ModalFooterSimple_container__rteom']/button[2]"))
        self.click_to_element((By.XPATH, "//div[@aria-label='Закрыть']"))
