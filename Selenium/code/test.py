from pages.PAlegalEntityPage import PAlegalEntityTopNavbar
import time
import pytest


@pytest.mark.parametrize("link_num, link", [
        (1, 'https://ads.vk.com/cases'),
        (2, 'https://ads.vk.com/help/subcategories/agency'),
        (3, 'https://ads.vk.com/upvote')
        ])
def test_help_button(login, link_num, link):
    pa_legal_entity_page = PAlegalEntityTopNavbar(login)
    pa_legal_entity_page.click_to_help_button()
    pa_legal_entity_page.redirect_to_help_button(link_num)
    pa_legal_entity_page.change_tab(pa_legal_entity_page.get_tab(-1))
    assert pa_legal_entity_page.get_current_url() == link
    # time.sleep(5)
    pa_legal_entity_page.close_current_tab()
    pa_legal_entity_page.change_tab(pa_legal_entity_page.get_tab(0))

def test_clients(login):

    pa_legal_entity_page = PAlegalEntityTopNavbar(login)
    pa_legal_entity_page.go_to_page("https://ads.vk.com/hq/dashboard")
    pa_legal_entity_page.click_to_clients()

def test_budget(login):

    pa_legal_entity_page = PAlegalEntityTopNavbar(login)
    pa_legal_entity_page.go_to_page("https://ads.vk.com/hq/dashboard")
    pa_legal_entity_page.click_to_budget()
    pa_legal_entity_page.specify_banking_details()


def test_access_right(login):
    
    pa_legal_entity_page = PAlegalEntityTopNavbar(login)
    pa_legal_entity_page.go_to_page("https://ads.vk.com/hq/dashboard")
    pa_legal_entity_page.click_to_access_right()
    pa_legal_entity_page.addManager("123","123")

def test_top_navbar(login):
    
    pa_legal_entity_page = PAlegalEntityTopNavbar(login)
    pa_legal_entity_page.go_to_page("https://ads.vk.com/hq/dashboard")
    pa_legal_entity_page.click_to_VK_ico()
    assert pa_legal_entity_page.get_current_url() == 'https://ads.vk.com/hq/dashboard'
    
    pa_legal_entity_page.click_to_user_name()
    pa_legal_entity_page.click_to_user_name()

    pa_legal_entity_page.click_to_bell()
    pa_legal_entity_page.check_bell_text_field()
    pa_legal_entity_page.click_to_bell()

    pa_legal_entity_page.user_log_out()
    assert pa_legal_entity_page.get_current_url() == 'https://ads.vk.com/'
