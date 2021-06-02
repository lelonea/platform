from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import random
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
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR("//*[text()='Messenger']"))))
        direct_button = self.browser.find_element_by_css_selector("[aria-label=Messenger]")
        direct_button.click()
        time.sleep(5)


