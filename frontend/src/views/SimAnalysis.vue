<template>
  <common-layout>
    <template #content>
      <transition appear
      enter-active-class="transition duration-300 ease-out"
      enter-from-class="opacity-0 scale-75"
      enter-to-class="opacity-100 scale-100">
        <div class="flex flex-col items-center justify-around w-4/5 m-auto my-10 ml-20 border-2 border-blue-400">
          <div class="conf">
            <form class="mt-5">
              <h1 class="font-semibold">
                当前参数设置
              </h1>
              <div class="my-2 px-2 rounded-lg">
                <label for="compoents" class="text-left font-thin">降维参数纬度: </label>
                <input type="text" v-model="components" :placeholder="components"
                class="w-10 outline-none rounded-lg px-1">
              </div>
              <div class="my-2px-2 rounded-lg">
                <label for="resultsNum" class="text-left font-light">输出结果数量: </label>
                <input type="text" v-model="resultsNum" :placeholder="resultsNum"
                class="outline-none w-10 rounded-lg px-1">
              </div>
            </form>
          </div>

          <div class="user-input mt-5 mb-3 flex flex-col items-center justify-center border-t-2 pt-3 border-blue-400">
            <label for="material_pk" class="block mx-2 text-center font-bold font-mono">输入材料数据编号</label>
            <input type="text" v-model="materialPk" placeholder=""
            class="px-2 block border-2 outline-none w-20 rounded-xl border-blue-300 hover:border-blue-500">
          </div>

          <div class="flex justify-around w-24 items-center pb-3">
            <button @click="getSimAnalysis"
            class="bg">
              <svg t="1618989204412" class="h-6 w-6 opacity-70" v-if="resultsDone"
              viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="35681" width="200" height="200"><path d="M1011.84448 243.2c-16-16-41.6-16-57.6 0L384.64448 809.6 67.84448 544c-16-16-44.8-12.8-57.6 6.4-16 16-12.8 44.8 6.4 57.6l345.6 288c6.4 6.4 16 9.6 25.6 9.6h3.2c9.6 0 22.4-3.2 28.8-12.8L1011.84448 300.8c16-16 16-41.6 0-57.6z" p-id="35682"></path></svg>
              <svg t="1618986615738" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="30180" width="200" height="200"
              class="h-8 w-8 opacity-70 animate-spin" v-if="!resultsDone"><path d="M843.307 742.24c0 3.217 2.607 5.824 5.824 5.824s5.824-2.607 5.824-5.824a5.823 5.823 0 0 0-5.824-5.824 5.823 5.823 0 0 0-5.824 5.824zM714.731 874.912c0 6.398 5.186 11.584 11.584 11.584s11.584-5.186 11.584-11.584-5.186-11.584-11.584-11.584-11.584 5.186-11.584 11.584zM541.419 943.2c0 9.614 7.794 17.408 17.408 17.408s17.408-7.794 17.408-17.408-7.794-17.408-17.408-17.408-17.408 7.794-17.408 17.408z m-186.56-9.152c0 12.795 10.373 23.168 23.168 23.168s23.168-10.373 23.168-23.168-10.373-23.168-23.168-23.168-23.168 10.373-23.168 23.168zM189.355 849.12c0 16.012 12.98 28.992 28.992 28.992s28.992-12.98 28.992-28.992-12.98-28.992-28.992-28.992-28.992 12.98-28.992 28.992zM74.731 704.736c0 19.228 15.588 34.816 34.816 34.816s34.816-15.588 34.816-34.816-15.588-34.816-34.816-34.816-34.816 15.588-34.816 34.816z m-43.008-177.28c0 22.41 18.166 40.576 40.576 40.576s40.576-18.166 40.576-40.576-18.166-40.576-40.576-40.576-40.576 18.166-40.576 40.576z m35.392-176.128c0 25.626 20.774 46.4 46.4 46.4s46.4-20.774 46.4-46.4c0-25.626-20.774-46.4-46.4-46.4-25.626 0-46.4 20.774-46.4 46.4z m106.176-142.016c0 28.843 23.381 52.224 52.224 52.224s52.224-23.381 52.224-52.224c0-28.843-23.381-52.224-52.224-52.224-28.843 0-52.224 23.381-52.224 52.224z m155.904-81.344c0 32.024 25.96 57.984 57.984 57.984s57.984-25.96 57.984-57.984-25.96-57.984-57.984-57.984-57.984 25.96-57.984 57.984z m175.104-5.056c0 35.24 28.568 63.808 63.808 63.808s63.808-28.568 63.808-63.808c0-35.24-28.568-63.808-63.808-63.808-35.24 0-63.808 28.568-63.808 63.808z m160.32 72.128c0 38.421 31.147 69.568 69.568 69.568s69.568-31.147 69.568-69.568-31.147-69.568-69.568-69.568-69.568 31.147-69.568 69.568z m113.92 135.488c0 41.638 33.754 75.392 75.392 75.392s75.392-33.754 75.392-75.392-33.754-75.392-75.392-75.392-75.392 33.754-75.392 75.392z m45.312 175.488c0 44.854 36.362 81.216 81.216 81.216s81.216-36.362 81.216-81.216c0-44.854-36.362-81.216-81.216-81.216-44.854 0-81.216 36.362-81.216 81.216z" fill="" p-id="30181"></path></svg>
            </button>

            <button @click="clear">
              <svg t="1618988781896" class="h-6 w-6 opacity-70" v-if="!resultsDone"
              viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="34081" width="200" height="200"><path d="M224.9728 297.3696a358.4 358.4 0 0 0 501.7088 501.7088l-501.76-501.76z m72.3968-72.3968l501.6576 501.6576a358.4 358.4 0 0 0-501.7088-501.7088zM512 972.8a460.8 460.8 0 1 1 0-921.6 460.8 460.8 0 0 1 0 921.6z" p-id="34082"></path></svg>
              <svg t="1618988867674" class="h-7 w-7" v-if="resultsDone"
              viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="34822" width="200" height="200"><path d="M647.168 715.776c-49.664 34.816-108.032 52.224-166.912 51.712-7.68 0-15.872-0.512-23.552-1.536l-9.216-1.536c-6.144-1.024-12.288-1.536-17.92-2.56-3.584-0.512-7.168-1.536-10.752-2.56-5.632-1.536-11.776-2.56-17.408-4.096-2.56-1.024-5.12-2.048-8.192-3.072-6.656-2.048-13.312-4.096-19.456-7.168-1.536-0.512-3.072-1.024-4.096-1.536-7.168-3.584-14.848-6.656-22.016-10.752 0 0-0.512-0.512-1.024-0.512-24.064-13.312-45.568-29.184-65.024-48.64l-1.024-1.024c-6.144-6.144-11.776-12.288-16.896-18.944-1.024-1.536-2.048-2.56-3.072-4.096-38.912-48.64-62.464-110.592-62.464-177.664h75.264L153.088 302.08 33.28 481.792h74.752c0 78.848 24.576 152.064 66.56 212.48 0.512 1.024 1.024 2.048 1.536 2.56 4.096 6.144 9.216 11.776 13.824 17.92 2.048 2.048 3.072 4.096 5.12 6.656 6.656 8.192 14.336 15.872 21.504 23.552l2.048 2.048c25.088 25.088 53.76 46.08 84.48 63.488 1.024 0.512 1.536 1.024 2.56 1.536 8.704 4.608 17.92 9.216 27.136 13.312 2.56 1.024 4.608 2.048 6.656 3.072 8.192 3.584 15.872 6.144 24.576 9.216 4.096 1.536 7.68 2.56 11.776 4.096 7.168 2.048 14.336 4.096 22.016 5.632 5.12 1.024 9.728 2.56 14.848 3.584l6.144 1.536c7.168 1.536 13.824 2.048 20.992 2.56 2.56 0.512 5.12 1.024 7.68 1.024 12.8 1.024 25.088 2.048 37.376 2.048 76.288 0 150.528-23.04 214.528-68.096 20.48-14.336 25.6-42.496 11.264-62.464-15.36-21.504-43.008-26.112-63.488-11.776m211.456-233.984c0-78.848-24.576-152.064-66.048-211.968l-1.536-3.072c-5.12-7.168-10.752-14.336-16.384-21.504-0.512-1.024-1.536-1.536-2.048-2.56-38.4-46.08-86.016-81.92-140.288-105.472-1.536-0.512-3.072-1.536-4.608-2.048-8.704-3.584-17.408-6.656-26.624-9.728-3.072-1.024-6.144-2.048-9.728-3.072-7.68-2.56-15.36-4.096-23.552-6.144-4.608-1.024-8.704-2.048-13.312-3.072-2.048-0.512-4.096-1.024-6.656-1.536-6.144-1.024-11.776-1.536-17.92-2.048l-12.288-1.536c-9.728-1.024-19.968-1.536-29.696-1.536-2.048 0-3.584-0.512-5.632-0.512H481.28c-76.288 0-150.528 23.04-214.016 67.584-20.48 14.336-25.6 42.496-11.264 62.976s42.496 25.088 62.976 10.752c49.152-34.304 106.496-51.712 165.888-51.2 8.192 0 16.896 0.512 25.088 1.536 2.56 0 5.12 0.512 7.68 1.024 6.656 1.024 13.312 1.536 19.968 3.072 3.072 0.512 5.632 1.536 8.704 2.048 6.656 1.536 12.8 3.072 19.456 5.12 2.048 0.512 4.096 1.536 6.144 2.048l21.504 7.68c0.512 0 1.536 0.512 2.048 1.024 41.984 17.92 78.848 45.568 107.52 80.896 0 0 0 0.512 0.512 0.512 40.448 49.152 65.024 112.128 65.024 180.736h-75.264l120.32 180.224 119.808-180.224h-74.752z" fill="#5D5D5D" p-id="34823"></path></svg>
            </button>
          </div>
        </div>
      </transition>


      <div class="results w-2/3 lg:w-3/5 m-auto">
        <transition appear
          enter-active-class="transition delay-300 duration-300 ease-out"
          enter-from-class="opacity-0 scale-75"
          enter-to-class="opacity-100 scale-100">
          <h2 class="text-xl font-sans font-semibold mb-3 pb-3 border-b-2 border-blue-400">
            数据匹配结果
          </h2>
          </transition>

        <transition appear
        enter-active-class="transition delay-300 duration-300 ease-out"
        enter-from-class="opacity-0 scale-75"
        enter-to-class="opacity-100 scale-100">
          <div v-show="!results">
            <p>
              请输入材料数据编号（主键）以获取数据匹配结果
              <small class="block text-gray-500">
                如：输入0代表id为0（非材料ID）的材料数据对象
              </small>
              <small class="block text-gray-500">
                你可以在<span class="font-semibold">资源信息表单</span>页面查询你所需要的材料id
              </small>
            </p>
          </div>
        </transition>

        <transition-group appear
        enter-active-class="transition duration-300 ease-out"
        enter-from-class="opacity-0 scale-75"
        enter-to-class="opacity-100 scale-100"
        leave-active-class="transition duration-200 ease-in"
        leave-from-class="opacity-100 scale-100"
        leave-to-class="opacity-0, scale-60">
          <div v-for="result in results" :key="result"
          class="results flex flex-row items-center justify-between my-2">
            <div class="score text-left font-sans">
              离散度(欧式距离):
              <p class="font-semibold text-blue-600">{{ result.score }}</p>
            </div>

            <div class="materials">
              <material-detail :eventDetail="result.data">
                <!-- Brief introduction for materials shown in the list. -->
                <div class="flex justify-between items-center border-2 border-gray-400 rounded-lg my-3 mx-12">
                  <div class="flex flex-col justify-around items-start xl:flex-row xl:justify-center xl:items-center">
                    <div class="my-0 flex">
                      <span class="field-name">材料ID:</span>
                      <p>{{ result.data.material_id }}</p>
                    </div>

                    <div class="my-1 flex">
                      <span class="field-name">材料缩写名称：</span>
                      <p>{{ result.data.acronym }}</p>
                    </div>

                    <div class="my-0 flex">
                      <span class="field-name">材料类型：</span>
                      <p>{{ result.data.material_type }}</p>
                    </div>

                  </div>
                  <button @click="toggleDetail"
                  class="m-4 p-1 bg-gray-50 rounded border-gray-300 border-b-2 border-r-2" >
                    <span class="sr-only">Content</span>
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                      <path fill-rule="evenodd" d="M3 7a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 13a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1z" clip-rule="evenodd" />
                    </svg>
                  </button>
                </div>
              </material-detail>
            </div>
          </div>
        </transition-group>
      </div>
    </template>
  </common-layout>
