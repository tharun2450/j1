import argparse
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

def main(browser):
    driver = None
    if browser == 'chrome':
        options = ChromeOptions()
        driver = webdriver.Chrome(service=ChromeService(), options=options)
    elif browser == 'firefox':
        options = FirefoxOptions()
        driver = webdriver.Firefox(service=FirefoxService(), options=options)
    else:
        print(f"Browser '{browser}' not supported.")
        return

    try:
        # Example URL and action
        driver.get("http://www.google.com")
        print("Title of the page is:", driver.title)
        # Add your test code here
    finally:
        driver.quit()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run browser tests.')
    parser.add_argument('--browser', type=str, required=True, help='Browser to use for testing (chrome/firefox)')
    args = parser.parse_args()

    main(args.browser)
