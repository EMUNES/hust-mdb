<template>
  <div>
    <h1>当前显示表格</h1>
    <div v-for="event in events" :key="event">
      <span>{{ event.id }}</span> | 
      <span>{{ event.mark }}</span> | 
      <span>{{ event.series }}</span> | 
      <span>{{ event.manufacturer }}</span>
    </div>
  </div>
</template>

<script>
import MaterialDetail from "./MaterialDetail.vue"

export default {
  name: "MaterialList",

  props: {
    events: Array
  },

  components: {
    MaterialDetail,
  },
}
</script>

<style>

</style>