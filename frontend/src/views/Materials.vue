<template>
  <material-list :events="events"></material-list>
</template>

<script>
import axios from '../request/axios.js';
import MaterialList from '../components/materials/MaterialList.vue'
import { onBeforeMount, ref } from 'vue';
import { useStore } from 'vuex';

export default {
  name: 'Materials',

  components: {
    MaterialList,
  },

  setup() {
    const events = ref([])
    const store = useStore()

    onBeforeMount(() => {
      axios.get(store.state.backendAPIs.coreAPI, {
        headers: {

        }
      })
        .then(res => {
          events.value = res.data.results
          console.log(events.value)
        })
          .catch(err => {console.error(err)})
    })

    return {
      events,
    }
  },
}
</script>

<style>

</style>