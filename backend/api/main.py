import os
import json
import re
import boto3
from fastapi import FastAPI
from pydantic import BaseModel
from mangum import Mangum
from dynamodb_json import json_util as json

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "*",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

import logging


logging.basicConfig(level = logging.INFO)
logger = logging.getLogger()


class Item(BaseModel):
    userId: str
    location: str


dynamodb_client = boto3.client('dynamodb')
GAME_TABLE = os.environ['GAME_TABLE']
BOARD_TABLE = os.environ['BOARD_TABLE']


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


class Lobby(BaseModel):
    userId: str
    location: str

@app.post("/player/lobby/set/")
async def set_player_details(item: Item):
    print(item)
    result = dynamodb_client.put_item(
        TableName=GAME_TABLE, Item={'userId': {'S': item.userId}, 'location': {'S': item.location}}
    )
    logger.info(result)
    return result

@app.get("/player/lobby/")
async def start_lobby(item: Item):
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

class Board:
    game_id: str
    user_id: str

@app.post("/player/initial_location")
async def get_initial_location(board: Board):
    result = dynamodb_client.get_item(
        TableName=GAME_TABLE, Key={'userId':{'S': board.user_id}, 'gameId':{'S': board.game_id}}
    )
    logger.info(result)
    return json.loads(result['CharacterLocation'])

@app.get("/player/initial_cards")
async def get_initial_cards(board: Board):
    result = dynamodb_client.get_item(
        TableName=GAME_TABLE, Item={'userId': {'S': board.user_id}, 'gameId': {'S': board.game_id}}
    )
    return result

@app.get("/winning_hand")
async def get_winning_hand(game_id: str):
    result = dynamodb_client.get_item(
        TableName=BOARD_TABLE, Key={'gameId':{'S': game_id}}
    )
    return json.loads(result['winningHand'])


if os.environ.get('IS_OFFLINE'):
    dynamodb_client = boto3.client(
        'dynamodb', region_name='localhost', endpoint_url='http://localhost:8000'
    )

class Player(BaseModel):
    userId: str
    gameId: str

@app.post("/player/initialize")
async def initialize_player_location(player: Player):
    result = dynamodb_client.put_item(
        TableName=GAME_TABLE, Item={'userId': {'S': player.userId}, 'gameId': {'S': player.gameId}}
    )
    logger.info(result)
    return result

@app.get("/player/color")
async def get_character_color(player: Player):
    result = dynamodb_client.get_item(
        TableName=GAME_TABLE, Item={'userId': {'S': player.userId}, 'gameId': {'S': player.gameId}}
    )
    logger.info(result)
    return json.loads(result['CharacterColor'])

@app.get("/player/cards")
async def get_player_cards(player: Player):
    result = dynamodb_client.get_item(
        TableName=GAME_TABLE, Item={'userId': {'S': player.userId}, 'gameId': {'S': player.gameId}}
    )
    cards_array = []
    cards_array.append(json.loads(result['weaponCard']))
    cards_array.append(json.loads(result['roomCard']))
    cards_array.append(json.loads(result['playerCard']))
    return cards_array


if os.environ.get('IS_OFFLINE'):
    dynamodb_client = boto3.client(
        'dynamodb', region_name='localhost', endpoint_url='http://localhost:8000'
    )


handler = Mangum(app)
