from selenium import webdriver
import time 

# Definimos las opciones de Chrome
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("start-maximized")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
capabilities = chrome_options.to_capabilities()
print(capabilities)
capabilities["goog:chromeOptions"]["excludeSwitches"] = ["disable-popup-blocking"]

wd = webdriver.Chrome('C:\\users\\juanp\\chromedriver',chrome_options=chrome_options)

wd.get('https://magiceden.io/marketplace/solswipe')

wd.maximize_window()
time.sleep(15)

print(wd.execute_script("return document.getElementsByTagName('html')[0].innerHTML"))

content = wd.find_elements_by_xpath(".//div[@class='tw-bg-gray-200 tw-truncate tw-p-2 tw-space-x-2 tw-rounded-[4px] tw-flex tw-items-center tw-justify-between tw-flex-col sm:tw-flex-row']")

for c in content:
    print(c.text)