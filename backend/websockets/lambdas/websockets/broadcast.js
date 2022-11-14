const Responses = require('../common/API_Responses');
const Dynamo = require('../common/Dynamo');
const WebSocket = require('../common/websocketMessage');

const tableName = process.env.tableName;

exports.handler = async event => {
    console.log('event', event);
    const { connectionId, domainName, stage } = event.requestContext;
    const body = JSON.parse(event.body);
    const message = body.message;

    try {
        // update the connectionId record in DDB with latest message 
        const data = {
            connectionId,
            domainName,
            stage,
            message
        };

        await Dynamo.write(data, tableName);

        const connections = Dynamo.get_all_connection_ids(tableName);
        console.log("All connection Ids:", connections);
        // Broadcast the message to all a Response back 
        WebSocket.broadcast({
            domainName,
            stage,
            connections,
            message: message,
        });
        console.log('sent message');

        return Responses._200({ message: 'got a message' });
    } catch (error) {
        return Responses._400({ message: 'message could not be received' });
    }
};
