import json
import logging
from hello import Hello

log = logging.getLogger()
log.setLevel(logging.DEBUG)


def hello(event, context):
    result = Hello.runHello('hey')

    try:
        response = {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": 'OPTIONS, GET',
            },
            # "body": json.dumps(result, ensure_ascii=False, indent='\t')
            "body": result
        }
    except KeyError:
        response = {
            "statusCode": 400,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": 'OPTIONS, GET',
            },
            "body": "400 Bad request"
        }

    return response
