from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = '/Users/chromedriver' #Path were you have chromedriver s

#driver is what will take on actions to interact with the webpage


driver = webdriver.Chrome(PATH) #we need to pick a the browser we need to use for selenium

# This bot was specifically created to purchase a PS5 Console from a walmart website on 11/12 . It will not work with other shopping sites
# with some tweaking and few knowledge of selenium you could adapt it to purchase another item , form another shopping site

#The get fucntion opens a specific website
driver.maximize_window()
driver.get('https://www.walmart.com/ip/PlayStation-5-Console/363472942') #place your desired website inside

#Look for the add to cart button and proceed
search = driver.find_element_by_xpath('//button[@data-tl-id="ProductPrimaryCTA-cta_add_to_cart_button"]')
search.send_keys(Keys.ENTER)
time.sleep(3)

#Look for the check out button  and proceed
search = driver.find_element_by_xpath('//button[@data-tl-id="IPPacCheckOutBtnBottom"]')
search.send_keys(Keys.ENTER)
time.sleep(2)

#For faster purchase and checkout procedure i chose to sign in with crendentials

#Look for the sign in entry email and enter it
search = driver.find_element_by_id('sign-in-email')
search.send_keys('enteryouremailhere@gmail.com')

#Look for the password entry and enter it

search = driver.find_element_by_xpath('//input[@data-tl-id="signin-password-input"]')
search.send_keys('enteryourpasswordhere')

#Look for the sign in button and proceed
search = driver.find_element_by_xpath('//button[@data-automation-id="signin-submit-btn"]')
search.send_keys(Keys.ENTER)
time.sleep(3)

#Look for the continue button and proceed
search = driver.find_element_by_xpath('//button[@data-automation-id="fulfillment-continue"]')
search.send_keys(Keys.ENTER)
time.sleep(3)

#Look for the continue button and proceed
search = driver.find_element_by_xpath('//button[@data-automation-id="address-book-action-buttons-on-continue"]')
search.send_keys(Keys.ENTER)
time.sleep(3)

#Fill info for cvv
search = driver.find_element_by_name('cvv')
search.send_keys('966')
time.sleep(1)

#Look for the submit payment button and proceed
search = driver.find_element_by_xpath('//button[@data-automation-id="submit-payment-cc"]')
search.send_keys(Keys.ENTER)
time.sleep(3)

#Look for the submit order button and proceed
search = driver.find_element_by_xpath('//button[@data-automation-id="summary-place-holder"]')
search.send_keys(Keys.ENTER)

