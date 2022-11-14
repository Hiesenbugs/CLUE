const AWS = require('aws-sdk');

const create = (domainName, stage) => {
    const endpoint = `${domainName}/${stage}`;
    return new AWS.ApiGatewayManagementApi({
        apiVersion: '2018-11-29',
        endpoint,
    });
};

const send = ({ domainName, stage, connectionID, message }) => {
    const ws = create(domainName, stage);

    const postParams = {
        Data: message,
        ConnectionId: connectionID,
    };

    return ws.postToConnection(postParams).promise();
};

const broadcast = ({ domainName, stage, connections, message }) => {

    const ws = create(domainName, stage);

    connections.forEach(async connection => {
        const postParams = {
            Data: message,
            ConnectionId: connection,
        };
        await ws.postToConnection(postParams);
    });
};

module.exports = {
    send,
    broadcast,
};
