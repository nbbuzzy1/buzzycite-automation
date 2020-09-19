from selenium import webdriver
import time

chrome_browser = webdriver.Chrome('./chromedriver.exe')

chrome_browser.get('https://buzzycite.com')

time.sleep(5)

chrome_browser.close()
