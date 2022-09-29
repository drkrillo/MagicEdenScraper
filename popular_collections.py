from operator import index
from selenium import webdriver
import time 
import pandas as pd
import sys
from helpers import divide_chunks, divide_chunks_by_type

pd.options.display.max_columns = None
pd.options.display.max_rows = None

# Definimos las opciones de Chrome
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
capabilities = chrome_options.to_capabilities()
capabilities["goog:chromeOptions"]["excludeSwitches"] = ["disable-popup-blocking"]

wd = webdriver.Chrome('chromedriver',chrome_options=chrome_options)

wd.get('https://magiceden.io/popular-collections')

wd.maximize_window()
time.sleep(2)

popular_collections = pd.DataFrame(columns=['Rank','CollectionName','Link'])
popular_collections_stats = pd.DataFrame(columns=['Rank','VolumeTotal','24hsVolume','Sales','FloorPrice','Owners','TotalSupply'])
for i in range(1,21):
    Y = 50*i
    scrollable_element = wd.find_element('xpath','//div[@class="dark-scroll-bar"]')
    wd.execute_script(f"arguments[0].scrollBy(0, {Y});", scrollable_element)

    time.sleep(0.1)
    content = wd.find_elements('xpath', "//tbody[@role='rowgroup']/tr[@class='!tw-border-b-[1px] !tw-border-gray-400 me-table-border']/td/a")
    try:
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
        popular_collections = popular_collections.append(df, ignore_index=True)

    except:
        pass

    content = wd.find_elements('xpath', "//tr[@role='row']/td[@role='cell']")
    row = []
    for i in content:
        counter = 0
        try:
            if '\n' in i.text:
                if counter > 0:
                    pass
                else:
                    row.append(int(i.text.split('\n')[0]))
                    counter += 1
            elif '%' in i.text:
                pass
            else:
                row.append(i.text)
        except:
            pass

        rows = list(divide_chunks_by_type(row))
        rows = [row for row in rows if len(row)==7]

popular_collections.drop_duplicates(inplace=True)
#popular_collections = pd.merge(popular_collections, popular_collections_stats)
print(popular_collections)
popular_collections.to_csv('popular_collections.csv')