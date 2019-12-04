import json
from backend.src.spotify_api import SpotifyApi

def handler(event, context):
    query_params = json.loads(event)['queryStringParameters']
    spotify = SpotifyApi(query_params['token'])
    playlist_id = query_params["playlist_id"]

    if playlist_id:
        has_next = True
        items = []
        limit = 50
        offset = 0
        while has_next:
            page = spotify.get_playlist_tracks(playlist_id, limit, offset)
            items.append(page['items'])
            has_next = page['next']
            offset += 1
        return  {
            "statusCode": 200,
            "body": json.dumps(items)
        }
