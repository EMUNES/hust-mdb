// This is the common layout with sidebar and heabar

<template>
  <general-header></general-header>
  <div class="nav flex items-start">  
    <side-bar v-if="sidebar"></side-bar>

    <div class="w-full">
      <head-bar :sidebarShowing="sidebar" @udpate:sidebarShowing="sidebar=$event">
        <template #func-head>
          <slot name="func-head">
          </slot>
        </template>
      </head-bar>
      <slot name="content">
        
      </slot>
    </div>
  </div>
</template>

<script>
import GeneralHeader from '../components/GeneralHeader.vue';
import HeadBar from '../components/bars/HeadBar.vue';
import SideBar from '../components/bars/SideBar.vue';
import { ref } from 'vue';

export default {
  name: 'CommonLayout',
  components: {
    GeneralHeader,
    HeadBar,
    SideBar
  },
  setup() {
    const sidebar = ref(true)

    return {
      sidebar
    }
  }
}
</script>

<style>

</style>