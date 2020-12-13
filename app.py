from selenium import webdriver
from datetime import datetime
from time import sleep


class PlaylistScrapper():

	driver = None
	current_date = None


	def __init__(self):
		self.driver = webdriver.Firefox()
		self.driver.get("http://radioluz.pwr.edu.pl/")
		self.current_date = datetime.now().strftime('%d-%m-%Y')


	def getSongs(self):
		songs = []
		path = "/html/body/div[2]/div/section[3]/div/ul/"

		for i in range(1, 6):
			time = self.driver.find_element_by_xpath(f"{path}li[{i}]/time").text
			title = self.driver.find_element_by_xpath(f"{path}li[{i}]/div/p[1]").text
			artist = self.driver.find_element_by_xpath(f"{path}li[{i}]/div/p[2]").text
			songs.append(f'{time}  {artist} - {title}')

		return songs


	def main(self):
		songs = self.getSongs()
		with open(f'np_luz_{self.current_date}.txt', mode='a') as file:
		    file.write("\n".join(item for item in songs))
		    file.write("\n")

		self.driver.close()


if __name__ == "__main__":
	scrape = PlaylistScrapper()
	scrape.main()
