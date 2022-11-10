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
