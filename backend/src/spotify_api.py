import requests
import json

spotify_api = 'https://api.spotify.com'

class SpotifyApi:
    
    def __init__(self, token):
        if token:
            self.token = token
        else:
            raise
            
    def create_playlist(self, playlist_name):
        url = '{api}/v1/playlists'.format(api = spotify_api)
        params = {
            "name": "{playlist_name} samples".format(playlist_name = playlist_name),
            "description": "Created by playlist samples",
            "public": True
        }
        return requests.post(url = url, params = params, headers = auth_headers())


    def add_tracks_to_playlist(self, playlist_id, tracks):
        url = '{api}/v1/playlists/{playlist_id}/tracks'.format(api = spotify_api, playlist_id = playlist_id)
        params = {
            'uris': ','.join(tracks)
        }
        return requests.post(url = url, params = params, headers = auth_headers())


    def get_playlist_tracks(self, playlist_id):
        url = '{api}/v1/playlists/{playlist_id}/tracks'.format(api = spotify_api, playlist_id = playlist_id)
        return requests.get(url = url, headers = auth_headers())


    def search_track(self, track_name, track_artist):
        url = '{api}/v1/search'.format(url = spotify_api)
        params = {
            'q': '{name} {artist}'.format(name = track_name, artist = track_artist),
            'type': 'track',
            'limit': 1
        }
        return requests.get(url = url, params = params, headers = auth_headers())
        

    def auth_headers (self):
        return {
            'Authorization': 'Bearer ' + self.token
        }