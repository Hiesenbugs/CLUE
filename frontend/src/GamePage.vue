<template>
  <div id="app">
    <div id="title">
      <h1>Adventure Time Clue!</h1>
      <div id="joinLobbyButton">
        <input v-model="this.userId" placeholder="Enter Name" />
        <button :disabled="lobbyJoined" @click="JoinLobby">Join Lobby</button>
      </div>
      <div id="startButton">
        <button :disabled="(lobbyCount < 2)" @click="StartGame">Start</button>
      </div>
      <div id="playersInLobby">
        <!-- constant update on this -->
        <h2>Lobby Count: {{ lobbyCount }} </h2>
        <h2>Start: {{ beginGame }} </h2>
      </div>
    </div>
    <div id="gameStateAlert" style="white-space: pre;">Game State: {{ gameStateAlert }}</div>
    <div id="playerLocation">Player Location: {{ playerLocation }}</div>
    <div class="turnButton">
      <button @click="EndTurn">End Turn</button>
    </div>
    <div id="suggestAccuseButton">
      <button @click="suggest(checkedSuspect, checkedWeapon, checkedRoom)">Suggestion</button>
    </div>
    <div id="suggestAccuseButton">
      <button @click="accuse(checkedSuspect, checkedWeapon, checkedRoom)">Accusation</button>
    </div>
    <div id="selected">
      <div id="selectedSuspect">
        <div v-for="suspect in suspects" v-bind:key="suspect">
          <input type="checkbox" :id="suspect" :value="suspect"
            :disabled="checkedSuspect.length > 0 && checkedSuspect.indexOf(suspect) === -1" v-model="checkedSuspect">
          <label :for="suspect">{{ suspect }}</label>
        </div>
      </div>
      <div id="selectedWeapon">
        <div v-for="weapon in weapons" v-bind:key="weapon">
          <input type="checkbox" :id="weapon" :value="weapon"
            :disabled="checkedWeapon.length > 0 && checkedWeapon.indexOf(weapon) === -1" v-model="checkedWeapon">
          <label :for="weapon">{{ weapon }}</label>
        </div>
      </div>
      <div id="selectedRoom">
        <div v-for="room in rooms" v-bind:key="room">
          <input type="checkbox" :id="room" :value="room"
            :disabled="checkedRoom.length > 0 && checkedRoom.indexOf(room) === -1" v-model="checkedRoom">
          <label :for="room">{{ room }}</label>
        </div>
      </div>
    </div>
    <div id="moveGrid">
      <div v-for="(row, idx1) in grid" v-bind:key="row">
        <input type="image" class="grid" :id="getGrid(idx1, idx2)" v-for="(col, idx2) in row" v-bind:key="col"
          @click="broadcastMessage(getGrid(idx1, idx2))" img :src="require(`${col}`)"
          :style="[getRoom(getGrid(idx1, idx2)) == 1 ? { 'width': '80px', 'height': '80px' } : { 'width': '50px', 'height': '40px' }]" />
      </div>
    </div>
    <div id="cardGrid">
      <figure class="card" v-for="hcard in playerHand" v-bind:key="hcard">
        <img :src="require(`${hcard.asset}`)" width="50" height="50" />
        <figcaption> {{ hcard.cardId }} - Hand </figcaption>
      </figure>
      <figure class="card" id="disproveCard" v-for="dcard in disproveCard" v-bind:key="dcard">
        <img v-if="disprove" :src="require(`${dcard.asset}`)" width="50" height="50" />
        <figcaption v-if="disprove"> {{ dcard.cardId }} - Disprove </figcaption>
      </figure>
    </div>
    <div>
      <textarea id="notebook" placeholder="Detective's Notebook"></textarea>
    </div>
  </div>
</template>

<script>
import ReconnectingWebSocket from 'reconnecting-websocket';

