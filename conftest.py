import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture(scope="module")# params=["Chrome", "Firefox", "IE"])
def driver(request):
    driver = webdriver.Chrome()
    WebDriverWait(driver, 5)
    driver.get('http://blog.csssr.ru/qa-engineer/')
    request.addfinalizer(driver.quit)
    return driver