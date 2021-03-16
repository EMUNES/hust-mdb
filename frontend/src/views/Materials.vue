<template>
  <div class="flex flex-auto justify-between items-center border-2">
    <div class="text-white rounded-md bg-blue-400 p-1 hover:bg-blue-300 m-1">
      bar
    </div>
    <div class="function">
      <button @click="toggleShowFilter"
      class="text-white rounded-md bg-blue-400 p-1 hover:bg-blue-300 m-1">
      Filter
      </button>
      <button @click="toggleShowFilter"
      class="text-white rounded-md bg-blue-400 p-1 hover:bg-blue-300 m-1">
      Search
      </button>
    </div>
  </div>
  <Filter :showing="showFilter" @close-filter="toggleShowFilter" @add-filter="requestFilter"/>
  <material-list :events="events"></material-list>
  <Paginator :totalPages="totalPages" @page-updated="updateRequestPage" />
</template>

<script>
import axios from '../request/axios.js';
import MaterialList from '../components/materials/MaterialList.vue'
import Paginator from '../components/Paginator.vue'
import Filter from '../components/Filter.vue'
import { onBeforeMount, ref, watch } from 'vue';
import { useStore } from 'vuex';

export default {
  name: 'Materials',

  components: {
    MaterialList,
    Paginator,
    Filter
  },

  setup(_, context) {
    const requestPage = ref(1)
    const totalPages = ref(0)
    const events = ref([])
    const store = useStore()
    const showFilter = ref(false)

    const updateRequestPage = (e) => {
      requestPage.value = e.page.value
    }

    const toggleShowFilter = () => {
      showFilter.value = !showFilter.value
    }

    const requestFilter = () => {
      toggleShowFilter()
      axios.get(store.state.backendAPIs.filterAPI, {
        headers: {}
      })
        .then(res => {
          events.value = res.data.results
        })
          .catch(err => {console.log(err)})
    }

    onBeforeMount(() => {
      axios.get(store.state.backendAPIs.coreAPI, {
        headers: {}
      })
        .then(res => {
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
      showFilter,
      requestPage,
      totalPages,
      events,
      toggleShowFilter,
      requestFilter,
      updateRequestPage
    }
  }
}
</script>

<style>

</style>