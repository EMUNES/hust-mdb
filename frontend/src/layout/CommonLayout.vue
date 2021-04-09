// This is the common layout with sidebar and heabar

<template>
  <general-header></general-header>
  <div class="nav flex items-start">  
    <!-- transition here is set for common layout -->
    <transition appear
    enter-active-class="transition duration-1000 ease-out"
    leave-active-class="transition duration-200 ease-out"
    enter-from-class="opacity-0 scale-70"
    enter-to-class="opactiy-100 scale-100"
    leave-from-class="opacity-100 scale-100"
    leave-to-class="opacity-0 scale-70">
      <side-bar v-if="sidebar"></side-bar>
    </transition>
    
    <div class="w-full">
      <transition appear
      enter-active-class="transition duration-500 ease-out"
      enter-from-class="opacity-0 scale-70"
      enter-to-class="opactiy-100 scale-100">
        <head-bar :sidebarShowing="sidebar" @udpate:sidebarShowing="sidebar=$event">
          <template #func-head>
            <slot name="func-head">
            </slot>
          </template>
        </head-bar>
      </transition>
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