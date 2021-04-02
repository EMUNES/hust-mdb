<template>
  <header class="fixed my-10 mx-10 text-3xl">
    华中科技大学
  </header>

  <div class="flex flex-col items-center justify-center h-screen">
    <login-form @login-submit="login">

    </login-form>
  </div>
</template>

<script>
import LoginForm from '../components/auth/LoginForm.vue';
import RegisterForm from '../components/auth/RegisterForm.vue';
import Logout from '../components/auth/Logout.vue';
import axios from '../request/axios.js';
import { useStore } from 'vuex';
import { ref } from 'vue'

export default {
  name: "Login",
  components: {
    LoginForm,
    RegisterForm,
    Logout
  },
  setup() {
    const currentLogin = ref(true)
    const currentRegister = ref(false)
    const store = useStore()

    const login = (paylood) => {
      console.log(paylood.username)
      axios.post(store.state.backendAPIs.loginAPI, {
        username: paylood.username,
        password: paylood.password
      })
        .then(res => console.log(res.data.token))
          .catch(err => console.log(err))
    }

    return {
      currentLogin,
      currentRegister,
      login
    }
  }
}
</script>

<style>

</style>