from conftest import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from secrets import USER_NAME
from selenium.common.exceptions import TimeoutException

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


def testBell(login):
        driver = login
        bellIco = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "header_bellNotifications__vAHeR"))
        )
        bellIco.click()
        bellDropbox = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "BellNotificationsContent_cardContent__Hkz1H"))
        )
        # print(bellDropbox.get_attribute("innerHTML"))
        assert bellDropbox.find_element(By.XPATH, ".//div[contains(@class, 'vkuiHeader__main')]/h2/span[1]/span[1]").text == "Уведомления"
        assert bellDropbox.find_element(By.XPATH, ".//div[contains(@class, 'EmptyPlaceholder_wrapper__8LcAC')]/div[1]/h2").text == "Нет уведомлений"
        assert bellDropbox.find_element(By.XPATH, ".//h4/span[1]/span[1]").text == "Как только у вас появятся уведомления, они отобразятся здесь"
        

def testUserAcc(login):
        driver = login
        userIco = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "userMenu_avatar__oCUFq"))
        )
        userIco.click()
        outButton = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='vkuiPopover__in']/div[1]/div[@role='button']"))
        )
        outButton.click()
        # print(bellDropbox.get_attribute("innerHTML"))
        assert driver.current_url == 'https://ads.vk.com/'

@pytest.fixture
def testHelpSideButton(login):
        driver = login
        helpButton = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "Hint_hintTrigger__ixYRu"))
        )
        helpButton.click()
        # тут проблема в том, что после срабатывания перехода на внешнюю ссылку необходимо 2 раза тыкать, иначе панель помощь не открывается
        try:
            listOfButtons = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "Tooltip_tooltipContainer__P1b-O"))
            )
        except TimeoutException:
            helpButton.click()
            listOfButtons = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "Tooltip_tooltipContainer__P1b-O"))
            )
        return listOfButtons

@pytest.mark.parametrize("link_num, link", [
        (1, 'https://ads.vk.com/cases'),
        (2, 'https://ads.vk.com/help/subcategories/agency'),
        (3, 'https://ads.vk.com/upvote')
        ])
def testRedirectSideButton(login, testHelpSideButton, link_num, link):
        driver = login
        companyKeysButton = WebDriverWait(testHelpSideButton, 10).until(
            EC.presence_of_element_located((By.XPATH, f".//section[1]/a[{link_num}]/div[1]"))
        )
        # companyKeysButton = testHelpSideButton.find_element(By.XPATH, f".//section[1]/a[{link_num}]/div[1]")
        companyKeysButton.click()
        
        driver.switch_to.window(driver.window_handles[-1])
        # WebDriverWait(driver, 10).until(EC.url_to_be(driver.current_url))

        # assert driver.current_url == link
        driver.close()
        driver.switch_to.window(driver.window_handles[0])

# def testCompanyKeysHelpSideButton(login, testHelpSideButton):
#         driver = login
#         companyKeysButton = testHelpSideButton.find_element(By.XPATH, ".//section[1]/a[1]/div[1]")
#         companyKeysButton.click()
#         assert driver.current_url == 'https://ads.vk.com/cases'

# def testCompanyKeysHelpSideButton(login, testHelpSideButton):
#         driver = login
#         companyKeysButton = testHelpSideButton.find_element(By.XPATH, ".//section[1]/a[2]/div[1]")
#         companyKeysButton.click()
#         assert driver.current_url == 'https://ads.vk.com/help/subcategories/agency'

# def testCompanyKeysHelpSideButton(login, testHelpSideButton):
#         driver = login
#         companyKeysButton = testHelpSideButton.find_element(By.XPATH, ".//section[1]/a[3]/div[1]")
#         companyKeysButton.click()
#         assert driver.current_url == 'https://ads.vk.com/upvote'


def test_clients(login):
        driver = login
        clientsIco = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[@data-route='dashboardV2']/div[2]"))
        )
        clientsIco.click()

def test_budget(login):
        driver = login
        budgetIco = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[@data-route='budget']/div[2]"))
        )
        budgetIco.click()
        specDetailsBut = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='vkuiPlaceholder__action']"))
        )
        specDetailsBut.click()
        closeButton = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Закрыть']"))
        )
        closeButton.click()

def test_access_right(login):
        driver = login
        clientsIco = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[@data-route='access_rights']/div[2]"))
        )
        clientsIco.click()
        addManagerButton = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@data-testid='add-manager']/div[2]"))
        )
        addManagerButton.click()
        addManagerModal = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "vkuiModalPage__content-in"))
        )
        managerFIO = addManagerModal.find_element(By.XPATH, ".//input[@name='managerFio']")
        managerFIO.send_keys("123")
        managerAcc = addManagerModal.find_element(By.XPATH, ".//input[@name='managerEmail']")
        managerAcc.send_keys("123")
        saveButt = addManagerModal.find_element(By.XPATH, ".//div[@class='ModalFooterSimple_container__rteom']/button[2]")
        saveButt.click()
        closeButton = addManagerModal.find_element(By.XPATH, "//div[@aria-label='Закрыть']")
        closeButton.click()