<template>
  <div id="app">
    <h1>The Heisenbugs Present...</h1>
    <h2>CLUELESS</h2>
    <div id="joinLobbyButton">
      <input v-model="name" placeholder="Enter Name"/>
      <button :disabled="join > 0" @click="JoinLobby">Join Lobby</button>
      <figure>
        <img v-if="join > 0" src="character" alt="characterColor" width="100" height="100" />
      </figure>
    </div>
    <div id="startButton">
      <button :disabled="join != 1" @click="Start">Start</button>
    </div>
    <div id="playersInLobby"> <!-- constant update on this -->
      <span>{{lobbyCount}}</span>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      name: '',
      join: 0,
      character:'',
      characterColor:''
    };
  },
  methods: {
    async JoinLobby() {
      alert(`${this.name} has joined the game lobby.`)
      this.join++
      //Rand number for index of character out of array[characters]
      //Check if character is already assigned in player table
      //If statements for each character, assign character = ./assets/character.png and characterColor
      let axiosConfig = {
      headers: {
        'Content-Type': 'application/json',
        'Accept': "application/json",
      }
      };
      var payloadBody = {  'userId': "characterColor",  } //add boolean value for startLobby = true
      try {
      const response = await axios.post( `https://93cpkeoc1e.execute-api.us-east-1.amazonaws.com/lobby/join/`,
                                          payloadBody,
                                          axiosConfig
                                        )
      this.lobbyCount = response.data.ResponseMetadata.HTTPStatusCode //return total players in lobby
      } catch (e) {
      console.log("joinLobby Error:", e)
      }
    },
    async Start() {
      this.$router.push('/GamePage')
    }
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

