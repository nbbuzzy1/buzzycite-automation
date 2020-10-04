from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.add_argument("--headless")


def buzzycite_automation():
	chrome_browser = webdriver.Chrome('./chromedriver.exe', options=options)
	chrome_browser.get('https://buzzycite.com')
	time.sleep(95)
	buzzycite_page_interaction(chrome_browser)

	chrome_browser.get('https://google.com')
	time.sleep(35)
	google_page_interaction(chrome_browser)
	time.sleep(95)
	buzzycite_page_interaction(chrome_browser)
	chrome_browser.close()


def buzzycite_page_interaction(chrome_browser):
	case_search_button = chrome_browser.find_element_by_xpath("//i[text()='search']")
	case_search_button.click()
	time.sleep(95)
	search_panel = chrome_browser.find_element_by_xpath("//mat-panel-title[text()='Case Term or Phrase']")
	search_panel.click()


def google_page_interaction(chrome_browser):
	google_search_input = chrome_browser.find_element_by_class_name('gLFyf')
	google_search_input.send_keys('buzzycite court case search')
	google_search_input.send_keys(Keys.ENTER)
	time.sleep(35)
	buzzycite_url = 'https://www.buzzycite.com/'
	buzzycite_link = chrome_browser.find_element_by_xpath('//a[@href="'+ buzzycite_url +'"]')
	buzzycite_link.click()


successful_automations = 0

while True:
	buzzycite_automation()
	successful_automations += 1
	print('successful automation', successful_automations)
	time.sleep(10800)