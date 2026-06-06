import json
import boto3
import string
import random

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('url-shortener')

def generate_short_code():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=6))

def lambda_handler(event, context):
    
    try:
        body = json.loads(event['body'])
        original_url = body['url']
    except:
        return {
            'statusCode': 400,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'error': 'Please provide a URL'})
        }
    
    # Generate unique short code
    short_code = generate_short_code()
    
    # Save to DynamoDB
    table.put_item(Item={
        'shortCode': short_code,
        'originalUrl': original_url,
        'createdAt': str(__import__('datetime').datetime.now())
    })
    
    return {
        'statusCode': 200,
        'headers': {'Access-Control-Allow-Origin': '*'},
        'body': json.dumps({
            'shortCode': short_code,
            'shortUrl': f'Use your API URL + /{short_code}'
        })
    }
