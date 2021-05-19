from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

print("Working very well")

while True:
	time.sleep(5)
	options = Options()
	options.headless = True
	browser = webdriver.Firefox(options=options, executable_path='/root/discord/geckodriver')
	url = "https://www.youtube.com/c/AboFlah/videos"

	browser.get(url)
	video = browser.find_element_by_xpath('//*[@id="video-title"]')
	video_title = str(video.text)
	f = open('titles.txt', 'r')
	past_title = f.readline()

	if past_title == video_title:
		pass
	else:
		video_url = str(browser.current_url)
		id = video_url.split("=", 1)[0]
		print("New")
		f = open('titles.txt', 'w')
		f.write(video_title)

browser.quit()
