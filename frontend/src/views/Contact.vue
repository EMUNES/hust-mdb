<template>
  <common-layout>
    <template #content>
      <div class="flex flex-col text-center">
        <transition appear
        enter-active-class="transition duration-3000 ease-in"
        enter-from-class="opacity-0"
        enter-to-class="opacity-100">
          <img class=" w-48 md:w-80 m-auto mt-20" src="../assets/doggy.jpeg" alt="孤独的犬">
        </transition>
          <div>
            <transition appear
            enter-active-class="transition duration-1000 ease-out"
            enter-from-class="opacity-0 scale-75 transform translate-y-10"
            enter-to-class="opacity-100">
              <p class="text-xl my-3">
                华中科技大学
              </p>
            </transition>

            <transition appear
            enter-active-class="transition delay-1000 duration-1000 ease-out"
            enter-from-class="opacity-0 scale-75 transform translate-y-16"
            enter-to-class="opacity-100">
              <p class="text my-2">
                某位同学
              </p>
            </transition>
            <transition appear
            enter-active-class="transition delay-2000  duration-1000 ease-out"
            enter-from-class="opacity-0 scale-75 transform translate-y-24"
            enter-to-class="opacity-100">
              <p class="text-sm">
                2021.3 - 2021.5
              </p>
            </transition>
          </div>

        <div class="mt-10 text-blue-700">
          <p>
            管理员: 
            <span class="text-gray-400">
              {{ admin }}
            </span>
          </p>

          <p>
            负责人:
            <span class="text-gray-400">
              {{ responser }}
            </span>
          </p>
        </div>
      </div>
    </template>
  </common-layout>
</template>

<script>
import { onBeforeMount, ref } from 'vue';
import { useStore } from 'vuex';
import CommonLayout from '../layout/CommonLayout.vue';

export default {
  name: "Contact",
  components: {
    CommonLayout
  },
  setup() {
    const store = useStore()
    const admin = ref(store.state.admin)
    const responser = ref(store.state.responser)

    onBeforeMount(() => {
      if (!admin.value) {
        admin.value = "未知，为什么没人管呢"
      }
      if (!responser.value) {
        responser.value = "未知，为什么没人负责任呢"
      }
    })

    return {
      admin,
      responser
    }
  }
}
</script>

<style>

</style>