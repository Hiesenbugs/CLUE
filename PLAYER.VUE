class Player 

{
    char colors = ["red","blue","green", "purple", "white", "yellow"]
    constructor(userId, gameId) {
      this.userId = userId;
      this.gameId = gameId;
    }
    function initalizePlayerLocation(userId, gameId){
        let location = "";
        location = Board(userId, gameId).getLocation;
        return location;
    }
    function getCharacterColor(){
        // Load the AWS SDK for Node.js
        var AWS = require('aws-sdk');
        // Set the region 
        AWS.config.update({region: 'REGION'});
        // Create the DynamoDB service object
        var ddb = new AWS.DynamoDB({apiVersion: '2012-08-10'});// is the API version correct?
        var params = {
        TableName: 'gameTable',
        Key: {
        'userID': {N: '001'} // what is '001'?
        };
        ProjectionExpression: 'characterColor' // gets color attribute 
        };
        // Call DynamoDB to read the item from the table
        var color = ddb.getItem(params).promise()
        return color
    }
    function getPlayerCards(){
        let player_cardss = Board.getInitialCards
        return player_cards
    }
    
}
