import json
import requests
import unicodecsv
from datetime import date

writer = unicodecsv.writer(open('doodles.csv', 'w'))
writer.writerow(['title', 'url', 'year', 'month', 'day'])

base_url = "http://www.google.com/doodles/json/"
for x in range(1998, date.today().year+1):
	old_url = base_url + str(x) + '/'
	for x in range (1, 13):
		new_url = old_url + str(x)
		
		response = requests.get(new_url)
		data = json.loads(response.content)

		for x in data[0:]:
			title = x['title']
			url = 'http:' + x['url']
			year = x['run_date_array'][0]
			month = x['run_date_array'][1]
			day = x['run_date_array'][2]
			writer.writerow([title, url, year, month, day])