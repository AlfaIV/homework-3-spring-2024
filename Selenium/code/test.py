from pages.PAlegalEntityPage import PAlegalEntityTopNavbar
from selenium.webdriver.common.by import By
import time

def test_top_navbar(login):
    
    pa_legal_entity_page = PAlegalEntityTopNavbar(login)
    # почему-то не работает клик по иконке
    # pa_legal_entity_page.click_to_VK_ico()
    # assert pa_legal_entity_page.get_current_url() == 'https://ads.vk.com/hq/dashboard'
    
    pa_legal_entity_page.click_to_user_name()
    # тут нужны проверки
    pa_legal_entity_page.click_to_user_name()

    pa_legal_entity_page.click_to_bell()
    pa_legal_entity_page.check_bell_text_field()
    pa_legal_entity_page.click_to_bell()

    pa_legal_entity_page.user_log_out()
    assert pa_legal_entity_page.get_current_url() == 'https://ads.vk.com/'


def test_top_navbar(login):
    
    pa_legal_entity_page = PAlegalEntityTopNavbar(login)

    # почему-то не работает клик по иконке
    # pa_legal_entity_page.click_to_VK_ico()
    # assert pa_legal_entity_page.get_current_url() == 'https://ads.vk.com/hq/dashboard'
    
    pa_legal_entity_page.click_to_user_name()
    # тут нужны проверки
    pa_legal_entity_page.click_to_user_name()

    lambda: pa_legal_entity_page.click_to_bell()
    pa_legal_entity_page.check_bell_text_field()
    pa_legal_entity_page.click_to_bell()

    pa_legal_entity_page.user_log_out()
    assert pa_legal_entity_page.get_current_url() == 'https://ads.vk.com/'
