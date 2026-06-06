import json
import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('url-shortener')

def lambda_handler(event, context):
    
    try:
        # Get the short code from the URL
        short_code = event['pathParameters']['shortCode']
    except:
        return {
            'statusCode': 400,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'error': 'Please provide a short code'})
        }
    
    # Look up the short code in DynamoDB
    response = table.get_item(Key={'shortCode': short_code})
    
    # If not found return 404
    if 'Item' not in response:
        return {
            'statusCode': 404,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'error': 'Short URL not found'})
        }
    
    # Get the original URL
    original_url = response['Item']['originalUrl']
    
    # Redirect to original URL
    return {
        'statusCode': 301,
        'headers': {
            'Location': original_url,
            'Access-Control-Allow-Origin': '*'
        },
        'body': ''
    }
