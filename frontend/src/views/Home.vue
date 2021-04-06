<template>
  <general-header></general-header>
  <!-- <div class="nav flex items-start">  
    <side-bar></side-bar>

    <div class="w-full">
      <head-bar></head-bar>
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
    </div>
  </div> -->
  <common-layout>
    <template #func-head>
      test
    </template>

    <template #content>
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
  </common-layout>
</template>

<script>
import CommonLayout from '../layout/CommonLayout.vue'; 

export default {
  name: 'Home',

  components: {
    CommonLayout
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