from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import sys
from getpass import getpass
from info import email
from info import psd
from info import chromium_path

def dailycheck():
	print('Beggining Daily Check...')

	# add path to chromium driver
	driver = webdriver.Chrome(chromium_path)
	driver.get("https://dailycheck.cornell.edu/daily-checkin")
	# student login
	driver.find_element_by_xpath('//*[@id="main-article"]/p/a[1]').click()
	sleep(1)
	# enter email and password
	driver.find_element_by_id('netid').send_keys(email)
	driver.find_element_by_name('password').send_keys(psd)
	driver.find_element_by_xpath('//*[@id="content"]/form/fieldset/div[3]/div/input').click()
	sleep(1)
	driver.find_element_by_xpath('//*[@id="continue"]').click()
	sleep(1)

	# click each of the no buttons
	buttons = ['//*[@id="positivetestever-no"]', '//*[@id="covidsymptoms-no"]', '//*[@id="contactdiagnosed-no"]', '//*[@id="contactsymptoms-no"]']
	for b in buttons:
		driver.find_element_by_xpath(b).click()

	driver.find_element_by_id('submit').click()
	driver.find_element_by_id('submit').click()
	print("Daily Check Complete")
	driver.quit()

dailycheck()