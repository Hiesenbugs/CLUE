const AWS = require('aws-sdk');
const ddb = new AWS.DynamoDB.DocumentClient();

let apiGatewayManagementApi;
const lobbyTableName = process.env.lobbyTableName;
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
    return ddb.scan({ TableName: lobbyTableName }).promise();
}

function writeToTable(connectionId, message) {
    return ddb.put({
        TableName: lobbyTableName,
        Item: {
            connectionId: connectionId,
            message: message
        }
    }).promise();
}

exports.handler = (event, context, callback) => {
    initApiGatewayManagementApi(event);
    let message = JSON.stringify({ message: JSON.parse(event.body).message.message });
    const connectionId = event.requestContext.connectionId;

    writeToTable(connectionId, message).then(() => {
        callback(null, { statusCode: 200 });
    });

    getConnections().then((data) => {
        data.Items.forEach(function (connection) {
            send(connection.connectionId, message);
        });
        callback(null, { statusCode: 200 })
    });
};



