from selenium import webdriver
import time 
import pandas as pd

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

wd.get('https://magiceden.io/popular-collections')

wd.maximize_window()
time.sleep(5)

#scrollable_element = wd.find_element('xpath','//div[@class="dark-scroll-bar"]')
#wd.execute_script("arguments[0].scroll(0, arguments[0].scrollHeight);", scrollable_element)
#time.sleep(5)

content = wd.find_elements('xpath', "//tbody[@role='rowgroup']/tr[@class='!tw-border-b-[1px] !tw-border-gray-400 me-table-border']/td/a")

hrefs = [x.get_attribute('href') for x in content]
texts = [x.text for x in content]
ranking_places = [x.split('\n',1)[0] for x in texts]
collection_names = [x.split('\n',1)[1] for x in texts]
dict_for_df = {
    'Rank': ranking_places,
    'CollectionName': collection_names,
    'Link': hrefs
    }
df = pd.DataFrame(dict_for_df) 

df.to_csv('popular_collections.csv')