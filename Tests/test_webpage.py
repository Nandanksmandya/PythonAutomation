import datetime

import pytest

from POM.webpage import MMT


class TestMMT:
    counts = 0

    def test_MMTwebpage(self, init_driver):
        driver = init_driver
        try:
            n = MMT(init_driver)
            n.popuppage_closing()
            n.selecting_mode_transportatin()
            n.selecting_routeAnddate()
            TestMMT.counts += n.filtering()
            n.avilability_of_seats(TestMMT.counts)

        except BaseException as msg:
            td = datetime.datetime.now()
            name = f'Screenshot_{td.date}_{td.hour}_{td.minute}_{td.second}.png'
            path = "../Screenshots/"
            driver.save_screenshot(path+name)
            raise msg
