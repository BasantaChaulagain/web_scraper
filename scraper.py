from bs4 import BeautifulSoup
import json
import requests


class Scraper(object):
	url=""
	content=""
	tweetArr=[]

	def __init__(self):
		self.url="http://ethans_fake_twitter_site.surge.sh/"
		
	def scrape(self):
		try:
			response=requests.get(self.url, timeout=5)
			self.content=BeautifulSoup(response.content, "html.parser")
			
			for tweet in self.content.findAll('div', attrs={"class":"tweetcontainer"}):
				tweetObject = {
					"author": tweet.find('h2', attrs={"class": "author"}).text,
					"date": tweet.find('h5', attrs={"class": "dateTime"}).text,
					"tweet": tweet.find('p', attrs={"class": "content"}).text,
					"likes": tweet.find('p', attrs={"class": "likes"}).text,
					"shares": tweet.find('p', attrs={"class": "shares"}).text
				}
				self.tweetArr.append(tweetObject)

			with open('twitterData.json', 'w') as outfile:
				json.dump(self.tweetArr, outfile)

		except Exception as e:
			print ("cannot scrape")
			print (e)

	def parse(self):
		with open('twitterData.json', 'r') as file:
			json_data=json.load(file)

		for i in json_data:
			if 'obama' in i['tweet'].lower():
				print(i)


def main():
	sc=Scraper()
	sc.scrape()
	sc.parse()


if __name__=="__main__":
	main()