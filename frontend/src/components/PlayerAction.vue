<template>
  <div class="playerAction">
    <h1>{{ msg }}</h1>
  </div>
</template>

<script>
export default {
  name: 'PlayerAction',
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 100px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #d61111;
}
</style>
