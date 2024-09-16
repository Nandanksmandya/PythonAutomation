import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# To stop automatically closing browser
option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=option,)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get(r'https://www.passportindia.gov.in/AppOnlineProject/welcomeLink#')
driver.find_element(By.XPATH, '//a[@class="twoyears-close-btn"]').click()
cont = driver.find_element(By.XPATH, '(//li[@id="contactus"])[2]')
act = ActionChains(driver)
act.move_to_element(cont).perform()
passport_tab = driver.find_element(By.XPATH, '//a[@id="pass"]')
passport_tab.click()
gen_info = driver.find_element(By.XPATH, '//a[@id="pass1"]')
gen_info.click()
driver.execute_script("window.scrollBy(0, 400);")
# driver.find_element(By.XPATH, '(//div[@class="Information_Corner_List"])[2]//li[2]').click()
# # driver.find_element(By.XPATH, '//li[contains(text(), "main passport application")]/a').click()
# driver.find_element("xpath", '//li[contains(text(), "main passport application")]/a').click()
# time.sleep(3)
# driver.close()
