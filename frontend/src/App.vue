<template>
  <img alt="Heisenbug logo" src="./assets/heisenbug.png">
  <LandingPage msg="Clue App by Heisenbugs"/>
  <img alt="RedPawn logo" src="./assets/redplayer.png">
  <PlayerAction msg="red player"/>
</template>

<script>
import LandingPage from './components/LandingPage.vue'
import PlayerAction from './components/PlayerAction.vue'

export default {
  name: 'App',
  components: {
    LandingPage,
    PlayerAction
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
