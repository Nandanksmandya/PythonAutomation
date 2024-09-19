import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from Library import configure


@pytest.fixture(params=["Chrome", "edge"])
def init_driver(request):
    browsers = request.param

    if browsers.lower() == "chrome":
        # To stop automatically closing browser
        option = webdriver.ChromeOptions()
        option.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=option)
    else:
        driver = webdriver.Edge()

    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(configure.Configure.URL)
    yield driver
    driver.close()

