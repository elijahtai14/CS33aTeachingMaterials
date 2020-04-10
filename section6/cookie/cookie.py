from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://orteil.dashnet.org/cookieclicker/')
cookie = browser.find_element_by_id('bigCookie')

while True:
    try:
        cookie.click()
    except:
        continue