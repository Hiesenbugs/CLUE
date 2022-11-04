class Lobby {
    constructor(userId) {
      this.userId = userId;
    }

    joinLobby(){
        // 1.  ddb.put_item(this.userId)
        // 2.  lobby_count = dd.get_count(userId)

        return lobby_count
    }

    startGame(){
        // 1. ddb.put_item(Item = {"userID" = this.userID, startGame = True})  
        // 2. dict = ddb.scan("lobby-table-dev")
        //    for keys,vals in dict.items():
        //      if false in vals:
        //        return false
        //      else:
        //            let game_Id = random_number(0-1000)
        //            for player in keys:
        //              player_object = Player(userId, gameId)
        //              load player_object in new GamePage
        //              load player_object + game_Id in GameTable
        //              create winning hand Board.winningHand
        //              redirect to new GamePage         
    }

  }


