import sys
import time
from mod.recog import numrecog
try:
    import cloudscraper
    scraper = cloudscraper.create_scraper()
except:
    import cfscrape
    scraper = cfscrape.create_scraper()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

ERROR = """chromedriver.exe was not found or is not compatible with your browser.
Make sure that it's located in your PATH or in your directory.
Download the driver from this website http://chromedriver.chromium.org if you haven't."""

# sample variables
webs = 'https://kissanime.ru/Anime/One-Punch-Man-Season-2/Episode-005?id=158021'
xpaths = '//*[@id="formVerify1"]/div[2]/div/div[1]/img'
image_names = 'image.png'

def statweb():
    if driver.get(webs):
        return False
    else:
        return True

def statim(xpath=xpaths):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
    global logo
    logo = driver.find_element_by_xpath(xpath)
    src = logo.get_attribute('src')
    i_mage = scraper.get(src, stream=True)
    total_size = int(i_mage.headers['content-length'])
    print(total_size)
    with open(image_names, "wb") as byte:
        byte.write(i_mage.content)
    return True


def spin(func):
    def spinning_cursor():
        while True:
            for cursor in '|/-\\':
                yield cursor

    spinner = spinning_cursor()
    is_stat_called = False
    while not is_stat_called:
        is_stat_called = func
        sys.stdout.write(next(spinner))
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write('\b')

def catch(image_name=image_names):
    global driver
    driver = webdriver.Chrome()
    print('Initializing Chrome: ', end="")
    spin(statweb())
    print('done!')

    try:
        print('Downloading Image: ', end="")
        global logo
        spin(statim())

        print('done!')

    except:
        print('Something went wrong')

        driver.quit()
        sys.exit()

    return image_name

numrecog(catch())
