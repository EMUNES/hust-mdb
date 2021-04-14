<template>
  <common-layout>
    <template #content>
      <div>
        <transition appear=""
        enter-active-class="transition delay-200 duration-1000 ease-out"
        enter-from-class="opacity-0 scale-90"
        enter-to-class="opacity-100 scale-100">
          <div class="content-head mt-10">
            <p class="my-2 home-intro text-5xl font-semibold">
              欢迎！
            </p>
            <p class="my-5">
              这里是
              <span class="font-bold text-2xl">
                华中科技大学 . 材料科学与工程学院 . 热塑性材料数据云平台
              </span>
            </p>
          </div>
        </transition>

        <transition appear
        enter-active-class="transition delay-1500 duration-2000 ease-out"
        enter-from-class="opacity-0 scale-90 transform traslate-x-24"
        enter-class="opacity-100 scale-100">
          <div class="content-body mt-10">
            <div class="flex flex-col flex-wrap items-center justify-around text-center mx-10 px-10 xl:flex-row">
              <p class="home-display my-10 xl:mx-20 2xl:mx-40">
                <svg t="1617699380656" class="inline w-64 h-64" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="1124" width="200" height="200"><path d="M782.37 216.15v596.6H244.45v-596.6h537.92m22.25-88.56H222.2c-36.53 0-66.31 27.9-66.31 61.88v650c0.11 34.1 30 61.88 66.42 61.88h582.31c36.53 0 66.31-27.9 66.31-61.88v-650c0-34.21-29.67-61.88-66.31-61.88z" fill="#4D4D4D" p-id="1125"></path><path d="M706.54 706.58H418.7a33.31 33.31 0 0 1-33.21-33.21 33.31 33.31 0 0 1 33.21-33.21h287.84a33.31 33.31 0 0 1 33.21 33.21 33.31 33.31 0 0 1-33.21 33.21zM320.4 640.16a33.21 33.21 0 1 1-33.21 33.21 33.17 33.17 0 0 1 33.21-33.21z m386.14-92.55H418.7a33.31 33.31 0 0 1-33.21-33.21 33.31 33.31 0 0 1 33.21-33.21h287.84a33.31 33.31 0 0 1 33.21 33.21 33.31 33.31 0 0 1-33.21 33.21zM320.4 481.18a33.21 33.21 0 1 1-33.21 33.21 33.17 33.17 0 0 1 33.21-33.21z m386.14-92.44H418.7a33.31 33.31 0 0 1-33.21-33.21 33.31 33.31 0 0 1 33.21-33.21h287.84a33.31 33.31 0 0 1 33.21 33.21 33.31 33.31 0 0 1-33.21 33.21zM320.4 322.32a33.21 33.21 0 1 1-33.21 33.21 33.17 33.17 0 0 1 33.21-33.21z" fill="#5E9EFC" p-id="1126"></path></svg>
                <span class="block text-xl font-semibold">
                  大容量
                  <p class="text-gray-500 text-base">
                    当前材料数据实例总量: {{count}}
                  </p>
                </span>
              </p>
              <p class="home-display my-10 xl:mx-20 2xl:mx-40">
                <svg t="1617700017344" class="inline w-64 h-64" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="1259" width="200" height="200"><path d="M400 884.26H239.12a98.43 98.43 0 0 1-98.32-98.32V625.05a98.43 98.43 0 0 1 98.32-98.32H400a98.43 98.43 0 0 1 98.32 98.32v160.89A98.43 98.43 0 0 1 400 884.26zM239.12 616.11a9 9 0 0 0-8.94 8.94v160.89a9 9 0 0 0 8.94 8.94H400a9 9 0 0 0 8.94-8.94V625.05a9 9 0 0 0-8.94-8.94zM400 455.23H239.12a98.43 98.43 0 0 1-98.32-98.32V196a98.43 98.43 0 0 1 98.32-98.3H400a98.43 98.43 0 0 1 98.33 98.3v160.91A98.43 98.43 0 0 1 400 455.23zM239.12 187.08a9 9 0 0 0-8.94 8.94v160.89a9 9 0 0 0 8.94 8.94H400a9 9 0 0 0 8.94-8.94V196a9 9 0 0 0-8.94-8.94zM829 884.26H668.15a98.43 98.43 0 0 1-98.32-98.32V625.05a98.43 98.43 0 0 1 98.32-98.32H829a98.43 98.43 0 0 1 98.32 98.32v160.89A98.43 98.43 0 0 1 829 884.26zM668.15 616.11a9 9 0 0 0-8.94 8.94v160.89a9 9 0 0 0 8.94 8.94H829a9 9 0 0 0 8.94-8.94V625.05a9 9 0 0 0-8.94-8.94z" fill="#4D4D4D" p-id="1260"></path><path d="M748.6 455.23c-98.6 0-178.77-80.23-178.77-178.77S650 97.7 748.6 97.7s178.76 80.19 178.76 178.76-80.19 178.77-178.76 178.77z m0-286a107.26 107.26 0 1 0 107.25 107.23A107.38 107.38 0 0 0 748.6 169.21z" fill="#5E9EFC" p-id="1261"></path></svg>
                <span class="block text-xl font-semibold">
                  多参数
                  <p class="text-gray-500 text-base">
                    构成数据实例总维度: {{dataDim-1}}
                  </p>
                </span>
              </p>
              <p class="home-display my-10 xl:mx-20 2xl:mx-40">
                <svg t="1617700218346" class="inline w-64 h-64" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="1392" width="200" height="200"><path d="M860.26 139.33H181a98.43 98.43 0 0 0-98.32 98.32v429A98.43 98.43 0 0 0 181 765h679.3a98.43 98.43 0 0 0 98.32-98.32v-429a98.43 98.43 0 0 0-98.36-98.35z m8.94 527.35a9 9 0 0 1-8.94 8.94H181a9 9 0 0 1-8.94-8.94v-429a9 9 0 0 1 8.94-8.94h679.3a9 9 0 0 1 8.94 8.94zM770.87 818.63H252.46a44.69 44.69 0 0 0 0 89.38h518.41a44.69 44.69 0 0 0 0-89.38z" fill="#4D4D4D" p-id="1393"></path><path d="M450.9 558.52a35.75 35.75 0 0 1-25.28-61l101.12-101.15a35.75 35.75 0 1 1 50.56 50.56L476.18 548.05a35.64 35.64 0 0 1-25.28 10.47zM539.38 647a35.75 35.75 0 0 1-25.28-61l265.45-265.48a35.75 35.75 0 0 1 50.56 50.56L564.66 636.53A35.65 35.65 0 0 1 539.38 647z" fill="#5E9EFC" p-id="1394"></path></svg>
                <span class="block text-xl font-semibold">
                  易兼容
                  <p class="text-gray-500 text-base">
                    大屏小屏皆可使用
                    <span class="block text-sm">
                    （目前尚未兼容手机）
                    </span>
                  </p>
                </span>
              </p>
              <p class="home-display my-10 xl:mx-20 2xl:mx-40">
                <svg t="1617700357503" class="inline w-64 h-64" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="1527" width="200" height="200"><path d="M364.72 558a44.69 44.69 0 0 1-32.06-75.82l130.12-134.05a44.69 44.69 0 1 1 64.14 62.25L396.79 544.45A44.56 44.56 0 0 1 364.72 558z" fill="#4D4D4D" p-id="1528"></path><path d="M593.17 459.7c98.57 0 178.76-80.19 178.76-178.76s-80.19-178.77-178.76-178.77-178.76 80.19-178.76 178.76S494.6 459.7 593.17 459.7z m0-268.14a89.38 89.38 0 1 1-89.38 89.38 89.48 89.48 0 0 1 89.38-89.39zM789.81 549.08c-75.38 0-140 46.9-166.25 113l-213.78-66.3a44.69 44.69 0 0 0-26.49 85.37l229.45 71.21c12 87 86.82 154.25 177.07 154.25 98.57 0 178.76-80.19 178.76-178.76s-80.19-178.77-178.76-178.77z m0 268.14a89.38 89.38 0 1 1 89.38-89.38 89.48 89.48 0 0 1-89.38 89.38z" fill="#4D4D4D" p-id="1529"></path><path d="M253.52 790.41c-93.64 0-169.82-76.18-169.82-169.82s76.18-169.83 169.82-169.83 169.82 76.18 169.82 169.83-76.18 169.82-169.82 169.82z m0-268.14a98.32 98.32 0 1 0 98.32 98.32 98.43 98.43 0 0 0-98.32-98.33z" fill="#5E9EFC" p-id="1530"></path></svg>
                <span class="block text-xl font-semibold">
                  分离开发
                  <p class="text-gray-500 text-base">
                    完全基于REST的安全开发，
                    <span class="block text-gray-700">
                      基于 vue3 + Djano
                    </span>
                  </p>
                </span>
              </p>
            </div>
          </div>
        </transition>
      </div>
    </template>
  </common-layout>
</template>

<script>
import { onBeforeMount, ref } from 'vue';
import CommonLayout from '../layout/CommonLayout.vue'; 
import axios from '../request/axios.js';
import { useStore } from 'vuex';

export default {
  name: 'Home',
  components: {
    CommonLayout
  },
  setup() {
    const store = useStore()
    const count = ref(0)
    const dataDim = ref(0)

    onBeforeMount(() => {
      axios.get(store.state.backendAPIs.coreAPI)
        .then(res => {
          count.value = res.data.count
          dataDim.value = Object.keys(res.data.results[0]).length
        })
          .catch(err => {
            window.alert("很遗憾，无法加载首页信息")
            console.log(err)
          })
    })

    return {
      count,
      dataDim
    }
  }
}
</script>

<style scoped>
</style>