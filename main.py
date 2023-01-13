from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

service = Service(executable_path="D:\\Ohjelmat\\ChromeDriver\\Chromedriver.exe")

driver = webdriver.Chrome(service=service)

# Get price
#driver.get("https://www.amazon.com/My-Little-Pony-Rarity-Classic/dp/B07BBGTPK6/ref=sr_1_1?crid=MUJLBIU7C8DJ&keywords=rarity&qid=1673443571&s=toys-and-games-intl-ship&sprefix=rarit%2Ctoys-and-games-intl-ship%2C161&sr=1-1")
#price = driver.find_element(By.CLASS_NAME, "a-price-whole")
#print(price.text)

driver.get("https://python.org/")

# get anchor tag
# documentation_link = driver.find_elements(By.CSS_SELECTOR, ".documentation-widget a")
# print(documentation_link)

# Get link text
#bug_link = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
#print(bug_link.text)

# Get CSS selectors
#links = driver.find_elements(By.CSS_SELECTOR, ".documentation-widget a")
#print(links)

# get logo size
#logo = driver.find_element(By.CLASS_NAME, "python-logo")
#print(logo.size)

# get search bar placeholder
#search_bar = driver.find_element(By.NAME, "q")
#print(search_bar.get_attribute("placeholder"))

events = driver.find_elements(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul')

#   print(type(events)) #   list

dict_events = {}



driver.quit()   # Closes the entire browser. driver.close() Closes a single, active tab
