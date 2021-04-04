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
    localTokenName: 'hust-mdbsys-token',
    // Template for material instance.
    materialModelInstance: {
      series: '#',
      mark: '#',
      manufacturer: '#',
      link: '#',
      acronym: '#',
      material_type: '#',
      data_source: '#',
      last_modified_date: '#',
      test_date: '#',
      data_status: '#',
      material_id: '#',
      level_code: '#',
      vendor_code: '#',
      fibre_or_infill: '#',
      model_surface_temperature: 0.0,
      melt_temperature: 0.0,
      mold_temperature_range_min: 0.0,
      mold_temperature_range_max: 0.0,
      melt_temperature_range_min: 0.0,
      melt_temperature_range_max: 0.0,
      absolute_maximum_melt_temperature: 0.0,
      ejection_temperature: 0.0,
      maximum_shear_stress: 0.0,
      maximum_shear_rate: 0.0,
      melt_density: 0.0,
      solid_density: 0.0,
      pvt_b5: 0.0,
      pvt_b6: 0.0,
      pvt_b1m: 0.0,
      pvt_b2m: 0.0,
      pvt_b3m: 0.0,
      pvt_b4m: 0.0,
      pvt_b1s: 0.0,
      pvt_b2s: 0.0,
      pvt_b3s: 0.0,
      pvt_b4s: 0.0,
      pvt_b7: 0.0,
      pvt_b8: 0.0,
      pvt_b9: 0.0,
      elastic_modulus_e1: 0.0,
      elastic_modulus_e2: 0.0,
      poisson_ratio_v12: 0.0,
      poisson_ratio_v23: 0.0,
      shear_modulus_g12: 0.0,
      thermal_expansion_data_transverse_isotropic_coefficient_alpha1: 0.0,
      thermal_expansion_data_transverse_isotropic_coefficient_alpha2: 0.0,
      seven_params_n: 0.0,
      seven_params_Tau: 0.0,
      seven_params_D1: 0.0,
      seven_params_D2: 0.0,
      seven_params_D3: 0.0,
      seven_params_A1: 0.0,
      seven_params_A2: 0.0,
      c1: 0.0,
      c2: 0.0,
      conversion_temperature: 0.0,
      MFR_temperature: 0.0,
      MFR_loading: 0.0,
      measured_MFR: 0.0
    }
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
