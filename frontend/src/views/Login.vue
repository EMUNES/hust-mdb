<template>
  <div class="bg-hust-bg-full bg-cover">
    <header class="fixed my-10 mx-10 text-3xl">
      华中科技大学
    </header>

    <div class="flex flex-col items-center justify-center h-screen w-2/3 md:m-auto max-w-3xl">
      <div class="mb-10">
        <button class="text-blue-400 border-b-2 border-current px-5 text-xl mx-1">
          登录
        </button>
        
        <button class="hover:text-green-600 border-b-2 hover:border-current px-5 text-xl mx-1">
          注册
        </button>
      </div>
      <login-form @login-submit="login" class="opacity-90">

      </login-form>
    </div>
  </div>
</template>

<script>
import LoginForm from '../components/auth/LoginForm.vue';
import RegisterForm from '../components/auth/RegisterForm.vue';
import Logout from '../components/auth/Logout.vue';
import axios from '../request/axios.js';
import { useStore } from 'vuex';
import { useRouter } from 'vue-router'
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
    const store = useStore()
    const router = useRouter()

    const login = (paylood) => {
      // Try to require token.
      axios.post(store.state.backendAPIs.tokenAPI, {
        username: paylood.username,
        password: paylood.password
      })
        .then(res => {
          localStorage.setItem(store.state.localTokenName, res.data.token)
        })
          .catch(err => {
            console.log(err)
          })
      
      // If the token is required and athenticated, jump to the main page.
      if (store.getters.isAuthenticated) {
        router.push('/')
      }
    }

    return {
      currentLogin,
      login
    }
  }
}
</script>

<style>

</style>