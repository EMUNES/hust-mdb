<template>
  <material-list :events="events"></material-list>
  <div>
    <button v-if="page > 1" @click="pageDown">|-|</button>
    <span>current page: {{page}}</span>
    <button @click="pageUp">|+|</button>
  </div>
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
    const page = ref(1)
    const events = ref([])
    const store = useStore()

    const pageDown = () => {
      page.value -= 1
    }

    const pageUp = () => {
      page.value += 1
    }

    onBeforeMount(() => {
      axios.get(store.state.backendAPIs.coreAPI, {
        headers: {

        }
      })
        .then(res => {
          events.value = res.data.results
        })
          .catch(err => {console.error(err)})
    })

    return {
      page,
      events,
      pageDown,
      pageUp
    }
  },
}
</script>

<style>

</style>