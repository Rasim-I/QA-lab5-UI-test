from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome("chromedriver/chromedriver.exe")
browser.get('https://stylus.ua/')
browser.implicitly_wait(10)
browser.maximize_window()

def search_test():
    browser.find_element_by_css_selector('[id="header-search"]').send_keys('стилус')
    browser.find_element_by_css_selector('[id="header-search"]').send_keys(Keys.RETURN)

    actual_text = browser.find_element_by_css_selector('div.page-name').text
    expected_text = 'Результаты поиска по запросу «стилус»'

    assert actual_text == expected_text


def auth_test():
    browser.find_element_by_css_selector('[class="profile-link js-action"]').send_keys(Keys.RETURN)

    actual_text = browser.find_element_by_css_selector('a.js-action').text
    expected_text = 'Я забыл пароль'

    assert actual_text == expected_text


def language_test():
    browser.find_element_by_css_selector('a.list-item').send_keys(Keys.RETURN)

    actual_text = browser.find_element_by_css_selector('[class="profile-block"]').text
    expected_text = 'Вітаємо'

    assert actual_text.__contains__(expected_text)


search_test()
auth_test()
language_test()



