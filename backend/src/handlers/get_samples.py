import json
from src.whosampled_scrape import WhoSampledScrape

def handler(event, context):
    print(event)
    query_params = event['queryStringParameters']
    
    if query_params and "tracks" in query_params:
        tracks = query_params['tracks'].split(';')
        scrape = WhoSampledScrape()
        samples = []
        for track in tracks:
            samples.append(scrape.get_samples_from_track_search(track))

        return response(200, json.dumps(samples))

    return response(500)

def response(code, body = None):
    return {
        "statusCode": code,
        "body": body
    }