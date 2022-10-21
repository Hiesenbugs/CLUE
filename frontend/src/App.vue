<template>
  <div id="app">
    <h1>Hiesenbugs Clue Game</h1>

    <div class="get-player-location">
      <input type="radio" v-model="getPlayerLocation" @keydown.enter="getLocation">
      <button @click="getLocation">GetLocation</button>
    </div>

    <div class="get-player-location-response">
      <span>{{setPlayerLocationResponse}}</span>
    </div>

    <div class="set-player-location">
      <input type="text" v-model="setPlayerLocation" @keydown.enter="setLocation">
      <button @click="setLocation">SetLocation</button>
    </div>

    <div class="set-player-response">
      <span>{{setPlayerLocationResponse}}</span>
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
      setPlayerLocationResponse: '',
    }
  },
  methods: {
    async getLocation() {
      let user_id = "greenplayer";
      try {
        const response = await axios.get(`https://93cpkeoc1e.execute-api.us-east-1.amazonaws.com/player/location/get/${user_id}`)
        this.playerLocation = response.data
      } catch (e) {
        this.errors.push(e)
      }
    },
    async setLocation() {
      try {
        const response = await axios.post(`https://93cpkeoc1e.execute-api.us-east-1.amazonaws.com/player/location/set/`, {
          body: {'userId':"greenplayer", 'location': this.setPlayerLocation}
        })
        this.setPlayerLocationResponse = response.data
      } catch (e) {
        this.errors.push(e)
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