<template>
  <form @submit.prevent="submitLogin">
    <label for="username">用户名</label>
    <input type="text" v-model="username">

    <label for="username">密码</label>
    <input type="text" v-model="password">

    <div class="flex justify-around flex-wrap ">
      <button type="submit">
        提交
      </button>

      <button @click="cancelLogin">
        取消
      </button>
    </div>
  </form>
</template>

<script>
import { ref } from 'vue'

export default {
  name: 'LoginForm',
  setup(props, context) {
    const username = ref('')
    const password = ref('')
    const error = ref(false)

    const submitLogin = () => {
      context.emit('loginSubmit', {
        username: username.value,
        password: password.value
      })
    }

    return {
      username,
      password,
      error,
      submitLogin
    }
  }
}
</script>

<style>

</style>