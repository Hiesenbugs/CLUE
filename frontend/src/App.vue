<template>
  <div id="app">
    <h1>The Heisenbugs Present...</h1>
    <h2>CLUELESS</h2>
    <div id="joinLobbyButton">
      <input v-model="this.userId" placeholder="Enter Name" />
      <button :disabled="lobbyCount > 3" @click="JoinLobby">Join Lobby</button>
    </div>
    <div id="startButton">
      <button :disabled="startGameCount === lobbyCount" @click="StartGame">Start</button>
    </div>
    <div id="playersInLobby">
      <!-- constant update on this -->
    <h2>Lobby Count: {{lobbyCount}} </h2>  
    <h2>Start Game: {{startGame}} </h2>  
    <h2>Start Game Count: {{startGameCount}} </h2>  

    </div>
  </div>
</template>

<script>
import ReconnectingWebSocket from 'reconnecting-websocket';

export default {
  data: function () {
    return {
      userId: '',
      websocketResponse: '',
      lobbyCount: '',
      startGame: '',
      startGameCount: ''
    }
  },
  methods: {
    JoinLobby: function () {
      this.connection.send(
        JSON.stringify({
          userId: this.userId,
          joinLobby: true,
          startGame: false,
          "action": "lobby"
        })
      );
    },
    StartGame: function () {
      this.connection.send(
        JSON.stringify({
          userId: this.userId,
          joinLobby: true,
          startGame: true,
          "action": "lobby"
        })
      );
    }
  },
  created: function () {
    console.log("Starting connection to WebSocket Server")
    this.connection = new ReconnectingWebSocket("wss://aej0yks5r9.execute-api.us-east-1.amazonaws.com/dev")
    this.connection.debug = true;
    this.connection.reconnectInterval = 4000;

    this.connection.onmessage = (event) => {
      let response = JSON.parse(event.data)
      console.log("Event Recieved from server", response);
      this.startGame = response.message.startGame
      console.log("Start Game:", this.startGame)
      this.lobbyCount = response.message.lobbyCount
      this.startGameCount = response.message.startGameCount

      console.log("Lobby Count:", this.lobbyCount)
    }

    this.connection.onopen = (event) => {
      console.log(event)
      console.log("Successfully connected to the echo websocket server...")
    }

    this.connection.onerror = function (err) {
      console.error('Socket encountered error: ', err.message, 'Closing socket');
      this.connection.close();
    }
  },
  watch: function() {

  }
}

</script>

<style scoped>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>

<!--  
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
-->