</template>

<script>
import { onBeforeMount, onBeforeUpdate, ref } from 'vue';
import { useStore } from 'vuex';
import axios_no_token from '../request/axios_no_token';
import axios from '../request/axios';
import CommonLayout from '../layout/CommonLayout.vue';
import MaterialDetail from '../components/materials/MaterialDetail.vue';

export default {
  name: "SimAnalysis",
  components: {
    CommonLayout,
    MaterialDetail
  },
  setup() {
    const store = useStore()
    const components = ref(0)
    const resultsNum = ref(0)
    const materialPk = ref(null)
    const results = ref(null)
    const resultsDone = ref(true)

    // Get similarity analysis result from backend.
    const getSimAnalysis = async () => {
      results.value = []
      resultsDone.value = false
      await axios_no_token.get(store.state.backendAPIs.simAnalysisAPI + materialPk.value)
        .then(async res => {
          // All needed data.
          for (let result of res.data.data_results) {
            const mat_pk = result[0]
            const mat_score = result[1]
            const mat_result = {
              data: {},
              score: 0.0
            }
            // Get material similarity score.
            mat_result.score = mat_score
            // Get material corresponding data.
            // Use await here to avoid asynchronization so data will be required.
            await axios.get(store.state.backendAPIs.coreAPI + mat_pk)
              .then(res => {
                mat_result.data = res.data
              })
                .catch(err => console.log(err))
            // Add to final results.
             results.value.push(mat_result)
          }
        })
      resultsDone.value = true
    }

    const clear = () => {
      results.value = null
      resultsDone.value = true
      materialPk.value = null
    }

    onBeforeUpdate(() => {
      results.value = null
    })

    // Initiate local params setting with backend params.
    onBeforeMount(() => {
      axios_no_token.get(store.state.backendAPIs.mlAPI)
        .then(res => {
          components.value = res.data.components
          resultsNum.value = res.data.results_num
        })
    })

    return {
      components,
      resultsNum,
      materialPk,
      getSimAnalysis,
      results,
      resultsDone,
      clear
    }
  }
}
</script>

<style>

</style>