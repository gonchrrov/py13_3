import pytest
from selene import browser


@pytest.fixture(scope='session', autouse=True)
def browser_config():
    browser.config.window_height = 1080
    browser.config.window_width = 1366
    browser.config.headless = True
    yield
    browser.quit()
