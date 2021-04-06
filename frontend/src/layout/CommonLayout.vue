// This is the common layout with sidebar and heabar

<template>
  <general-header></general-header>
  <div class="nav flex items-start">  
    <side-bar></side-bar>

    <div class="w-full">
      <head-bar>
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

export default {
  name: 'CommonBodyLayut',
  components: {
    GeneralHeader,
    HeadBar,
    SideBar
  }
}
</script>

<style>

</style>