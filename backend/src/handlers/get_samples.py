import json
from whosampled_scrape import WhoSampledScrape

def handler(event, context):

    query_params = json.loads(event)['queryStringParameters']
    tracks = query_params['tracks']
    
    if tracks:
        scrape = WhoSampledScrape()
        result = list(scrape.create_samples_list(tracks.split(',')))
        return {
            "statusCode": 200,
            "body": json.dumps(result)
        }
