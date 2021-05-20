try:
	from selenium import webdriver
	from selenium.webdriver.firefox.options import Options
	import time
except Exception:
	print('Package Error: The packages that the program using is not exist, Try "pip3 install selenium"')

def main():
	print("Applcation starts...")
	options = Options()
	options.headless = True
	browser = webdriver.Firefox(options=options, executable_path='/root/discord/geckodriver')
	url = "https://www.youtube.com/c/AboFlah/videos"
	while True:
		try:
			time.sleep(1800)
			browser.get(url)
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
			print("Error: error has been ocurred, send the log to the developers it you sure this is an error from the app")
			e = open('Error.log', 'w')
			e.write(ex)
			break
	browser.quit()

if __name__=='__main__':
	print("Its working very well")
	print("Every 1800 seconds(30 minutes) the app will check for a new video")
	time.sleep(0.75)
	main()
