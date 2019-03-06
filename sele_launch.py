from selenium import webdriver

userid = 'userid'
password = 'password'

browser = webdriver.Safari()
url = 'http://ucffans.mayhem.cbssports.com/brackets/'
browser.get(url)

username = browser.find_element_by_id("userid")
userpassword = browser.find_element_by_id("password")

username.click()
username.clear()
username.send_keys('userid')
userpassword.send_keys('password')

submitButton = browser.find_element_by_name("_submit")
submitButton.click()

browser.close()
