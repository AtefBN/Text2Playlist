import requests
import json

api_key = 'NmQ5N2I1YWQtZWU4Zi00ZTJkLTgwZjAtYjM0OGZkOTc1ZDJk'
username = raw_input('Please set the username: ')
playlist_name = raw_input('Please enter playlist name: ')
found = False
r = requests.get('http://api.napster.com/v2.0/members/'+username+'?apikey='+api_key)
GUID = r.json()['members'][0]['id']
HEADERS = {'Content-type': 'application/json', 'Accept': 'text/plain'}


r = requests.get('http://api.napster.com/v2.0/members/'+GUID+'/library/playlists?apikey='+api_key)
print('For user {} found {} public playlists'.format(username, r.json()['meta']['totalCount']))

for playlist in r.json()['playlists']:
	if playlist_name == playlist['name']:
		print('Playlist already exists!')
		found = True
		playlist_id = playlist['id']
		break
if not found: 
	print('Playlist does not exist, creating...')
	create_playlist(playlist_name)




def create_playlist(name):
	playlist = Dict()
	playlist['playlists']['name'] = name
	playlist['playlists']['privacy'] = public
	playlist['playlists']['tracks'] = []
	r = requests.post('api.napster.com', json.dumps(playlist), headers = HEADERS, auth=api_key)