export default {
  name: "App",
  data() {
    return {
      playerTurn: '',
      userId: '',
      websocketResponse: '',
      lobbyCount: '',
      beginGame: '',
      lobbyJoined: false,
      gameStateAlert: [],
      playerHand: [],
      disproveCard: [],
      disprove: false,
      checkedSuspect: [],
      checkedWeapon: [],
      checkedRoom: [],
      suspects: ["Bmo",
        "Finn",
        "Jake",
        "Princess Bubblegum"],
      weapons: ["Axe Bass",
        "Demonic Wishing Eye",
        "Electrode Gun",
        "Finn Sword",
        "Gauntlet",
        "Mushroom Bomb"],
      rooms: ["Candy Kingdom",
        "Cotton Candy Forest",
        "Fire Kingdom",
        "Glass Kingdom",
        "Ice Kingdom",
        "Land of the Dead",
        "Lumpy Space",
        "Mystery Mountains",
        "Tree House"],
      grid: [["./assets/Candy_Kingdom.png", "./assets/Hallway.png", "./assets/Cotton_Candy_Forest.png", "./assets/Hallway.png", "./assets/Fire_Kingdom.png"],
      ["./assets/Hallway.png", "./assets/Hallway.png", "./assets/Hallway.png"],
      ["./assets/Glass_Kingdom.png", "./assets/Hallway.png", "./assets/Ice_Kingdom.png", "./assets/Hallway.png", "./assets/Land_of_the_Dead.png"],
      ["./assets/Hallway.png", "./assets/Hallway.png", "./assets/Hallway.png"],
      ["./assets/Lumpy_Space.png", "./assets/Hallway.png", "./assets/Mystery_Mountains.png", "./assets/Hallway.png", "./assets/TreeHouseINT.png"],],
      playerLocation: [],
      roomCoord: ['c0-0', 'c0-2', 'c0-4', 'c2-0', 'c2-2', 'c2-4', 'c4-0', 'c4-2', 'c4-4']
    };
  },
  methods: {
    setPlayerTurn() {
      try {
        this.playerTurn = "reached till here"
        console.log(this.playerTurn)
      } catch (error) {
        console.log(error)
      }
    },
    setInitalLocaiton() {
      this.playerLocation = ['c0-0']
    },
    setInitialCards() {
      this.playerHand = { cardId: "Bmo", asset: "./assets/bmo.png" }
    },
    Move() {
      this.playerLocation
      //this.gameStateAlert
    },
    MakeAccusation() {
      this.checkedSuspect
      this.checkedSuspect
      this.checkedRoom

      // get winning hand and match
      // return 

    },
    MakeSuggestion() {
      this.checkedSuspect
      this.checkedSuspect
      this.checkedRoom
    },
    JoinLobby: function () {
      this.lobbyJoined = true;
      this.connection.send(
        JSON.stringify({
          userId: this.userId,
          joinLobby: true,
          startGame: false,
          "action": "game"
        })
      );
    },
    StartGame: function () {
      this.connection.send(
        JSON.stringify({
          userId: this.userId,
          joinLobby: true,
          startGame: true,
          "action": "game"
        })
      );
    },
    getGrid(x, y) {
      this.xCoord = x;
      this.yCoord = y;
      return `c${this.xCoord}-${this.yCoord}`;
    },
    getRoom(coord) {
      if (coord == this.roomCoord[0]) {
        return 1;
      }
      else if (coord == this.roomCoord[1]) {
        return 1;
      }
      else if (coord == this.roomCoord[2]) {
        return 1;
      }
      else if (coord == this.roomCoord[3]) {
        return 1;
      }
      else if (coord == this.roomCoord[4]) {
        return 1;
      }
      else if (coord == this.roomCoord[5]) {
        return 1;
      }
      else if (coord == this.roomCoord[6]) {
        return 1;
      }
      else if (coord == this.roomCoord[7]) {
        return 1;
      }
      else if (coord == this.roomCoord[8]) {
        return 1;
      }
      else {
        return 0;
      }
    },
    broadcastMessage: function (coord) {
      this.connection.send(
        JSON.stringify({
          userId: this.userId,
          location: coord,
          "action": "game"
        })
      );
    }
  },
  watch: {
    beginGame() {
      if (this.beginGame == true) {
        this.setPlayerTurn()
        this.setInitalLocaiton()
        this.setInitialCards()
      }
    },
    immediate: true
  },
  created: function () {
    console.log("Starting connection to WebSocket Server")
    this.connection = new ReconnectingWebSocket("wss://4fa24d5qqf.execute-api.us-east-1.amazonaws.com/dev")
    this.connection.debug = true;
    this.connection.reconnectInterval = 4000;

    this.connection.onmessage = (event) => {
      let response = JSON.parse(event.data)
      console.log("Event Recieved from server", response);
      this.beginGame = response.message.startGame
      console.log("Start Game:", this.beginGame)
      this.lobbyCount = response.message.lobbyCount

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
};
</script>

<style scoped>
#app {
  width: 1700px;
  margin: 0 auto;
  position: absolute;
}

#title {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#gameStateAlert {
  position: relative;
  top: 75px;
  left: 350px;
}

#playerLocation {
  position: relative;
  top: 75px;
  left: 350px;
}

