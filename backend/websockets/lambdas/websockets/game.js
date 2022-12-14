const AWS = require('aws-sdk');
const ddb = new AWS.DynamoDB.DocumentClient();

let apiGatewayManagementApi;
const gameTableName = process.env.gameTableName;
const apiVersion = '2018-11-29';

function initApiGatewayManagementApi(event) {
    apiGatewayManagementApi = new AWS.ApiGatewayManagementApi({
        apiVersion,
        endpoint: event.requestContext.domainName + '/' + event.requestContext.stage
    });
}

async function send(connectionId, data) {
    if (apiGatewayManagementApi) {
        await apiGatewayManagementApi.postToConnection({
            ConnectionId: connectionId,
            Data: data
        }).promise();
    }
}

function getConnections() {
    return ddb.scan({ TableName: gameTableName }).promise();
}

function writeToTable(connectionId, message) {
    return ddb.put({
        TableName: gameTableName,
        Item: {
            connectionId: connectionId,
            userId: message.userId,
            joinLobby: message.joinLobby,
            startGame: message.startGame
        }
    }).promise();
}

exports.handler = (event, context, callback) => {
    initApiGatewayManagementApi(event);
    let message = JSON.parse(event.body);
    const connectionId = event.requestContext.connectionId;


    writeToTable(connectionId, message).then(() => {
        getConnections().then((data) => {
            console.log(data);

            let lobbyCount = 0;
            let startGame = true;

            data.Items.forEach(item => {
                if (item.joinLobby) {
                    message.lobbyCount = ++lobbyCount;
                };// count of dynamodb table rows
            });

            data.Items.forEach(item => {
                startGame = startGame && item.startGame;
            });
            
            message.startGame = startGame

            data.Items.forEach(function (connection) {
                send(
                    connection.connectionId,
                    JSON.stringify(
                        {
                            message: message
                        }
                    ));
            });
            callback(null, { statusCode: 200 });
        });
    });
};



