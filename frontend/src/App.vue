<template>
  <div id="app">
    <h1>Hiesenbugs Clue Game</h1>

    <div class="get-player-location">
      <input type="radio" v-model="getPlayerLocation" @keydown.enter="getLocation">
      <button @click="getLocation">GetLocation</button>
      <span>{{playerLocation}}</span>
    </div>

    <div class="set-player-location">
      <input type="text" v-model="setPlayerLocation" @keydown.enter="setLocation">
      <button @click="setLocation">SetLocation</button>
      <span>setPlayerLocationResponseCode: {{setPlayerLocationResponseCode}}</span>
    </div>

    <figure>
      <img src="./assets/bmo.png" alt="bmo" width="100" height="100" />
      <figcaption> Green Player </figcaption>
    </figure>

  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'App',
  components: {},
  data() {
    return {
      getPlayerLocation: '',
      setPlayerLocation: '',
      playerLocation: '',
      setPlayerLocationResponseCode: '',
    }
  },
  methods: {
    async getLocation() {
      let user_id = "greenplayer";
      try {
        const response = await axios.get(`https://93cpkeoc1e.execute-api.us-east-1.amazonaws.com/player/location/get/${user_id}`)
        this.playerLocation = response.data
      } catch (e) {
        console.log("getLocation Error:", e)
      }
    },
    async setLocation() {
      let axiosConfig = {
        headers: {
          'Content-Type': 'application/json',
          'Accept': "application/json",
        }
      };
      var payloadBody = {  'userId': "greenplayer", 
                    'location': this.setPlayerLocation 
                  }

      try {
        const response = await axios.post( `https://93cpkeoc1e.execute-api.us-east-1.amazonaws.com/player/location/set/`,
                                            payloadBody,
                                            axiosConfig
                                            )
      this.setPlayerLocationResponseCode = response.data.ResponseMetadata.HTTPStatusCode
      } catch (e) {
        console.log("setLocation Error:", e)
      }
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