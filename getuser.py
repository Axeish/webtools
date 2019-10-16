from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

#driver = webdriver.Firefox()
driver = webdriver.Chrome()

#river.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't') 
driver.get("https://python.org")
