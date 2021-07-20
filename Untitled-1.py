import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://www.midsouthshooterssupply.com/dept/reloading/primers?currentpage=1")
driver.implicitly_wait(20)
time.sleep(5)
driver.find_element(By.NAME,"email").send_keys("sonu969123@gmail.com")
clickbutton=driver.find_element(By.XPATH,"//input[@value='SIGN UP']")
clickbutton.click()
ClickStart=driver.find_element(By.XPATH,"//input[@value='START SHOPPING']")
ClickStart.click()




title=driver.find_elements(By.XPATH,"//a[contains(text(),'Primer')]")
price= driver.find_elements(By.XPATH,"//span[contains(@class,'price')]")
maftr= driver.find_elements_by_class_name("catalog-item-brand-item-number")
availibility= driver.find_elements(By.XPATH,"//span[contains(@class,'out-of-stock')]")

for titles in title:
    print(titles.text)

for prices in price:
    print(prices.text)

for m in maftr:
    print(m.text)

for avail in availibility:
    print(avail.text)

driver.quit()