.turnButton {
  position: relative;
  top: 50px;
  left: 100px;
}

#notebook {
  width: 300px;
  min-height: 72px;
  padding: 2px;
  resize: vertical;
  overflow: hidden;
  background-color: transparent;
  border: 2px solid #000;
  border-radius: 4px;
  font-family: "Inconsolata", monospace;
  font-size: 1rem;
  color: #000;
  position: absolute;
  top: 0px;
  right: 0px;
  overflow-y: scroll;
}

#suggestAccuseButton {
  position: relative;
  display: inline-block;
  padding-left: 165px;
  bottom: 55px;
  left: 800px;
}

#selected {
  position: relative;
  display: flex;
  flex-direction: column;
  justify-content: top;
  align-items: center;
  bottom: 50px;
}

#selectedSuspect {
  position: absolute;
  left: 900px;
}

#selectedWeapon {
  position: absolute;
  left: 1055px;
}

#selectedRoom {
  position: absolute;
  left: 1225px;
}

#cardGrid {
  position: relative;
  top: 250px;
}

.card {
  display: inline-block;
}

#moveGrid {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  position: relative;
  top: 130px;
}

#c0-1 {
  position: relative;
  bottom: 20px;
}

#c0-3 {
  position: relative;
  bottom: 20px;
}

#c1-0 {
  position: relative;
  right: 80px;
  transform: rotate(270deg);
}

#c1-1 {
  transform: rotate(90deg);
}

#c1-2 {
  position: relative;
  left: 80px;
  transform: rotate(90deg);
}

#c2-1 {
  position: relative;
  bottom: 20px;
}

#c2-3 {
  position: relative;
  bottom: 20px;
}

#c3-0 {
  position: relative;
  right: 80px;
  transform: rotate(270deg);
}

#c3-1 {
  transform: rotate(270deg);
}

#c3-2 {
  position: relative;
  left: 80px;
  transform: rotate(90deg);
}

#c4-1 {
  position: relative;
  bottom: 20px;
}

#c4-3 {
  position: relative;
  bottom: 20px;
}
</style>

<!--  
Class Board {
    constructor(gameId) {
        this.gameId = gameId
    }

    const starting_positions = {};
    const room_cards = [];
    const player_cards = [];
    const weapon_cards = [];

    checkInitialLocaiton(){
        // if this gameid associated inital postion doesn't exists
        // return item_not_exisits (Item = {
                                    game_id = this.gameId this.gameId,
                                    pos = [x,y]) 
                                    in board table
    }
    
    getInitalLocaiton(){
        for pos in starting_postions:
            if (checkInitialLocaiton() is True) {
                // write gameid, pos into ddb initial positions list
                return position
            }
    }

    getInitialCards(){
        player_cards = []
            for card in room_card:
                pick a room_card,
                if doesn't exist in GameTable
                insert to GameTable with userId
            add room_card to player_cards

            for card in weapon_card:
                pick a weapon_card,
                if doesn't exist in GameTable
                insert to GameTable with userId
            add weapon_card to player_cards

            for card in player_cards:
                pick a player_card,
                if doesn't exist in GameTable
                    insert to GameTable with userId

        return player_cards
    }

    get winningCards() {
        winning_hand = getInitialCards
        write to boardTable
    }
    
}



class Player {

    char colors = ["red","blue","green"]
    constructor(userId) {
      this.userId = userId;
      this.gameId = gameId;
    }

    initalizePlayerLocation(gameId){
        let loction = ""

        location = Board(gameId).getLocation
        return locaiton
    }

    getCharacterColor(){
        for color in colors:
            if color exists in gamesTable with "userID"
                pass
            else:   
                inster into gamesTable with "userId"
        return color
    }

    getPlayerCards(){
        player_cards = Board.getInitialCards
        return player_cards
    }

    
  }


  Class PlayerAction {

    constructor(userId) {
        this.userId = userId
        this.gameId = gameId
    }

    roll dice(){
        // return random(1,12)
    }


    move(){
        change gameTable userId CharecterLocation 
    }

    suggestion (){

    }

    accusation (){

    }

    disproveCard() {


    }

    showDetectiveLog () {

    }

    getCurrentPlayerTurn(){
        userIds = []
        // scan GameTable and fill userIds
        // sort userIds by alphabet
        // call BoardTable and get currentPlayerTurn
        // if null:
             insert userIds[0] into ddb
            else:
                get userIds.index('currentPlayerTurn) in userIds
                insert userIds.index('currentPlayerTurn) next
    }

    endTurn (){

    }
}
-->


