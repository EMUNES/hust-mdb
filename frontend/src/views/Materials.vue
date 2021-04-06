<template>
  <general-header></general-header>
  <head-bar>
    <li class="inline-block rounded-full mx-2">
      <button @click="initPagination"
      class="outline-none">
        <svg class="inline h-5 w-5" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
          <path fill-rule="evenodd" d="M4 2a1 1 0 011 1v2.101a7.002 7.002 0 0111.601 2.566 1 1 0 11-1.885.666A5.002 5.002 0 005.999 7H9a1 1 0 010 2H4a1 1 0 01-1-1V3a1 1 0 011-1zm.008 9.057a1 1 0 011.276.61A5.002 5.002 0 0014.001 13H11a1 1 0 110-2h5a1 1 0 011 1v5a1 1 0 11-2 0v-2.101a7.002 7.002 0 01-11.601-2.566 1 1 0 01.61-1.276z" clip-rule="evenodd" />
        </svg>
      </button>
    </li>
    <li class="inline-block rounded-full mx-2">
      <button @click="toggleShowFilter"
      class="outline-none h-5 w-5">
        <span class="sr-only">Filter</span>
        <svg class="inline" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
          <path fill-rule="evenodd" d="M3 3a1 1 0 011-1h12a1 1 0 011 1v3a1 1 0 01-.293.707L12 11.414V15a1 1 0 01-.293.707l-2 2A1 1 0 018 17v-5.586L3.293 6.707A1 1 0 013 6V3z" clip-rule="evenodd" />
        </svg>
      </button>
    </li>
    <li class="inline-block rounded-full mx-2">
      <button @click="openDetailForm">
        <span class="sr-only">Delete</span>
        <svg t="1617534954422" class="inline h-5 w-5" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="2957" width="200" height="200"><path d="M874.666667 469.333333H554.666667V149.333333c0-23.466667-19.2-42.666667-42.666667-42.666666s-42.666667 19.2-42.666667 42.666666v320H149.333333c-23.466667 0-42.666667 19.2-42.666666 42.666667s19.2 42.666667 42.666666 42.666667h320v320c0 23.466667 19.2 42.666667 42.666667 42.666666s42.666667-19.2 42.666667-42.666666V554.666667h320c23.466667 0 42.666667-19.2 42.666666-42.666667s-19.2-42.666667-42.666666-42.666667z" p-id="2958"></path></svg>      </button>
    </li>
    <li class="search inline-block mx-2 my-1 border-2 border-gray-500 rounded bg-white">
      <input type="text" placeholder="Search..." v-model="searchContent" @keydown.enter="requestSearch"
      class="w-25 outline-none px-1 py-1">
      <button @click="requestSearch" class="px-1 border-l-2">
        <svg class="inline w-5 h-5" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
          <path fill-rule="evenodd" d="M8 4a4 4 0 100 8 4 4 0 000-8zM2 8a6 6 0 1110.89 3.476l4.817 4.817a1 1 0 01-1.414 1.414l-4.816-4.816A6 6 0 012 8z" clip-rule="evenodd" />
        </svg>
      </button>
    </li>
  </head-bar>
  <Filter :showing="showFilter" @close-filter="toggleShowFilter" @add-filter="requestFilter"/>
  <material-list :events="events" @modal-form-submit="makeUpdate" @delete-material="makeDelete"></material-list>
  <Paginator :initPage="initPage" :totalPages="totalPages" @page-updated="updateRequestPage" />
  <material-modal :showModal="showDetailModal" :eventDetail="$store.state.materialModelInstance" @close="showDetailModal=false" @modal-form-submit="makeNew"></material-modal>
</template>

<script>
import axios from '../request/axios.js';
import MaterialList from '../components/materials/MaterialList.vue'
import Paginator from '../components/Paginator.vue'
import Filter from '../components/Filter.vue'
import HeadBar from '../components/bars/HeadBar.vue';
import { onBeforeMount, ref, watch } from 'vue';
import { useStore } from 'vuex';
import GeneralHeader from '../components/GeneralHeader.vue';
import MaterialModal from '../components/materials/MaterialModal.vue';

export default {
  name: 'Materials',

  components: {
    MaterialList,
    Paginator,
    Filter,
    HeadBar,
    GeneralHeader,
    MaterialModal
  },

  setup(_, context) {
    const requestPage = ref(1)
    const totalPages = ref(0)
    const events = ref([])
    const store = useStore()
    const showFilter = ref(false)
    const showDetailModal = ref(false)
    const initPage = ref(false)
    const searchContent = ref('')
    const totalMaterials = ref(0)

    // A general request method to connect backend API.
    const dataRequest = (_, backendURL=store.state.backendAPIs.coreAPI) => {
      axios.get(backendURL, {
        headers: {}
      })
        .then(res => {
          events.value = res.data.results
          totalPages.value = res.data.total_pages
          totalMaterials.value = res.data.count
          store.commit('setCount', {
            count: totalMaterials.value
          })
        })
          .catch(err => {console.error(err)})
    }

    // Open/Close the filter form.
    const toggleShowFilter = () => {
      showFilter.value = !showFilter.value
    }

    // Open/Close the material detail form.
    const openDetailForm = () => {
      showDetailModal.value = true
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
    
    // Update material detail.
    const makeUpdate = (payload) => {
      axios.put(store.state.backendAPIs.coreAPI + payload.id + '/', payload.data)
        .then(res => window.alert('实例更新成功！'))
          .catch(err => {
            window.alert('实例无法实现更新 详情请见控制台')
            console.log(err)
          })
    }

    // Add new material instance.
    const makeNew = (payload) => {
      // Django won't handle the primary key for us.
      // We have to set the primary key id field by ourself.
      store.commit('addCount', _)
      axios.post(store.state.backendAPIs.coreAPI, payload.data)
        .then(_ => console.log('新的实例提交成功！'))
          .catch(err => {
            window.alert('添加实例失败 详情请见控制台')
            console.log(err)
          })
    }

    // Delete material instance.
    const makeDelete = (payload) => {
      const del = confirm("确定删除该项材料数据吗？\n\n您的操作讲不可挽回。")

      if (del) {
        axios.delete(store.state.backendAPIs.coreAPI + payload.targetID + '/')
          .then(_ => window.alert("删除成功！"))
            .catch(err => {
              window.alert('删除操作失败 详情请见控制台')
              console.log(err)
            })
      }
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
      updateRequestPage,
      showDetailModal,
      openDetailForm,
      makeNew,
      makeUpdate,
      makeDelete
    }
  }
}
</script>

<style>

</style>