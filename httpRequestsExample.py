# Example for how to use http requests module to save data from a webpage.

import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.raise_for_status()
playFile = open('Romeo and Juliet.txt', 'wb')
for chunk in res.iter_content(100000):
	playFile.write(chunk)
playFile.close()
