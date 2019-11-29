import json
from backend.src.spotify_api import SpotifyApi

def handler(event, context):

    body = json.loads(event)['body']
    spotify = SpotifyApi(body['token'])
   
    # wip
    return {
        "statusCode": 200,
        "body": json.dumps(tracks)
    }
