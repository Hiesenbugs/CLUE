const AWS = require('aws-sdk');

const documentClient = new AWS.DynamoDB.DocumentClient();

const Dynamo = {
    async get(connectionId, TableName) {
        const params = {
            TableName,
            Key: {
                connectionId,
            },
        };
        const data = await documentClient.get(params).promise();
        if (!data || !data.Item) {
            throw Error(`There was an error fetching the data for connectionId of ${connectionId} from ${TableName}`);
        }
        console.log(data);
        return data.Item;
    },

    async write(data, TableName) {
        if (!data.connectionId) {
            throw Error('no connectionId on the data');
        }
        const params = {
            TableName,
            Item: data,
        };
        const res = await documentClient.put(params).promise();
        if (!res) {
            throw Error(`There was an error inserting connectionId of ${data.connectionId} in table ${TableName}`);
        }
        return data;
    },

    async delete(connectionId, TableName) {
        const params = {
            TableName,
            Key: {
                connectionId,
            },
        };
        return documentClient.delete(params).promise();
    },

    async get_all_connection_ids(TableName) {
        const params = {
            TableName: TableName,
            ProjectionExpression: 'connectionId'
        }
        return documentClient.scan(params).promise();
    }

};
module.exports = Dynamo;
