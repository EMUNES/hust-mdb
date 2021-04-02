import { createStore } from 'vuex'

export default createStore({
  state: {
    msg: "Vuex is working!",
    backendAPIs: {
      // API for backend root.
      rootAPI: 'http://127.0.0.1:8000/',
      // API for materials.
      coreAPI: 'http://127.0.0.1:8000/core/',
      // API for users.
      userAPI: 'http://127.0.0.1:8000/auth/users/',
      // API FOR searching.
      searchAPI: 'http://127.0.0.1:8000/core/?search=',
      // API for filtering.
      filterBaseAPI: 'http://127.0.0.1:8000/core/?',
      filterAPI: 'http://127.0.0.1:8000/core/?',
      filter: {
        series: '',
        mark: '' ,
        manufacturer: '',
        acronym: '',
        material_type: '',
        data_source: '',
        material_id: '',
        level_code: '',
        vendor_code: '',
        fibre_or_infill: ''
      },
      // API for login.
      loginAPI: 'http://127.0.0.1:8000/auth/login/',
      // API for token.
      tokenAPI: 'http://127.0.0.1:8000/api-token-auth/',
    }, 
    localTokenName: 'hust-mdbsys-token'
  },

  getters: {
    isAuthenticated: state => {
      return true ? localStorage.getItem(state.localTokenName) : false
    }
  },
  
  // sync, mutate state.
  mutations: {
    getFilter(state, payload) {
      // Init our request API.
      state.backendAPIs.filterAPI = state.backendAPIs.filterBaseAPI
      // Access all filter fields and add them into request url.
      for (let [key, value] of Object.entries(state.backendAPIs.filter)) {
        value = payload[key]
        let filterField = `${key}__icontains=${value}&`
        state.backendAPIs.filterAPI = state.backendAPIs.filterAPI + filterField
      }
      
      //Trim the filter request url.
      state.backendAPIs.filterAPI = state.backendAPIs.filterAPI.slice(0, -1).trim()
    }
  }, 

  // async, commit mutations.
  actions: {

  },
  modules: {

  }
})
