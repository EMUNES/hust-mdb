<template>
  <form @submit.prevent="submitLogin"
  class="bg-blue-50 px-5 py-3 w-2/3 rounded-xl">
    <div class="login-form-field">
      <svg t="1617366349414" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="6273" width="200" height="200"
      class="login-form-input-icon">
      <path d="M512 74.666667C270.933333 74.666667 74.666667 270.933333 74.666667 512S270.933333 949.333333 512 949.333333 949.333333 753.066667 949.333333 512 753.066667 74.666667 512 74.666667zM288 810.666667c0-123.733333 100.266667-224 224-224S736 686.933333 736 810.666667c-61.866667 46.933333-140.8 74.666667-224 74.666666s-162.133333-27.733333-224-74.666666z m128-384c0-53.333333 42.666667-96 96-96s96 42.666667 96 96-42.666667 96-96 96-96-42.666667-96-96z m377.6 328.533333c-19.2-96-85.333333-174.933333-174.933333-211.2 32-29.866667 51.2-70.4 51.2-117.333333 0-87.466667-72.533333-160-160-160s-160 72.533333-160 160c0 46.933333 19.2 87.466667 51.2 117.333333-89.6 36.266667-155.733333 115.2-174.933334 211.2-55.466667-66.133333-91.733333-149.333333-91.733333-243.2 0-204.8 168.533333-373.333333 373.333333-373.333333S885.333333 307.2 885.333333 512c0 93.866667-34.133333 177.066667-91.733333 243.2z" p-id="6274"></path>
      </svg>
      <label for="username"></label>
      <input type="text" v-model="username" placeholder="用户名" class="login-form-input">
    </div>
    <div class="login-form-field">
      <svg t="1617366171395" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="6116" width="200" height="200"
      class="login-form-input-icon">
      <path d="M785.066667 416h-61.866667v-121.6c0-108.8-91.733333-198.4-202.666667-198.4s-202.666667 89.6-202.666666 198.4v121.6h-78.933334c-55.466667 0-100.266667 44.8-100.266666 100.266667v311.466666c0 55.466667 44.8 100.266667 100.266666 100.266667h546.133334c55.466667 0 100.266667-44.8 100.266666-100.266667V516.266667c0-55.466667-44.8-100.266667-100.266666-100.266667z m-403.2-121.6c0-74.666667 61.866667-134.4 138.666666-134.4s138.666667 59.733333 138.666667 134.4v121.6h-277.333333v-121.6z m439.466666 533.333333c0 19.2-17.066667 36.266667-36.266666 36.266667H238.933333c-19.2 0-36.266667-17.066667-36.266666-36.266667V516.266667c0-19.2 17.066667-36.266667 36.266666-36.266667h546.133334c19.2 0 36.266667 17.066667 36.266666 36.266667v311.466666z" p-id="6117"></path><path d="M512 544c-17.066667 0-32 14.933333-32 32v106.666667c0 17.066667 14.933333 32 32 32s32-14.933333 32-32v-106.666667c0-17.066667-14.933333-32-32-32z" p-id="6118"></path>
      </svg>
      <label for="password"></label>
      <input type="text" v-model="password" placeholder="密码" class="login-form-input">
    </div>

    <div class="flex justify-around flex-wrap mt-10 mb-3">
      <button type="submit"
      class="bg-blue-400 text-white px-5 py-1">
        登录
      </button>

      <button @click="cancelLogin"
      class="bg-blue-200 px-5 py-1">
        取消
      </button>
    </div>
  </form>
</template>

<script>
import { ref } from 'vue'

export default {
  name: 'LoginForm',
  setup(_, context) {
    const username = ref('')
    const password = ref('')

    const submitLogin = () => {
      context.emit('loginSubmit', {
        username: username.value,
        password: password.value
      })
    }

    const cancelLogin = () => {
      username.value = ''
      password.value = ''
    }

    return {
      username,
      password,
      submitLogin,
      cancelLogin,
    }
  }
}
</script>

<style>
.login-form-field {
  @apply flex justify-start my-3 bg-white rounded md:w-auto;
}

.login-form-input {
  @apply text-sm outline-none;
}

.login-form-input-icon {
  @apply inline h-4 w-4 mx-3 my-2;
}
</style>