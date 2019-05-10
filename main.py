import cv2
import sys
import random
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

DEFAULT_USER_AGENTS = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/65.0.3325.181 Chrome/65.0.3325.181 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; Moto G (5) Build/NPPS25.137-93-8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.137 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 7_0_4 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11B554a Safari/9537.53",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:59.0) Gecko/20100101 Firefox/59.0",
    "Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0"
]

DEFAULT_USER_AGENT = random.choice(DEFAULT_USER_AGENTS)

print(DEFAULT_USER_AGENT + "\n")

ERROR = """chromedriver.exe was not found or is not compatible with your browser.

Make sure that it's located in your PATH or in your directory.
Download the driver from this website http://chromedriver.chromium.org if you haven't."""

# Remove this tuple if you want to manually add some.
webs, xpaths, image_names = 'https://google.com', '//*[@id="hplogo"]', 'image.png'

def catch(web=webs, xpath=xpaths, image_name=image_names):
    try:
        driver = webdriver.Chrome()

    except:
        print(ERROR)
        sys.exit()

    driver.get(web)

    # Execution of process

    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
        logo = driver.find_element_by_xpath(xpath)
        logo.click()
        src = logo.get_attribute('src')
        opener = urllib.request.build_opener()
        opener.addheaders = [('User-agent', DEFAULT_USER_AGENT)]
        urllib.request.install_opener(opener)
        urllib.request.urlretrieve(src, image_name)

        driver.quit()

    except:
        print('Something went wrong')

        driver.quit()
        sys.exit(-1)

    try:
        action()

    except:
        print('Wrong call_cv module!')
        sys.exit(-1)

def action(name=image_names):
    img = cv2.imread(name, 1)
    cv2.imshow('some', img)
    cv2.waitKey(0)

catch()
