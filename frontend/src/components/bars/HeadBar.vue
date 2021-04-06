<template>
  <!-- headbar -->
  <nav class="flex flex-auto justify-between items-center border-2">
    <ul class="flex rounded p-1 m-1">
      <!-- this button controls the sidebar, default showing sidebar. -->
      <button @click="toggleSideBar" class="ml-3 mr-4">
        <span class="sr-only">Menu Bar</span>
        <svg class="h-6 w-6" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
          <path fill-rule="evenodd" d="M3 5a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 10a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 15a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1z" clip-rule="evenodd" />
        </svg>
      </button>

      <router-link to="/" class="global-link">
        首页
      </router-link>
      <router-link to="/materials" class="global-link">
        热塑性材料信息
      </router-link>
    </ul>
    <ul class="function">
      <slot name="func-head">
        
      </slot>
    </ul>
  </nav>
</template>

<script>
import { toRef } from 'vue'
export default {
  name: "HeadBar",
  props: {
    sidebarShowing: {
      required: false,
      type: Boolean,
    }
  },
  emits: [
    'udpate:sidebarShowing'
  ],
  setup(props, context) {
    const sidebarShowing = toRef(props, 'sidebarShowing')

    const toggleSideBar = () => {
      console.log(!sidebarShowing.value)
      context.emit('udpate:sidebarShowing', !sidebarShowing.value)
    }

    return {
      toggleSideBar
    }
  }
}
</script>

<style>
.global-link {
  @apply border-2 border-gray-400 py-1 px-2 mx-1 rounded-lg;
}
</style>