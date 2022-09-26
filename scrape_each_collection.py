import pandas as pd
from selenium import webdriver
import time

df = pd.read_csv('popular_collections.csv')

pd.options.display.max_columns = None

# Definimos las opciones de Chrome
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("start-maximized")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
capabilities = chrome_options.to_capabilities()
capabilities["goog:chromeOptions"]["excludeSwitches"] = ["disable-popup-blocking"]

wd = webdriver.Chrome('chromedriver',chrome_options=chrome_options)

for href in df.Link.tolist():
    wd.get(href)
    wd.maximize_window()
    time.sleep(5)
    wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")    
    time.sleep(5)

    elems = wd.find_elements('xpath', '//div[@class="tw-absolute tw-w-full tw-cursor-pointer"]')
    for elem in elems:
        print(elem.text)
        print('---------------')
    break