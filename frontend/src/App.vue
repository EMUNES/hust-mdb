<template>
  <router-view />
</template>

<script>

import HeadBar from './components/bars/HeadBar.vue';

export default {
  name: 'App',
  components: {
    HeadBar,
  }
}

// This starter template is using Vue 3 experimental <script setup> SFCs
// Check out https://github.com/vuejs/rfcs/blob/script-setup-2/active-rfcs/0000-script-setup.md
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2e3e55;
}
</style>