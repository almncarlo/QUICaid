import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

options = webdriver.ChromeOptions()
#options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-notifications')
options.add_argument('--disable-extensions')
options.add_argument('--disable-popup-blocking')
options.add_argument('--start-maximized')
options.add_argument('--disbale-infobars')
service = Service(executable_path="./chromedriver")
driver = webdriver.Chrome(service=service, options=options)

driver.get('https://www.instagram.com')

WebDriverWait(driver, 5).until (
	EC.presence_of_element_located((By.NAME, 'username'))
)
input_email = driver.find_element(By.NAME, 'username')
input_email.send_keys("sslnetworks1@gmail.com")
time.sleep(1)
input_pass = driver.find_element(By.NAME, 'password')
input_pass.send_keys("ilovessl")
time.sleep(1)
input_pass.send_keys(Keys.ENTER)

WebDriverWait(driver, 10).until (
	EC.presence_of_element_located((By.CSS_SELECTOR, "[aria-label='Reels']"))
)
reels = driver.find_element(By.CSS_SELECTOR, "[aria-label='Reels']")
reels.click()


time.sleep(310)
driver.quit()
