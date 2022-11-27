try:
	from selenium import webdriver
	from selenium.webdriver.firefox.options import Options
	import time
except Exception:
	print('Error: Selenium is not found/installed, try "pip3 install selenium"')
	
url = "https://www.youtube.com/c/AboFlah/videos"

def main():
	print("Applcation starts...")
	options = Options()
	options.headless = True
	# Using geckodriver since I was using linux at the time
	browser = webdriver.Firefox(options=options, executable_path='/path/to/geckodriver')
	while True:
		try:
			time.sleep(1800)
			browser.get(url)
			# idk if this will always work but if id didn't just change the xpath
			video = browser.find_element_by_xpath('//*[@id="video-title"]')
			video_title = str(video.text)
			f = open('titles.txt', 'r')
			past_title = f.readline()

			if past_title == video_title:
				pass
			else:
				print("New video has been uploaded, Check it now!")
				print("Opening the new video...")
				time.sleep(1)
				video.click()
				f = open('titles.txt', 'w')
				f.write(video_title)
		except KeyboardInterrupt:
			print("Closing...")
			break
		except Exception as ex:
			print('Error occured!\nAn "Error.log" has been generated\ncreate an issue at "https://github.com/OmarHosam/youtube-new-video-notifier/issues"')
			e = open('Error.log', 'w')
			e.write(ex)
			break
	browser.quit()

if __name__=='__main__':
	print("Its working very well")
	print("Every 1800 seconds(30 minutes) the app will check for a new video")
	time.sleep(0.75)
	main()
