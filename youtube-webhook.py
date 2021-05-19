from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

binary = FirefoxBinary('/usr/bin/firefox')

options = webdriver.ChromeOptions() 
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Firefox(executable_path='/root/discord/geckodriver')
baseurl = "http://youtube.com"
keyword = input()
driver.get(f'{baseurl}/search?q={keyword}')
print([my_elem.text for my_elem in WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.XPATH, "//yt-formatted-string[@class='style-scope ytd-video-renderer' and @aria-label]")))])
driver.quit()