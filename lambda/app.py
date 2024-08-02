import json


def lambda_handler(event, context):
    # Print the event to the logs
    print(json.dumps(event))

    # Return a simple message
    return {
        'statusCode': 200,
        'body': json.dumps('Event printed successfully!')
    }
