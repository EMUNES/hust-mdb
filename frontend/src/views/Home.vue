<template>
  <navigation></navigation>
  <h1>{{ testMsg }}</h1>
  <h2 class="text-red-500">tailwind is working!</h2>

  <p>
    <a href="https://vitejs.dev/guide/features.html" target="_blank">Vite Documentation</a> |
    <a href="https://v3.vuejs.org/" target="_blank">Vue 3 Documentation</a>
  </p>

  <button @click="count++">count is: {{ count }}</button>
  <p>
    Edit
    <code>components/HelloWorld.vue</code> to test hot module replacement.
  </p>
</template>

<script>
import Navigation from '../components/Navigation.vue';

export default {
  name: 'Home',

  components: {
    Navigation
  },
  
  props: {
    msg: {
      type: String,
    }
  },

  data () {
    return {
      count: 0,
      testMsg: this.$store.state.msg
    }
  }
}
</script>

<style scoped>
a {
  color: #42b983;
}
</style>