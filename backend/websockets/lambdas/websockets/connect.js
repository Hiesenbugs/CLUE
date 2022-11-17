const AWS = require('aws-sdk');
const ddb = new AWS.DynamoDB.DocumentClient();

const lobbyTableName = process.env.lobbyTableName;

function addConnection(connectionId) {
    return ddb.put({
        TableName: lobbyTableName,
        Item: {
            connectionId: connectionId
        }
    }).promise();
}

exports.handler = (event, context, callback) => {
    const connectionId = event.requestContext.connectionId;
    addConnection(connectionId).then(() => {
        callback(null, { statusCode: 200 });
    });
};


