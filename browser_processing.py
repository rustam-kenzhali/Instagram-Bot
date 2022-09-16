from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


s = Service('W:/1. Python/inst_bot_project/firefox_driver/geckodriver.exe')
browser = webdriver.Firefox(service=s)
browser.implicitly_wait(30)

action = ''
link = ''
count = 0


def start_brows_proces(get_action, get_link, get_count):
    global action
    global link
    global count
    action = get_action
    link = get_link
    count = get_count
    browser.get('https://www.instagram.com/')
    login('mr_kenzhali', '_383Men3900Rustam1__3cAraatist30_')
    sleep(10)
    browser.close()


def login(username, password):
    try:
        username_input = browser.find_element(By.NAME, "username")
        username_input.send_keys(username)

        password_input = browser.find_element(By.NAME, "password")
        password_input.send_keys(password)

        password_input.send_keys(Keys.ENTER)

        elem = WebDriverWait(browser, 30).until(
            EC.presence_of_element_located((By.CLASS_NAME, "eyXLr"))  # This is a dummy element
        )
        #
        processing()

    except Exception as ex:
        print(ex)
        browser.close()
        browser.quit()


def processing():
    # print(action, link, count)
    # https://www.instagram.com/champagnepapi/
    # https://www.instagram.com/p/Cf-CxCQuixx/
    browser.get(link)
    sleep(2)
    if action == 'Subscribe':
        subscr_btn = browser.find_element(By.CSS_SELECTOR, 'div._ab9k:nth-child(3) > div:nth-child(1) > div:nth-child(2) > button:nth-child(1)')
        subscr_btn.click()
    elif action == 'Like':
        print('Like')
        like_btn = browser.find_element(By.CSS_SELECTOR, '._aamw > button:nth-child(1)')
        like_btn.click()
    elif action == 'Save':
        print('Save')
        save_btn = browser.find_element(By.CSS_SELECTOR, '._aamz > div:nth-child(1) > div:nth-child(1) > button:nth-child(1)')
        save_btn.click()

# _383Men3900Rustam1__3cAraatist30_