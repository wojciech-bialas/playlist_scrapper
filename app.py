from selenium import webdriver
from datetime import datetime


class PlaylistScrapper():


	def __init__(self):
		self.driver = webdriver.Firefox()
		self.driver.implicitly_wait(10)
		self.driver.get("http://radioluz.pwr.edu.pl/")
		self.current_date = datetime.now().strftime('%Y-%m-%d')
		self.main()


	# returns a list of 5 last played tracks on radio luz
	def get_songs(self):
		songs = []
		path = "/html/body/div[2]/div/section[3]/div/ul/"

		try:
			for i in range(1, 6):
				time = self.driver.find_element_by_xpath(f"{path}li[{i}]/time").text
				title = self.driver.find_element_by_xpath(f"{path}li[{i}]/div/p[1]").text
				artist = self.driver.find_element_by_xpath(f"{path}li[{i}]/div/p[2]").text
				songs.append(f'{time}  {artist} - {title}')
			return songs

		except Exception as e:
			raise e

		finally:
			self.driver.quit()


	# returns a list of already saved songs
	def get_saved(self):
		try:
			with open(f'np_luz_{self.current_date}.txt', mode='r') as file:
				return [line.strip("\n") for line in file.readlines()]
		except:
			return []


	def write_songs_to_file(self, prev, songs):
		try:
			with open(f'np_luz_{self.current_date}.txt', mode='a') as file:
				for item in songs:
					if item not in prev:
						file.write(item+"\n")
		except Exception as e:
			raise e


	def main(self):
		songs = self.get_songs()
		prev = self.get_saved()
		self.write_songs_to_file(prev, songs)


if __name__ == "__main__":
	PlaylistScrapper()
