import json
from backend.src.spotify_api import SpotifyApi

def handler(event, context):
    query_params = json.loads(event)['queryStringParameters']
    spotify = SpotifyApi(query_params['token'])
    playlist_id = query_params["playlist_id"]
    if playlist_id:
        tracks = spotify.get_playlist_tracks(playlist_id)
        return {
            "statusCode": 200,
            "body": json.dumps(tracks)
        }
