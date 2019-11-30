import json
from backend.src.spotify_api import SpotifyApi

def handler(event, context):
    event = json.loads(event)
    spotify = SpotifyApi(event['queryStringParameters']['token'])
    playlist = spotify.create_playlist(event['body']['playlistName'])
    
    return {
        "statusCode": 200,
        "body": json.dumps(playlist)
    }
