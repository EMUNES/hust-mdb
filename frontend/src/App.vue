<template>
  <div>
      <header class="text-center">
        <h2 class="text text-3xl">
          华中科技大学
        </h2>

        <h4 class="text text-2xl">
          材料学院
        </h4>

        <h4 class="text text-2xl">
          热塑性材料数据库
        </h4>
      </header>
      
    <router-link to="/">
      首页
    </router-link> | 


    <router-link to="/materials">
      热塑性材料信息
    </router-link>
    
    <router-view />
  </div>
</template>

<script>

import Navigation from './components/Navigation.vue';

export default {
  name: 'App',
  components: {
    Navigation,
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
  color: #2c3e50;
  margin-top: 60px;
}
</style>