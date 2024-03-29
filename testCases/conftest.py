from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):

    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path="C:\\Work\\Learning\\Python\\Automation_Testing\\Selenium_Automation\\Drivers\\chromedriver.exe")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Ie()

    return driver


def pytest_addoption(parser):   # this will get the value for CLI
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")



# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Manikandan'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)