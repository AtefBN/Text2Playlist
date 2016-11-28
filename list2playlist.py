import requests
from urlparse import urljoin

base_url = 'api.github.com'
version = 'v2.0'
api_key = 'NmQ5N2I1YWQtZWU4Zi00ZTJkLTgwZjAtYjM0OGZkOTc1ZDJk'
dir_file = 'list.txt'
number_of_songs = 0
number_of_results = 0
with open(dir_file) as open_file:
	for line in open_file:
		number_of_songs += 1
		print('Processing track: '+line)
		line = line.replace(' ', '%20')
		query = 'http://api.napster.com/'+version+'/search?apikey='+api_key+'&q='+line+'&type=track&limit=1'
		#query = 'http://api.napster.com/v2.0/search?apikey='+api_key+'&q=weezer&type=artist'
		print('Contacting Napster API...')
		r = requests.get(query)
		print(r.json())

		if r.status_code == requests.codes.ok and r.json()['meta']['totalCount'] > 0:
			print('Some songs found for: ' + line.replace('%20', ' '))
			number_of_results += 1
		else: 
			print('No match found for: {}.'.format(line.replace('%20', ' ')))
print('Finished finding {} outta {}'.format(number_of_results, number_of_songs))
