<template>
  <div class="landing">
    <h1>{{ msg }}</h1>
    <p>
      Skeletal System Demo
    </p>
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
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 10;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
