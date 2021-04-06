<template>
  <div class="flex fixed items-center"> 
    <span v-if="$store.getters.isAuthenticated"
    class="mt-3 mx-3">
      已登录
    </span>
    <button v-if="!$store.getters.isAuthenticated"
    class="mt-3 mx-1 px-1 border-2 border-blue-200 rounded">
      登陆
    </button>
    <button @click="logout"
    class="mt-3 mx-1 px-1 border-2 border-blue-200 rounded">
      登出
    </button>
  </div>
  <header class="bg-gradient-to-t from-blue-100 via-blue-200 to-blue-100 pt-14 pb-10">
    <h2 class="text text-3xl mb-5">
      华中科技大学
    </h2>

    <h2 class="text text-2xl mb-3">
      材料学院
    </h2>

    <h2 class="text text-2xl">
      热塑性材料数据库
    </h2>
  </header>

</template>

<script>
import { useStore } from 'vuex'
import { useRouter} from 'vue-router'

export default {
  name: "GeneralHeader",
  setup() {
    const store = useStore()
    const router = useRouter()

    const logout = () => {
      localStorage.removeItem(store.state.localTokenName)
      router.push('/login')
    }

    return {
      logout
    }
  }
}
</script>

<style>

</style>