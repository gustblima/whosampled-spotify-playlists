import json
from backend.src.spotify_api import SpotifyApi

def handler(event, context):

    body = json.loads(event)['body']
    spotify = SpotifyApi(body['token'])
    playlist = spotify.create_playlist(body['playlistName'])
    
    return {
        "statusCode": 200,
        "body": json.dumps(playlist)
    }
