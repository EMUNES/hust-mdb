<template>
  <material-list :events="events"></material-list>
  <Paginator :totalPages="totalPages" @page-updated="updateRequestPage" />
</template>

<script>
import axios from '../request/axios.js';
import MaterialList from '../components/materials/MaterialList.vue'
import Paginator from '../components/Paginator.vue'
import { onBeforeMount, ref, watch } from 'vue';
import { useStore } from 'vuex';

export default {
  name: 'Materials',

  components: {
    MaterialList,
    Paginator
  },

  setup(_, context) {
    const requestPage = ref(1)
    const totalPages = ref(0)
    const events = ref([])
    const store = useStore()

    const updateRequestPage = (e) => {
      requestPage.value = e.page.value
    }

    onBeforeMount(() => {
      axios.get(store.state.backendAPIs.coreAPI, {
        headers: {}
      })
        .then(res => {
          console.log("request")
          events.value = res.data.results
          totalPages.value = res.data.total_pages
        })
          .catch(err => {console.error(err)})
    })

    watch (requestPage, (newValue, _) => {
      axios.get(store.state.backendAPIs.coreAPI + `?page=${newValue}`, {
        headers: {}
      })
        .then(res => {
          events.value = res.data.results
        })
          .catch(err => {console.log(err)})
    })

    return {
      requestPage,
      totalPages,
      events,
      updateRequestPage
    }
  }
}
</script>

<style>

</style>