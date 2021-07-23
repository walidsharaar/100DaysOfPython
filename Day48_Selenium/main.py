from selenium import webdriver

CHROME_DRIVER_PATH= "C:/Webdrivers/chromedriver.exe"
driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
driver.get("https://www.amazon.com/Washable-Replaceable-Lupantte-Cognitive-Developmental/dp/B089NPCN4F/ref=sr_1_13_sspa?dchild=1&qid=1627065247&rnid=16225005011&s=baby-products-intl-ship&sr=1-13-spons&psc=1&smid=A173TL47D5PM1H&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExUDA4MUVONE5MMFVaJmVuY3J5cHRlZElkPUEwNTEzMzU2M1RVRkVHVkY4VlI5WCZlbmNyeXB0ZWRBZElkPUEwNDE0MTA5MzBWVEc3NlNBRVJIRyZ3aWRnZXROYW1lPXNwX210Zl9icm93c2UmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl")

price = driver.find_element_by_id("priceblock_ourprice")

print(price.text)






#driver.close()
driver.quit()
