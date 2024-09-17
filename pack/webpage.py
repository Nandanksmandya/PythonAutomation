import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# To stop automatically closing browser
option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=option, )
driver.maximize_window()
driver.implicitly_wait(10)
driver.get(r'https://www.makemytrip.com/')
driver.find_element(By.XPATH, '//span[@class="commonModal__close"]').click()
driver.find_element(By.XPATH, '//li[@class="menu_Buses"]').click()
driver.find_element(By.XPATH, '//input[@id="fromCity"]').click()
driver.find_element(By.XPATH, '//input[@placeholder="From"]').send_keys("Chennai")
time.sleep(1)
suggetions = driver.find_element(By.XPATH, '//ul[@role="listbox"]/li[1]')
# wait = WebDriverWait(driver, 10)
# wait.until(EC.visibility_of(suggetions)).click()
suggetions.click()
driver.switch_to.active_element.send_keys("Banglore")
time.sleep(1)
sugg_to = driver.find_element(By.XPATH, '//ul[@role="listbox"]/li[1]')
# wait.until(EC.visibility_of(sugg_to)).click()
sugg_to.click()
time.sleep(1)
# driver.find_element(By.XPATH, '//input[@id="travelDate"]').click()
driver.execute_script("window.scrollBy(0, 100);")
time.sleep(1)
# driver.execute_script("window.scrollBy(0, 1000);")
driver.find_element(By.XPATH,
                    '(//div[@class="DayPicker-Body"]//div[contains(@aria-label,"Sat") and  @aria-disabled="false"])[1]').click()
time.sleep(2)
driver.find_element(By.XPATH, '//button[text()="Search"]').click()
driver.find_element(By.XPATH, '//span[text()="AC"]').click()
driver.find_element(By.XPATH, '//span[text()="Sleeper"]').click()
driver.execute_script("window.scrollBy(0, 500);")
driver.find_element(By.XPATH, '//input[@id="Pick up point"]').send_keys("Thuraipakkam")
driver.find_element(By.XPATH, '//ul[@class="dropdownWrap"]//span[text()="Thuraipakkam"]').click()
driver.find_element(By.XPATH, '//div[(text()="Pick up time - Chennai")]/../..//span[text()="6 PM to 11 PM"]').click()
driver.execute_script("window.scrollBy(0, 200);")
driver.find_element(By.XPATH, '//input[@id="Drop point"]').send_keys("majestic")
driver.find_element(By.XPATH, '//input[@id="Drop point"]/../..//span[text()="Majestic"]').click()
driver.execute_script("window.scrollBy(0, -1000);")
time.sleep(1)
num_bus_found = driver.find_elements(By.XPATH,
                                     '//div[@class="busListingContainer"]/div[contains(@class, "busCardContainer")]')
num_count = len(num_bus_found)
print(num_count, "Buses found")
bus_name = []
for i in range(1, num_count + 1):
    bus_names = driver.find_element(By.XPATH, f'(//div[@class="busCardContainer "]//p)[{i}]')
    print("Bus Names are : " + bus_names.text)
    bus_name.append(bus_names.text)
    # time.sleep(1)
    # bus_names.click()
    # seats_available = driver.find_elements(By.XPATH, '//span[@data-testid="seat_horizontal_sleeper_available"]')
    # print("Available Seats", len(seats_available))
print(bus_name)
driver.quit()
