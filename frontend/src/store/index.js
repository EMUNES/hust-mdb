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
    },
  },
  
  // sync, mutate state.
  mutations: {

  }, 

  // async, commit mutations.
  actions: {

  },
  modules: {
  }
})
