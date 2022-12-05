const AWS = require('aws-sdk');
const ddb = new AWS.DynamoDB.DocumentClient();

const gameTableName = process.env.gameTableName;

function addConnection(connectionId) {
    return ddb.put({
        TableName: gameTableName,
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


