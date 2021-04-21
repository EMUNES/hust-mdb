<template>
  <div class="md:flex flex-col min-h-screen w-48 lg:w-64 border-r-2">
    <div class="my-3 py-2">
      <h1 class="font-bold text-xl">
        导航
      </h1>
    </div>
    <div class="flex flex-col w-full text-gray-700 bg-white dark-mode:text-gray-200 dark-mode:bg-gray-800 flex-shrink-0">
      <nav class="flex-grow md:block px-4 pb-4 md:pb-0 md:overflow-y-auto">
        <router-link class="block px-4 py-3 text-sm font-semibold text-gray-900 bg-transparent rounded dark-mode:bg-gray-700 dark-mode:hover:bg-gray-600 dark-mode:focus:bg-gray-600 dark-mode:focus:text-white dark-mode:hover:text-white dark-mode:text-gray-200 hover:text-gray-900 focus:text-gray-900 hover:bg-gray-200 focus:bg-gray-200 focus:outline-none focus:shadow-outline border-t-2" to="/">首页</router-link>
        <router-link class="block px-4 py-3 text-sm font-semibold text-gray-900 bg-transparent rounded dark-mode:bg-transparent dark-mode:hover:bg-gray-600 dark-mode:focus:bg-gray-600 dark-mode:focus:text-white dark-mode:hover:text-white dark-mode:text-gray-200 hover:text-gray-900 focus:text-gray-900 hover:bg-gray-200 focus:bg-gray-200 focus:outline-none focus:shadow-outline border-t-2" to="/materials">资源信息表单</router-link>
        <router-link class="block px-4 py-3 text-sm font-semibold text-gray-900 bg-transparent rounded dark-mode:bg-transparent dark-mode:hover:bg-gray-600 dark-mode:focus:bg-gray-600 dark-mode:focus:text-white dark-mode:hover:text-white dark-mode:text-gray-200 hover:text-gray-900 focus:text-gray-900 hover:bg-gray-200 focus:bg-gray-200 focus:outline-none focus:shadow-outline border-t-2" to="/checkAPI">API资源接口</router-link>
        <router-link class="block px-4 py-3 text-sm font-semibold text-gray-900 bg-transparent rounded dark-mode:bg-transparent dark-mode:hover:bg-gray-600 dark-mode:focus:bg-gray-600 dark-mode:focus:text-white dark-mode:hover:text-white dark-mode:text-gray-200 hover:text-gray-900 focus:text-gray-900 hover:bg-gray-200 focus:bg-gray-200 focus:outline-none focus:shadow-outline border-t-2" to="/contact">联系与反馈</router-link>
        <button @click="open = !open" class="flex flex-row items-center w-full text-center py-2 font-semibold bg-transparent rounded-lg dark-mode:bg-transparent dark-mode:focus:text-white dark-mode:hover:text-white dark-mode:focus:bg-gray-600 dark-mode:hover:bg-gray-600 md:block hover:text-gray-900 focus:text-gray-900 hover:bg-gray-200 focus:bg-gray-200 focus:outline-none focus:shadow-outline border-t-2">
          <span>高级功能</span>
        </button>
        <div v-show="open">
          <div class="px-2 py-2 bg-white rounded-xl shadow dark-mode:bg-gray-800">
            <router-link class="block px-4 py-2 mt-2 text-sm font-semibold bg-transparent rounded-lg dark-mode:bg-transparent dark-mode:hover:bg-gray-600 dark-mode:focus:bg-gray-600 dark-mode:focus:text-white dark-mode:hover:text-white dark-mode:text-gray-200 md:mt-0 hover:text-gray-900 focus:text-gray-900 hover:bg-gray-200 focus:bg-gray-200 focus:outline-none focus:shadow-outline" to="/sim-analysis">数据匹配</router-link>
            <a class="block px-4 py-2 mt-2 text-sm font-semibold bg-transparent rounded-lg dark-mode:bg-transparent dark-mode:hover:bg-gray-600 dark-mode:focus:bg-gray-600 dark-mode:focus:text-white dark-mode:hover:text-white dark-mode:text-gray-200 md:mt-0 hover:text-gray-900 focus:text-gray-900 hover:bg-gray-200 focus:bg-gray-200 focus:outline-none focus:shadow-outline text-gray-400" href="#">期待更多~</a>
            <a class="block px-4 py-2 mt-2 text-sm font-semibold bg-transparent rounded-lg dark-mode:bg-transparent dark-mode:hover:bg-gray-600 dark-mode:focus:bg-gray-600 dark-mode:focus:text-white dark-mode:hover:text-white dark-mode:text-gray-200 md:mt-0 hover:text-gray-900 focus:text-gray-900 hover:bg-gray-200 focus:bg-gray-200 focus:outline-none focus:shadow-outline text-gray-400" href="#">期待更多~</a>
          </div>
        </div>
      </nav>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue'
export default {
  name: 'SideBar',
  setup() {
    const open = ref(false)

    return {
      open
    }
  }
}
</script>

<style>

</style>