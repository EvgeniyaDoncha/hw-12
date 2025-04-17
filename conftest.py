import pytest

@pytest.fixture(scope='function')
def setup_browser(request):

    from selenium.webdriver.chrome.options import Options
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)
    from selene.support import webdriver
    driver = webdriver.Remote(
        command_executor=f"https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options
    )

    from selene import Browser
    from selene import Config
    browser = Browser(Config(driver))
    yield browser

    browser.quit()