import json
from backend.src.whosampled_scrape import create_samples_list

def handler(event, context):

    query_params = json.loads(event)['queryStringParameters']
    tracks = query_params['tracks']
    if tracks:
        result = list(create_samples_list(tracks.split(',')))
        return {
            "statusCode": 200,
            "body": json.dumps(result)
        }
