<template>
  <div id="app">
    <h1>Adventure Time Clue!</h1>
  </div>
  <div class="turnButton">
    <button @click="Move">Move</button>
  </div>
  <div class="turnButton">
    <button @click="EndTurn">End Turn</button>
  </div>
  <div class="turnButton">
    <button @click="setDice">Roll Dice</button>
  </div>
  <div id="rollDice">
    <div :class="getDice"></div>
  </div>
  <div>
    <textarea id="notebook" placeholder="Detective's Notebook"></textarea>
  </div>
  <div id="suggestionButton">
    <button @click="Suggestion">Suggestion</button>
  </div>
  <div id="accusationButton">
    <button @click="Accusation">Accusation</button>
  </div>
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
  <div id="moveGrid">
    <div v-for="(row, idx1) in coord" v-bind:key="row">
      <button :id="getGrid(idx1, idx2)" v-for="(col, idx2) in row" v-bind:key="col" v-bind:style="color"></button>
    </div>
  </div>
  <div id="roomGrid">
    <button v-for="room in roomIds" v-bind:key="room" :id="room" @click="printToConsole(room)"></button>
  </div>
</template>

<script>
//import axios from 'axios';

export default {
  name: "App",
  data() {
    return {
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
      rooms: ["Candy Kingdom",
        "Cotton Candy Forest",
        "Fire Kingdom",
        "Glass Kingdom",
        "Ice Kingdom",
        "Land of the Dead",
        "Lumpy Space",
        "Mystery Mountains",
        "Tree House"],
      roomIds: ["CandyKingdom",
        "CottonCandyForest",
        "FireKingdom",
        "GlassKingdom",
        "IceKingdom",
        "LandoftheDead",
        "LumpySpace",
        "MysteryMountains",
        "TreeHouse"],
      coord: [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
      [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
      [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
      [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
      [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
      [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
      [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
      [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
      [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
      [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
      [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
      [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
      [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
      [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
      [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
      [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
      [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
      ],

      color: "red",

      xtest: [5, 5, 5, 5, 5, 5, 17, 17, 6, 6, 6, 6, 6, 6, 6, 17, 17, 6, 6, 6, 6, 6, 6]
    };
  },
  methods: {
    getGrid(x, y) {
      this.xCoord = x;
      this.yCoord = y;
      return `c${this.xCoord}-${this.yCoord}`;
    },
    printToConsole: function (x) {
      console.log(x)
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
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

#CandyKingdom {
  position: relative;
  bottom: 650px;
  left: 350px;
  width: 75px;
  height: 75px;
}

#CottonCandyForest {
  position: relative;
  bottom: 650px;
  left: 542px;
  width: 75px;
  height: 75px;
}

#FireKingdom {
  position: relative;
  bottom: 650px;
  left: 735px;
  width: 75px;
  height: 75px;
}

#GlassKingdom {
  position: relative;
  bottom: 450px;
  left: 670px;
  width: 75px;
  height: 75px;
}

#IceKingdom {
  position: relative;
  bottom: 250px;
  left: 585px;
  width: 75px;
  height: 75px;
}

#LandoftheDead {
  position: relative;
  bottom: 250px;
  left: 242px;
  width: 75px;
  height: 75px;
}

#LumpySpace {
  position: relative;
  bottom: 250px;
  right: 100px;
  width: 75px;
  height: 75px;
}

#MysteryMountains {
  position: relative;
  bottom: 400px;
  right: 185px;
  width: 75px;
  height: 75px;
}

#TreeHouse {
  position: relative;
  bottom: 500px;
  right: 260px;
  width: 75px;
  height: 75px;
}

#moveGrid {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  position: relative;
  bottom: 250px;
}

#accusationButton {
  position: relative;
  bottom: 122px;
  left: 1100px;
}

#suggestionButton {
  position: relative;
  bottom: 100px;
  left: 900px;
}

#selectedSuspect {
  position: relative;
  bottom: 100px;
  left: 800px;
}

#selectedWeapon {
  position: relative;
  bottom: 180px;
  left: 955px;
}

#selectedRoom {
  position: relative;
  bottom: 297px;
  left: 1125px;
}

.turnButton {
  position: relative;
  top: 50px;
  left: 50px;
}

#notebook {
  width: 300px;
  min-height: 72px;
  padding: 2px;
  resize: none;
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
}

#rollDice {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.dice {
  display: inline-block;
  min-height: 1em;
  padding-left: 1em;
  background-size: 1em;
  background-repeat: no-repeat;
  font-size: 3em;
  position: relative;
  top: 50px;
  right: 450px;
}

.dice-1 {
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg' version='1.1' viewBox='0 0 76.5 76.5' height='21.6' width='21.6'%3E%3Cg transform='translate(113.25%2C-494.1)'%3E%3Cg transform='matrix(0.5%2C0%2C0%2C0.5%2C-406.5%2C374.7)'%3E%3Crect x='588' y='240.4' width='150' height='150' ry='50' rx='50' style='fill%3A%23fff%3Bstroke-width%3A3%3Bstroke%3A%23000'%2F%3E%3Ccircle transform='translate(337.5%2C87.5)' cx='325' cy='227.4' r='12.5' style='fill%3A%23000%3Bstroke-width%3A3%3Bstroke%3A%23000'%2F%3E%3C%2Fg%3E%3C%2Fg%3E%3C%2Fsvg%3E ");
}

.dice-2 {
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg' version='1.1' viewBox='0 0 76.5 76.5' height='21.6' width='21.6'%3E%3Cstyle%3E.s0%7Bfill%3A%23000%3Bstroke-width%3A3%3Bstroke%3A%23000%3B%7D%3C%2Fstyle%3E%3Cg transform='translate(109.9%2C-505.1)'%3E%3Cg transform='matrix(0.5%2C0%2C0%2C0.5%2C-415.6%2C485.6)'%3E%3Crect x='613' y='40.4' width='150' height='150' ry='50' rx='50' style='fill%3A%23fff%3Bstroke-width%3A3%3Bstroke%3A%23000'%2F%3E%3Ccircle transform='translate(326.5%2C-148.5)' cx='325' cy='227.4' r='12.5' class='s0'%2F%3E%3Ccircle transform='translate(398.5%2C-76.5)' cx='325' cy='227.4' r='12.5' class='s0'%2F%3E%3C%2Fg%3E%3C%2Fg%3E%3C%2Fsvg%3E ");
}

.dice-3 {
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg' version='1.1' viewBox='0 0 76.5 76.5' height='21.6' width='21.6'%3E%3Cstyle%3E.s0%7Bfill%3A%23000%3Bstroke-width%3A3%3Bstroke%3A%23000%3B%7D%3C%2Fstyle%3E%3Cg transform='translate(84.9%2C-515.5)'%3E%3Cg transform='matrix(0.5%2C0%2C0%2C0.5%2C-290.6%2C514.9)'%3E%3Crect x='413' y='2.9' width='150' height='150' ry='50' rx='50' style='fill%3A%23fff%3Bstroke-width%3A3%3Bstroke%3A%23000'%2F%3E%3Ccircle transform='translate(126.5%2C-186)' cx='325' cy='227.4' r='12.5' class='s0'%2F%3E%3Ccircle transform='translate(198.5%2C-114)' cx='325' cy='227.4' r='12.5' class='s0'%2F%3E%3Ccircle transform='translate(162.5%2C-150)' cx='325' cy='227.4' r='12.5' class='s0'%2F%3E%3C%2Fg%3E%3C%2Fg%3E%3C%2Fsvg%3E ");
}

.dice-4 {
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg' version='1.1' viewBox='0 0 76.5 76.5' height='21.6' width='21.6'%3E%3Cstyle%3E.s0%7Bfill%3A%23000%3Bstroke-width%3A3%3Bstroke%3A%23000%3B%7D%3C%2Fstyle%3E%3Cg transform='translate(90.7%2C-499.7)'%3E%3Cg transform='matrix(0.5%2C0%2C0%2C0.5%2C-302.7%2C367.8)'%3E%3Crect x='425.5' y='265.4' width='150' height='150' ry='50' rx='50' style='fill%3A%23fff%3Bstroke-width%3A3%3Bstroke%3A%23000'%2F%3E%3Ccircle transform='translate(139%2C76.5)' cx='325' cy='227.4' r='12.5' class='s0'%2F%3E%3Ccircle transform='translate(139%2C148.5)' cx='325' cy='227.4' r='12.5' class='s0'%2F%3E%3Ccircle transform='translate(211%2C76.5)' cx='325' cy='227.4' r='12.5' class='s0'%2F%3E%3Ccircle transform='translate(211%2C148.5)' cx='325' cy='227.4' r='12.5' class='s0'%2F%3E%3C%2Fg%3E%3C%2Fg%3E%3C%2Fsvg%3E ");
}

.dice-5 {
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg' version='1.1' viewBox='0 0 76.5 76.5' height='21.6' width='21.6'%3E%3Cstyle%3E.s0%7Bfill%3A%23000%3Bstroke-width%3A3%3Bstroke%3A%23000%3B%7D%3C%2Fstyle%3E%3Cg transform='translate(89.2%2C-510.5)'%3E%3Cg transform='matrix(0.5%2C0%2C0%2C0.5%2C-194.9%2C372.3)'%3E%3Crect x='213' y='277.9' width='150' height='150' ry='50' rx='50' style='fill%3A%23fff%3Bstroke-width%3A3%3Bstroke%3A%23000'%2F%3E%3Ccircle transform='translate(-73.5%2C89)' cx='325' cy='227.4' r='12.5' class='s0'%2F%3E%3Ccircle transform='translate(-73.5%2C161)' cx='325' cy='227.4' r='12.5' class='s0'%2F%3E%3Ccircle transform='translate(-1.5%2C89)' cx='325' cy='227.4' r='12.5' class='s0'%2F%3E%3Ccircle transform='translate(-1.5%2C161)' cx='325' cy='227.4' r='12.5' class='s0'%2F%3E%3Ccircle transform='translate(-37.5%2C125)' cx='325' cy='227.4' r='12.5' class='s0'%2F%3E%3C%2Fg%3E%3C%2Fg%3E%3C%2Fsvg%3E ");
}

.dice-6 {
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg' version='1.1' viewBox='0 0 76.5 76.5' height='21.6' width='21.6'%3E%3Cstyle%3E.s0%7Bfill%3A%23000%3Bstroke-width%3A3%3Bstroke%3A%23000%3B%7D%3C%2Fstyle%3E%3Cg transform='translate(86.2%2C-500.6)'%3E%3Cg transform='matrix(0.5%2C0%2C0%2C0.5%2C-98.2%2C356.2)'%3E%3Crect x='25.5' y='290.4' width='150' height='150' ry='50' rx='50' style='fill%3A%23fff%3Bstroke-width%3A3%3Bstroke%3A%23000'%2F%3E%3Ccircle transform='translate(-261%2C101.5)' cx='325' cy='227.4' r='12.5' class='s0'%2F%3E%3Ccircle transform='translate(-261%2C173.5)' cx='325' cy='227.4' r='12.5' class='s0'%2F%3E%3Ccircle transform='translate(-261%2C137.5)' cx='325' cy='227.4' r='12.5' class='s0'%2F%3E%3Ccircle transform='translate(-189%2C101.5)' cx='325' cy='227.4' r='12.5' class='s0'%2F%3E%3Ccircle transform='translate(-189%2C173.5)' cx='325' cy='227.4' r='12.5' class='s0'%2F%3E%3Ccircle transform='translate(-189%2C137.5)' cx='325' cy='227.4' r='12.5' class='s0'%2F%3E%3C%2Fg%3E%3C%2Fg%3E%3C%2Fsvg%3E");
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






