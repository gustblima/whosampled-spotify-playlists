

def handler(event, context):

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }
    return response

