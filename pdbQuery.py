from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import sys

# PATH = os.path.join(os.path.dirname(sys.argv[0]), "webdriver", "geckodriver")
# print(PATH)
UNIPROT_ID = "P60484"
XPATH = "//tbody"
# ./webdriver/geckodriver is needed to be put into system PATH

driver = webdriver.Firefox()
# driver = webdriver.Firefox("/PATH/TO/DRIVER")
option = webdriver.FirefoxOptions()
option.add_argument("--proxy-server=http://127.0.0.1:1080")
# option.add_argument('--disable-gpu')
# option.add_argument('blink-settings=imagesEnabled=false')
# option.add_argument('--headless')
# option.binary_location = "/PATH/TO/BIN"
# driver=webdriver.Firefox(firefox_options=option, executable_path=PATH)
driver=webdriver.Firefox(options=option)

driver.get("https://www.uniprot.org/uniprot/%s" %UNIPROT_ID)

element = WebDriverWait(driver, 30, 0.5).until(EC.presence_of_element_located((By.XPATH, XPATH)))

pdbTable = driver.find_element_by_xpath(XPATH)
print(pdbTable.get_attribute("outerHTML"))