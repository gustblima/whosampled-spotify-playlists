import json
from backend.src.whosamples_scrape import create_sample_list

def handler(event, context):

    body = json.loads(event)['body']
    result = list(create_sample_list(body['tracks']))
    return {
        "statusCode": 200,
        "body": json.dumps(result)
    }
