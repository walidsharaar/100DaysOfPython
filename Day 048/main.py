from selenium import webdriver

CHROME_DRIVER_PATH= "C:/Webdrivers/chromedriver.exe"
driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
driver.get("https://www.amazon.com")

price = driver.find_element_by_id("priceblock_ourprice")

print(price)






#driver.close()
driver.quit()
