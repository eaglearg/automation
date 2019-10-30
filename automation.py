from selenium import webdriver

#its necessary to download the updated driver for the browser
chrome_browser=webdriver.Chrome('./chromedriver.exe')
chrome_browser.maximize_window()
chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

assert 'Selenium Easy Demo - Simple Form to Automate using Selenium' in chrome_browser.title

show_message_button = chrome_browser.find_element_by_class_name('btn-default')
#print(show_message_button.get_attribute('innerHTML'))

assert 'Show Message' in chrome_browser.page_source

user_message = chrome_browser.find_element_by_id('user-message')
user_button2 = chrome_browser.find_elements_by_css_selector('#get-input > .btn')
user_message.clear()
user_message.send_keys('Hello world !')

show_message_button.click()
output_message = chrome_browser.find_element_by_id('display')

assert 'Hello world !' in output_message.text

chrome_browser.quit()