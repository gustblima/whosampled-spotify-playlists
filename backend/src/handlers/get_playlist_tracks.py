import json
from backend.src.spotify_api import SpotifyApi

def handler(event, context):

    body = json.loads(event)['body']
    spotify = SpotifyApi(body['token'])
    tracks = spotify.get_playlist_tracks(body['playlist_id'])

    return {
        "statusCode": 200,
        "body": json.dumps(tracks)
    }
