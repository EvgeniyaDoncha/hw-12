import pytest

from selenium import webdriver


from selenium.webdriver.chrome.service import Service



@pytest.fixture(scope='function')
def setup_browser(request):

    from selenium.webdriver.chrome.options import Options
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options":{
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)
    #from selene.support import webdriver
    driver = webdriver.Remote(
        command_executor=f"https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options
    )

  

    #from selene import Browser
    #from selene import Config


    #browser = Browser(Config(driver))
    #yield browser

    from selene import Browser, Config
    from selenium import webdriver

    # Создание экземпляра драйвера
    driver = webdriver.Chrome()  # Убедитесь, что у вас установлен ChromeDriver

    # Настройка конфигурации
    config = Config(driver=driver)  # Передаем созданный драйвер в Config

    # Создание браузера
    browser = Browser(config)

    # Ваш код для работы с браузером
    yield browser

    # Закрытие браузера
    browser.quit()

    from utils import attach
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)