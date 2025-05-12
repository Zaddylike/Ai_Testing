# appium_driver.py
from appium import webdriver
from selenium.common.exceptions import WebDriverException

def create_driver():
    caps = {
        'platformName': 'Android',
        'deviceName'  : 'emulator-5554',
        'appPackage'  : 'com.example.app',
        'appActivity' : '.MainActivity'
    }
    try:
        return webdriver.Remote('http://localhost:4723/wd/hub', caps)
    except WebDriverException as e:
        print(f"[Error] 無法啟動 Appium Driver：{e}")
        return None

if __name__ == "__main__":
    driver = create_driver()
    if driver:
        print(driver.page_source)
        driver.quit()
