import os
import json
import re
import boto3
from fastapi import FastAPI
from pydantic import BaseModel
from mangum import Mangum
from dynamodb_json import json_util as json

import logging


logging.basicConfig(level = logging.INFO)
logger = logging.getLogger()


class Item(BaseModel):
    userId: str
    location: str

app = FastAPI()
dynamodb_client = boto3.client('dynamodb')
GAME_TABLE = os.environ['GAME_TABLE']


@app.get("/")
async def root():
    return "Clue Game Endpoint"


@app.get("/player/location/get/{user_id}")
async def get_player_position(user_id: str):
    result = dynamodb_client.get_item(
        TableName=GAME_TABLE, Key={'userId':{'S': user_id}}
    )
    logger.info(result)
    return json.loads(result['Item'])

@app.post("/player/location/set/")
async def get_player_position(item: Item):
    print(item)
    result = dynamodb_client.put_item(
        TableName=GAME_TABLE, Item={'userId': {'S': item.userId}, 'location': {'S': item.location}}
    )
    logger.info(result)
    return result


if os.environ.get('IS_OFFLINE'):
    dynamodb_client = boto3.client(
        'dynamodb', region_name='localhost', endpoint_url='http://localhost:8000'
    )

handler = Mangum(app)
