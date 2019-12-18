import json
from src.whosampled_scrape import WhoSampledScrape
max_tracks_allowed_per_request = 5
def handler(event, context):
    print(event)
    query_params = event['queryStringParameters']
    
    if query_params and "tracks" in query_params:
        tracks = query_params['tracks'].split(';')
        if len(tracks) < max_tracks_allowed_per_request:
            scrape = WhoSampledScrape()
            samples = []
            for track in tracks:
                samples.append(scrape.get_samples_from_track_search(track))

            return response(200, json.dumps(samples))

    return response(500)

def response(code, body = None):
    return {
        "statusCode": code,
        "headers": {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Credentials': True,
        },
        "body": body
    }