from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from data import username, password


class InstagramBot:
    """Instagram Bot on Python sends messages to your clients"""

    # class constructor
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.browser = webdriver.Chrome('/usr/bin/chromedriver')

    # method for closing the browser
    def close_browser(self):
        self.browser.close()
        self.browser.quit()

    # account login method
    def login(self):
        self.browser.get('https://www.instagram.com')
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.NAME, 'username')))

        username_field = self.browser.find_element(By.NAME, 'username')
        username_field.clear()
        username_field.send_keys(self.username)

        password_field = self.browser.find_element(By.NAME, 'password')
        password_field.clear()
        password_field.send_keys(self.password)

        password_field.send_keys(Keys.ENTER)

    # method for opening direct
    def open_direct(self):
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[aria-label='Messenger']")))
        direct_button = self.browser.find_element_by_css_selector("[aria-label='Messenger']")
        direct_button.click()

    # method to close notification
    def close_notification(self):
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Не сейчас']")))
        disable_notification = self.browser.find_element_by_xpath("//*[text()='Не сейчас']")
        disable_notification.click()

    # method for sending message
    def send_message(self, user='', message=''):
        self.open_direct()
        self.close_notification()

        WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "[aria-label='Новое сообщение']")))
        direct_button = self.browser.find_element_by_css_selector("[aria-label='Новое сообщение']")
        direct_button.click()

        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[placeholder='Поиск...']")))
        search = self.browser.find_element_by_css_selector("[placeholder='Поиск...']")
        search.clear()
        search.send_keys(user)

        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, f"//*[text()='{user}']")))
        self.browser.find_element_by_xpath(f"//*[text()='{user}']").click()

        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Далее']")))
        self.browser.find_element_by_xpath("//*[text()='Далее']").click()

        WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "[placeholder='Напишите сообщение...']")))
        search = self.browser.find_element_by_css_selector("[placeholder='Напишите сообщение...']")
        search.clear()
        search.send_keys(message)

        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Отправить']")))
        self.browser.find_element_by_xpath("//*[text()='Отправить']").click()


bot = InstagramBot(username, password)
bot.login()
bot.send_message('lelolash', 'hello')
