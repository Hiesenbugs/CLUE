import os
import logging
import boto3
from fastapi import FastAPI
from pydantic import BaseModel
from mangum import Mangum
from dynamodb_json import json_util as json
from fastapi.middleware.cors import CORSMiddleware
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

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

dynamodb_client = boto3.client('dynamodb')
GAME_TABLE = os.environ['GAME_TABLE']
BOARD_TABLE = os.environ['BOARD_TABLE']
LOBBY_TABLE = os.environ['LOBBY_TABLE']


@app.get("/")
async def root():
    return "Clue Game Endpoint"


class Lobby(BaseModel):
    userId: str
    startLobby: str

# Lobby Methods

@app.post("/player/lobby/join")
async def join_lobby(item: Lobby):
    logger.info("Join Lobby Method")
    logger.info("Received Item: %s", item)
    response = dynamodb_client.put_item(
        TableName=LOBBY_TABLE, Item={'userId': {
            'S': item.userId}, 'startLobby': {'S': item.startLobby}}
    )
    logger.info(response)
    return response

@app.post("/player/lobby/start")
async def start_lobby(item: Lobby):
    logger.info("Start Lobby Method")
    logger.info("Received Item: %s", item)
    response = dynamodb_client.put_item(
        TableName=LOBBY_TABLE, Item={'userId': {
            'S': item.userId}, 'startLobby': {'S': item.startLobby}}
    )
    logger.info(response)
    return response


@app.get("/player/lobby/count")
async def get_lobby_count():
    logger.info("Get Lobby Count Method")
    response = dynamodb_client.scan(TableName=LOBBY_TABLE)
    table_count = len(response['Items'])
    logger.info(response)
    return table_count


handler = Mangum(app)
