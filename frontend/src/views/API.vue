<template>
  <common-layout>
    <template #content>
      <transition appear
      enter-active-class="transition duration-500 ease-out"
      enter-from-class="opacity-10"
      enter-to-class="opacity-100">
        <div class="flex flex-col text-left mt-10 ml-10 lg:ml-20">
          <h1 class="flex flex-col text-2xl pb-5">
            后端API接口详情
            <small class="text-sm text-gray-400">
              请注意：后端API仅供网站维护和功能调试使用，请勿直接在后端进行数据修改
            </small>
          </h1>
          <span class="api-field">
            后端根接口:
            <a :href="$store.state.backendAPIs.rootAPI">
              {{$store.state.backendAPIs.rootAPI}}
            </a>
          </span>
          <span class="api-field">
            材料数据接口:
            <a :href="$store.state.backendAPIs.coreAPI">
              {{$store.state.backendAPIs.coreAPI}}
            </a>
          </span>
          <span class="api-field">
            用户信息接口:
            <a :href="$store.state.backendAPIs.userAPI">
              {{$store.state.backendAPIs.userAPI}}
            </a>
          </span>
          <span class="api-field">
            后端登陆接口:
            <a :href="$store.state.backendAPIs.loginAPI">
              {{$store.state.backendAPIs.loginAPI}}
            </a>
          </span>
          <span class="api-field">
            用户token生成接口:
            <a :href="$store.state.backendAPIs.tokenAPI">
              {{$store.state.backendAPIs.tokenAPI}}
            </a>
          </span>
        </div>
      </transition>
    </template>
  </common-layout>
</template>

<script>
import CommonLayout from '../layout/CommonLayout.vue';

export default {
  name: "API",
  components: {
    CommonLayout
  },
}
</script>

<style>
.api-field {
  @apply py-3;
}

.api-field a {
  @apply text-blue-600 border-b-2 border-blue-700
}
</style>