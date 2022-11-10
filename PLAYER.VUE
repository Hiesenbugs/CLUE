class Player 

{
    char colors = ["red","blue","green", "purple", "white", "yellow"]
    constructor(userId, gameId) {
      this.userId = userId;
      this.gameId = gameId;
    }
    initalizePlayerLocation(userId, gameId){
        let location = "";
        location = Board(userId, gameId).getLocation;
        return location;
    }
    getCharacterColor(){
        // Load the AWS SDK for Node.js
        var AWS = require('aws-sdk');
        // Set the region 
        AWS.config.update({region: 'REGION'});
        // Create the DynamoDB service object
        var ddb = new AWS.DynamoDB({apiVersion: '2012-08-10'});
        var params = {
        TableName: 'gameTable',
        Key: {
        'characterColor': {N: '001'}
        };
  ProjectionExpression: 'ATTRIBUTE_NAME'
};
        for (color in colors){
            if color exists in gamesTable with "userID"
                pass
                // how can I make the gamesTable visible in this class? 
            else:   
                inster into gamesTable with "userId"
            return color
        }
    }
    getPlayerCards(){
        let player_cardss = Board.getInitialCards
        return player_cards
    }
    
}
