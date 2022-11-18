<template>
  <div id="app">
    <div id="title">
      <h1>Adventure Time Clue!</h1>
    </div>
    <div id="gameStateAlert">Game State: {{ gameStateAlert }}</div>
    <div id="playerLocation">Player Location: {{ playerLocation }}</div>
    <div class="turnButton">
      <button @click="EndTurn">End Turn</button>
    </div>
    <div id="suggestAccuseButton">
      <button @click="printAccusationToConsole(checkedSuspect, checkedWeapon, checkedRoom)">Suggestion</button>
    </div>
    <div id="suggestAccuseButton">
      <button @click="printAccusationToConsole(checkedSuspect, checkedWeapon, checkedRoom)">Accusation</button>
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
          <input type="checkbox" :id="room.name" :value="room.name"
            :disabled="checkedRoom.length > 0 && checkedRoom.indexOf(room.name) === -1" v-model="checkedRoom">
          <label :for="room.name">{{ room.name }}</label>
        </div>
      </div>
    </div>
    <div id="moveGrid">
      <div v-for="(row, idx1) in coord" v-bind:key="row">
        <button class="grid" :id="getGrid(idx1, idx2)" v-for="(col, idx2) in row" v-bind:key="col"
          :style="[getRoom(getGrid(idx1, idx2)) == 1 ? { 'background': 'grey' } : { 'background': 'orange' }]"
          @click="broadcastMessage(getGrid(idx1, idx2))">></button>
      </div>
    </div>
    <div id="cardGrid">
      <figure class="card" v-for="hcard in playerHand" v-bind:key="hcard">
        <img :src="require(`${hcard.asset}`)" width="50" height="50" />
        <figcaption> {{ hcard.cardId }} - Hand </figcaption>
      </figure>
      <figure id="disproveCard" v-for="dcard in disproveCard" v-bind:key="dcard">
        <img v-if="disproveCard.length != 0" :src="require(`${dcard.asset}`)" width="50" height="50" />
        <figcaption v-if="disproveCard.length != 0"> {{ dcard.cardId }} - Disprove </figcaption>
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
      gameStateAlert: [],
      playerHand: [{ cardId: "AxeBassCard", asset: "./assets/Axe_Bass.png" },
      { cardId: "BmoCard", asset: "./assets/bmo.png" },
      { cardId: "CandyKingdomCard", asset: "./assets/Candy_Kingdom.png" },
      { cardId: "CottonCandyForestCard", asset: "./assets/Cotton_Candy_Forest.png" }],
      disproveCard: [{ cardId: "DemonicWishingEyeCard", asset: "./assets/Demonic_Wishing_Eye.png" }],
      checkedSuspect: [],
      checkedWeapon: [],
      checkedRoom: [],
      diceNum: 1,
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
      rooms: [{ roomId: "CandyKingdom", name: "Candy Kingdom" },
      { roomId: "CottonCandyForest", name: "Cotton Candy Forest" },
      { roomId: "FireKingdom", name: "Fire Kingdom" },
      { roomId: "GlassKingdom", name: "Glass Kingdom" },
      { roomId: "IceKingdom", name: "Ice Kingdom" },
      { roomId: "LandoftheDead", name: "Land of the Dead" },
      { roomId: "LumpySpace", name: "Lumpy Space" },
      { roomId: "MysteryMountains", name: "Mystery Mountains" },
      { roomId: "TreeHouse", name: "Tree House" }],
      cards: [{ cardId: "BmoCard", asset: "./assets/bmo.png" },
      { cardId: "FinnCard", asset: "./assets/finn.png" },
      { cardId: "JakeCard", asset: "./assets/jake.png" },
      { cardId: "PrincessBubblegumCard", asset: "./assets/princess_bubblegum.png" },
      { cardId: "AxeBassCard", asset: "./assets/Axe_Bass.png" },
      { cardId: "DemonicWishingEyeCard", asset: "./assets/Demonic_Wishing_Eye.png" },
      { cardId: "ElectrodeGunCard", asset: "./assets/Electrode_Gun.png" },
      { cardId: "FinnSwordCard", asset: "./assets/Finn_Sword.png" },
      { cardId: "GauntletCard", asset: "./assets/Gauntlet.png" },
      { cardId: "MushroomBombCard", asset: "./assets/Mushroom_Bomb.png" },
      { cardId: "CandyKingdomCard", asset: "./assets/Candy_Kingdom.png" },
      { cardId: "CottonCandyForestCard", asset: "./assets/Cotton_Candy_Forest.png" },
      { cardId: "FireKingdomCard", asset: "./assets/Fire_Kingdom.png" },
      { cardId: "GlassKingdomCard", asset: "./assets/Glass_Kingdom.png" },
      { cardId: "IceKingdomCard", asset: "./assets/Ice_Kingdom.png" },
      { cardId: "LandoftheDeadCard", asset: "./assets/Land_of_the_Dead.png" },
      { cardId: "LumpySpaceCard", asset: "./assets/Lumpy_Space.png" },
      { cardId: "MysteryMountainsCard", asset: "./assets/Mystery_Mountains.png" },
      { cardId: "TreeHouseCard", asset: "./assets/TreeHouseINT.png" }],
      coord: [[0, 1, 2, 3, 4],
      [0, 1, 2, 3, 4],
      [0, 1, 2, 3, 4],
      [0, 1, 2, 3, 4],
      [0, 1, 2, 3, 4],
      ],
      roomCoord: ["c0-0", "c0-2", "c0-4", "c2-4", "c4-4", "c4-2", "c4-0", "c2-0", "c2-2"],
      playerLocation: ["c2-2"],
    };
  },
  methods: {
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
    printToConsole: function (x) {
      console.log(x)
    },
    printAccusationToConsole: function (a, b, c) {
      console.log('Suspect: ' + a + '; Weapon: ' + b + '; Room: ' + c)
    },
    setRandomDiceData() {
      const randomDiceNum = Math.floor(Math.random() * 6) + 1;
      this.diceNum = randomDiceNum;
    },
    setDice() {
      let count = 0;
      const timer = setInterval(() => {
        this.setRandomDiceData();
        if (count >= 6) {
          clearInterval(timer);
        }
        count += 1;
      }, 150);
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
  created: function () {
    console.log("Starting connection to WebSocket Server")
    this.connection = new ReconnectingWebSocket("wss://662507chgd.execute-api.us-east-1.amazonaws.com/dev")
    this.connection.debug = true;
    this.connection.reconnectInterval = 4000;

    this.connection.onmessage = (event) => {
      let response = JSON.parse(event.data)
      console.log("Event Recieved from server", response);
      this.playerLocation = response.message.location
      this.gameStateAlert = 'Player has moved to ' + response.message.location
      console.log("Location:", this.playerLocation)
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
  computed: {
    getDice() {
      this.setRandomDiceData();
      return `dice dice-${this.diceNum}`;
    }
  },
  watch: {
    diceNum() {
      console.log("Dice rolled!");
    }
  }
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
  display: inline-block;
}

.card {
  display: inline-block;
  position: relative;
  top: 250px;
}

#disproveCard {
  position: relative;
  bottom: -140px;
  left: 1100px;
}

#moveGrid {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  position: relative;
  top: 130px;
}

.grid {
  height: 80px;
  width: 80px;
}

#c0-0:after {
  content: 'Candy Kingdom';
}
#c0-2:after {
  content: 'Cotton Candy Forest';
}
#c0-4:after {
  content: 'Fire Kingdom';
}
#c2-4:after {
  content: 'Glass Kingdom';
}
#c4-4:after {
  content: 'Ice Kingdom';
}
#c4-2:after {
  content: 'Land of the Dead';
}
#c4-0:after {
  content: 'Lumpy Space';
}
#c2-0:after {
  content: 'Mystery Mountains';
}
#c2-2:after {
  content: 'Tree House';
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


