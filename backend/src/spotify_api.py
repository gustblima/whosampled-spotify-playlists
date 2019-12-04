import requests
import json


class SpotifyApi:
    
    __api = 'https://api.spotify.com'

    def __init__(self, token):
        if token:
            self.token = token
        else:
            raise
            
    def create_playlist(self, playlist_name):
        url = '{api}/v1/playlists'.format(api = self.__api)
        data = {
            "name": "{playlist_name} samples".format(playlist_name = playlist_name),
            "description": "Created by playlist samples",
            "public": True
        }
        return requests.post(url = url, data = data, headers = self.__auth_headers())


    def add_tracks_to_playlist(self, playlist_id, tracks):
        url = '{api}/v1/playlists/{playlist_id}/tracks'.format(api = self.__api, playlist_id = playlist_id)
        params = {
            'uris': ','.join(tracks)
        }
        return requests.post(url = url, params = params, headers = self.__auth_headers())


    def get_playlist_tracks(self, playlist_id, limit, offset = 0):
        url = '{api}/v1/playlists/{playlist_id}/tracks'.format(api = self.__api, playlist_id = playlist_id)
        params = {
            limit: limit,
            offset: offset
        }
        return requests.get(url = url, params = offset, headers = self.__auth_headers())


    def search_track(self, track_name, track_artist):
        url = '{api}/v1/search'.format(url = self.__api)
        params = {
            'q': '{name} {artist}'.format(name = track_name, artist = track_artist),
            'type': 'track',
            'limit': 1
        }
        return requests.get(url = url, params = params, headers = self.__auth_headers())
        

    def __auth_headers (self):
        return {
            'Authorization': 'Bearer ' + self.token
        }