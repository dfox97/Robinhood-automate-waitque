from selenium import webdriver
import time
import random
letters = ["a", "b","c", "d","e", "f","g", "h","i", "j","k", "l","m", "n",
           "o", "p","q", "r","s", "t","u", "v","w", "x","y", "z",]
while True:

    random1 = random.choice(letters)+random.choice(letters)+random.choice(letters)+random.choice(letters)
    username=random1+'@hotmail.com'

    driver = webdriver.Chrome('./drivers/chromedriver')
    driver.get("https://robinhood.com/gb/en/about/?referral_code=cG5t")

    driver.find_element_by_class_name("css-yjt382-EntryForm").send_keys(username)
    time.sleep(1)
    driver.find_element_by_class_name("css-jv7v4j-EntryForm").click()
    time.sleep(2)
    driver.close()
    continue