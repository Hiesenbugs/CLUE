<template>
  <div id="app">
    <h1>The Heisenbugs Present...</h1>
    <h2>CLUELESS</h2>
    <div class="Join-Lobby">
      <input v-model="name" placeholder="Enter Name"/>
      <button :disabled="join > 0" @click="JoinLobby">Join Lobby</button>
      <figure>
        <img v-if="join > 0" src="character" alt="characterColor" width="100" height="100" />
      </figure>
    </div>
    <div class="Start-Game">
      <button :disabled="LobbyCount != 4" @click="Start">Start</button>
    </div>
    <div class="Players-In-Lobby"> <!-- constant update on this -->
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
    }
  },
  methods: {
    async JoinLobby(event) {
      alert(`${this.name} has joined the game lobby.`)
      if (event) {
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
        console.log("setLocation Error:", e)
        }
      }
    },
    Start() {
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
