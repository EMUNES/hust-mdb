<template>
  <div class="flex flex-auto justify-between items-center border-2">
    <div class="text-white rounded-md bg-blue-400 p-1 hover:bg-blue-300 m-1">
      bar
    </div>
    <div class="function">
      <button @click="initPagination"
      class="text-white rounded-md bg-blue-400 p-1 hover:bg-blue-300 m-1">
        Init
      </button>
      <button @click="toggleShowFilter"
      class="text-white rounded-md bg-blue-400 p-1 hover:bg-blue-300 m-1">
        Filter
      </button>
      <div 
      class="search inline-block mx-2">
        <input type="text" placeholder="Search..." v-model="searchContent" @keydown.enter="requestSearch"
        class="border-2 rounded-full w-24 outline-none">
        <button @click="requestSearch"
        class="text-white rounded-md bg-blue-400 p-1 hover:bg-blue-300 m-1">
          Search
        </button>
      </div>
    </div>
  </div>
  <Filter :showing="showFilter" @close-filter="toggleShowFilter" @add-filter="requestFilter"/>
  <material-list :events="events"></material-list>
  <Paginator :initPage="initPage" :totalPages="totalPages" @page-updated="updateRequestPage" />
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
    const initPage = ref(false)
    const searchContent = ref('')

    // A general request method to connect backend API.
    const dataRequest = (_, backendURL=store.state.backendAPIs.coreAPI) => {
      axios.get(backendURL, {
        headers: {}
      })
        .then(res => {
          events.value = res.data.results
          totalPages.value = res.data.total_pages
        })
          .catch(err => {console.error(err)})
    }

    // Open/Close the filter form.
    const toggleShowFilter = () => {
      showFilter.value = !showFilter.value
    }

    // Update page content with page number.
    const updateRequestPage = (e) => {
      requestPage.value = e.page.value
    }
    
    // Init this view.
    const initPagination = () => {
      initPage.value = true
      dataRequest()
    }

    // Request filter API.
    const requestFilter = () => {
      initPage.value = true
      toggleShowFilter()
      dataRequest(_, store.state.backendAPIs.filterAPI)
    }

    // Request search API.
    const requestSearch = () => {
      initPage.value = true
      dataRequest(_, store.state.backendAPIs.searchAPI + searchContent.value)
      searchContent.value = ''
    }

    // Page initializtion.
    onBeforeMount(() => {
      dataRequest()
    })

    // If the page number changes, request the page content.
    watch (requestPage, (newValue, _) => {
      // When page change, don't not trigger paginator initialization.
      initPage.value = false
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
      initPage,
      events,
      initPagination,
      searchContent,
      requestSearch,
      dataRequest,
      toggleShowFilter,
      requestFilter,
      updateRequestPage
    }
  }
}
</script>

<style>

</style>