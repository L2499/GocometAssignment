from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent

options = Options()
ua = UserAgent()
userAgent = ua.random
print(userAgent)
options.add_argument(f'user-agent={userAgent}')
driver = webdriver.Chrome(chrome_options=options, executable_path=r'chromedriver.exe')
driver.get("https://www.google.co.in")
driver.quit()



Featured = //*[@id="a-popover-3"]/div/div/ul/li[1]
Price: Low to high = //*[@id="a-popover-3"]/div/div/ul/li[2]
Price high to low = //*[@id="a-popover-3"]/div/div/ul/li[3]
new = //*[@id="a-popover-3"]/div/div/ul/li[5]