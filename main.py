import cv2
import sys
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

# Remove this tuple if you want to manually add some.
webs, xpaths, image_names = 'https://kissanime.ru/Anime/One-Punch-Man-Season-2/Episode-005?id=158021', '//*[@id="formVerify1"]/div[2]/div/div[1]/img', 'image.png'

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
        #logo.click()
        src = logo.get_attribute('src')
        i_mage = scraper.get(src)
        with open(image_name, "wb") as byte:
            byte.write(i_mage.content)

    except:
        print('Something went wrong')

        driver.quit()
        sys.exit()


    action()


def action(name=image_names):
    img = cv2.imread(name, 1)
    cv2.imshow("!kistack!", img)
    cv2.waitKey(0)

catch()
