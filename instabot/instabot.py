from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from data import username, password
import time

chromedriver = "/usr/bin/chromedriver"
browser = webdriver.Chrome('/usr/bin/chromedriver')
browser.get('https://www.instagram.com')
wait = WebDriverWait(browser, 20)


def login(u, p):
    wait.until(EC.element_to_be_clickable((By.NAME, 'username')))

    username_field = browser.find_element(By.NAME, 'username')
    username_field.clear()
    username_field.send_keys(u)

    password_field = browser.find_element(By.NAME, 'password')
    password_field.clear()
    password_field.send_keys(p)

    password_field.send_keys(Keys.ENTER)


login(username, password)
time.sleep(10)

browser.close()
browser.quit()
