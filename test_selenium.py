import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def browser():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Запуск браузера в фоновом режиме
    chrome_service = Service('/path/to/chromedriver')  # Укажите путь к chromedriver
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    yield driver
    driver.quit()


def test_site_performance(browser):
    browser.get("https://your-website-url.com")

    performance_score = browser.execute_script("return JSON.stringify(window.performance.timing)")

    # Здесь можно добавить проверки производительности, например, на загрузку страницы, время отклика и другие метрики

    assert performance_score is not None, "Failed to retrieve performance data"