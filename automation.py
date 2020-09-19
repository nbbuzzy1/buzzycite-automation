from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from threading import Timer


def buzzycite_automation():
	chrome_browser = webdriver.Chrome('./chromedriver.exe')

	chrome_browser.get('https://buzzycite.com')

	chrome_browser.get('https://google.com')

	google_search_input = chrome_browser.find_element_by_class_name('gLFyf')
	google_search_input.send_keys('buzzycite free court case search')
	google_search_input.send_keys(Keys.ENTER)
	buzzycite_link = chrome_browser.find_element_by_xpath("//h3[contains(text(),'BuzzyCite')]")

	buzzycite_link.click()

	chrome_browser.close()


def buzzycite_interval():
    Timer(10000.0, buzzycite_automation).start()

Timer(1.0, buzzycite_automation).start()