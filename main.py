import sys
import random
import urllib.request
from call_cv import action
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


DEFAULT_USER_AGENTS = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/65.0.3325.181 Chrome/65.0.3325.181 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; Moto G (5) Build/NPPS25.137-93-8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.137 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 7_0_4 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11B554a Safari/9537.53",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:59.0) Gecko/20100101 Firefox/59.0",
    "Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0"
]

DEFAULT_USER_AGENT = random.choice(DEFAULT_USER_AGENTS)

print(DEFAULT_USER_AGENT)

# Variables

driver = webdriver.Chrome()
driver.get('http://google.com')
xpath = '//*[@id="hplogo"]'
file_name = 'p.png'

# Execution of process

try:

    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
    logo = driver.find_element_by_xpath(xpath)
    logo.click()
    src = logo.get_attribute('src')
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', DEFAULT_USER_AGENT)]
    urllib.request.install_opener(opener)
    urllib.request.urlretrieve(src, file_name)

    driver.quit()

except:

    print('Something went wrong')

    driver.quit()
    sys.exit(-1)

else:

    try:

        action(file_name)

    except:

        sys.exit(-1)
