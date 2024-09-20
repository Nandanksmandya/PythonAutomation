import time

from selenium.webdriver.common.by import By


class Mmt:

    def __init__(self, driver):
        self.driver = driver

    def popuppage_closing(self):
        self.driver.find_element(By.XPATH, '//span[@class="commonModal__close"]').click()

    def selecting_mode_transportatin(self):
        self.driver.find_element(By.XPATH, '//li[@class="menu_Buses"]').click()

    def selecting_routeAnddate(self):
        self.driver.find_element(By.XPATH, '//input[@id="fromCity"]').click()
        self.driver.find_element(By.XPATH, '//input[@placeholder="From"]').send_keys("Chennai")
        time.sleep(1)
        suggetions = self.driver.find_element(By.XPATH, '//ul[@role="listbox"]/li[1]')
        suggetions.click()
        self.driver.switch_to.active_element.send_keys("Banglore")
        time.sleep(1)
        sugg_to = self.driver.find_element(By.XPATH, '//ul[@role="listbox"]/li[1]')
        sugg_to.click()
        time.sleep(1)
        self.driver.execute_script("window.scrollBy(0, 100);")
        time.sleep(1)
        self.driver.find_element(By.XPATH,
                                 '(//div[@class="DayPicker-Body"]//div[contains(@aria-label,"Sat") and  @aria-disabled="false"])[1]').click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//button[text()="Search"]').click()

    def filtering(self):
        self.driver.find_element(By.XPATH, '//span[text()="AC"]').click()
        self.driver.find_element(By.XPATH, '//span[text()="Sleeper"]').click()
        self.driver.execute_script("window.scrollBy(0, 500);")
        self.driver.find_element(By.XPATH, '//input[@id="Pick up point"]').send_keys("Thuraipakkam")
        self.driver.find_element(By.XPATH, '//ul[@class="dropdownWrap"]//span[text()="Thuraipakkam"]').click()
        self.driver.find_element(By.XPATH,
                                 '//div[(text()="Pick up time - Chennai")]/../..//span[text()="6 PM to 11 PM"]').click()
        self.driver.execute_script("window.scrollBy(0, 200);")
        self.driver.find_element(By.XPATH, '//input[@id="Drop point"]').send_keys("majestic")
        self.driver.find_element(By.XPATH, '//input[@id="Drop point"]/../..//span[text()="Majestic"]').click()
        self.driver.execute_script("window.scrollBy(0, -1000);")
        time.sleep(1)
        num_bus_found = self.driver.find_elements(By.XPATH,
                                                  '//div[@class="busListingContainer"]/div[contains(@class, "busCardContainer")]')
        num_count = len(num_bus_found)
        # breakpoint()
        print(num_count, "Buses found")

        return num_count

    def avilability_of_seats(self, coun):
        for i in range(1, coun + 1):
            self.driver.execute_script("document.body.style.zoom='0.5'")
            # driver.execute_script(f"window.scrollBy(0, {scroll_rate});")
            self.driver.find_element(By.XPATH, f'(//div[text() = "Select Seats"])[{i}]').click()
            time.sleep(1)
            seats_available = self.driver.find_elements(By.XPATH,
                                                        '//span[@data-testid="seat_horizontal_sleeper_available"]')
            # or //span[@data-testid="seat_seater_available"] :-> for sitting
            print(f"Bus Number {i} having ", len(seats_available), "Seats.")
            self.driver.find_element(By.XPATH, '//div[text()="Hide Seats"]').click()
