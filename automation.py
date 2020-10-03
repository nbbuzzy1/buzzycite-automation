from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.add_argument("--headless")

def buzzycite_automation():
	chrome_browser = webdriver.Chrome('./chromedriver.exe', options=options)

	chrome_browser.get('https://buzzycite.com')
	time.sleep(61)
	chrome_browser.get('https://google.com')

	google_search_input = chrome_browser.find_element_by_class_name('gLFyf')
	google_search_input.send_keys('buzzycite free court case search')
	google_search_input.send_keys(Keys.ENTER)
	buzzycite_url = 'https://www.buzzycite.com/'
	buzzycite_link = chrome_browser.find_element_by_xpath('//a[@href="'+ buzzycite_url +'"]')
	time.sleep(5)
	buzzycite_link.click()
	time.sleep(61)
	chrome_browser.close()
	print('successful automation')

while True:
	buzzycite_automation()
	time.sleep(10800)