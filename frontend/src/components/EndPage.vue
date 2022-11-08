<template>
  <div id="end">
    <h1>
      {{ winner }} has won!
    </h1>
    <div class="Replay">
      <button @click="Replay">Replay</button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      winner: '',
    }
  },
  methods: {
    //Get winner and update winner before page load
    Replay() {
      this.$router.push('/LandingPage')
    }
  }
}
</script>

<style scoped>
#end {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
