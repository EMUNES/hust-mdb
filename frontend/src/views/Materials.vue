<template>
  <general-header></general-header>
  <navigation>
    <li class="inline-block rounded-full mx-2">
      <button @click="initPagination"
      class="outline-none">
        <i class="fas fa-redo-alt"></i>
      </button>
    </li>
    <li class="inline-block rounded-full mx-2">
      <button @click="toggleShowFilter"
      class="outline-none">
        <i class="fas fa-filter"></i>
      </button>
    </li>
    <li class="search inline-block mx-2 my-1 border-2 border-gray-500 rounded bg-white">
      <input type="text" placeholder="Search..." v-model="searchContent" @keydown.enter="requestSearch"
      class="w-25 outline-none px-1 py-1">
      <i @click="requestSearch"
      class="fas fa-search mx-2"></i>
    </li>
  </navigation>
  <Filter :showing="showFilter" @close-filter="toggleShowFilter" @add-filter="requestFilter"/>
  <material-list :events="events"></material-list>
  <Paginator :initPage="initPage" :totalPages="totalPages" @page-updated="updateRequestPage" />
</template>

<script>
import axios from '../request/axios.js';
import MaterialList from '../components/materials/MaterialList.vue'
import Paginator from '../components/Paginator.vue'
import Filter from '../components/Filter.vue'
import Navigation from '../components/Navigation.vue';
import { onBeforeMount, ref, watch } from 'vue';
import { useStore } from 'vuex';
import GeneralHeader from '../components/GeneralHeader.vue';

export default {
  name: 'Materials',

  components: {
    MaterialList,
    Paginator,
    Filter,
    Navigation,
    GeneralHeader
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