import os
import boto3
from fastapi import FastAPI
from pydantic import BaseModel
from mangum import Mangum


import logging

logging.basicConfig(level = logging.INFO)
logger = logging.getLogger()

# Clients
app = FastAPI()
dynamodb_client = boto3.client('dynamodb')

# Environment Variables
GAME_TABLE = os.environ['GAME_TABLE']


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/player/location/get/{user_id}")
async def get_player_position(user_id: int):
    result = dynamodb_client.get_item(
        TableName=GAME_TABLE, Key={'userId': {'S': user_id}}
    )
    logger.info(result)
    return {"response": result}

class Item(BaseModel):
    userId: str
    location: str


@app.post("/player/location/set/")
async def get_player_position(item: Item):
    result = dynamodb_client.put_item(
        TableName=GAME_TABLE, Item=item
    )
    logger.info(result)
    return {"response": result}


if os.environ.get('IS_OFFLINE'):
    dynamodb_client = boto3.client(
        'dynamodb', region_name='localhost', endpoint_url='http://localhost:8000'
    )

handler = Mangum(app)
