<template>
  <common-layout>
    <template #content>
      <div class="flex flex-col items-center justify-around w-4/5 m-auto my-10 ml-20 border-2">
        <div class="conf">
          <form>
            参数设置
            <div class="my-2 px-2 rounded-lg">
              <label for="compoents" class="text-left text-sm">降维参数纬度: </label>
              <input type="text" v-model="components" :placeholder="components"
              class="w-10 outline-none border-2 rounded-lg px-1">
            </div>
            <div class="my-2px-2 rounded-lg">
              <label for="resultsNum" class="text-left text-sm">输出结果数量: </label>
              <input type="text" v-model="resultsNum" :placeholder="resultsNum"
              class="outline-none w-10 border-2 rounded-lg px-1">
            </div>
          </form>
        </div>

        <div class="user-input mt-5 mb-3 flex flex-col items-center justify-center">
          <label for="material_pk" class="block mx-2 text-center">输入材料数据编号</label>
          <input type="text" v-model="materialPk" placeholder=""
          class="px-2 block border-2 outline-none w-20 rounded-xl">
        </div>

        <button @click="getSimAnalysis"
        class="bg">
          <svg t="1618970198743" class="h-8 w-8 opacity-50" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="2944" width="200" height="200"><path d="M512 74.666667C270.933333 74.666667 74.666667 270.933333 74.666667 512S270.933333 949.333333 512 949.333333 949.333333 753.066667 949.333333 512 753.066667 74.666667 512 74.666667z m238.933333 349.866666l-2.133333 2.133334-277.333333 277.333333c-10.666667 10.666667-29.866667 12.8-42.666667 2.133333L426.666667 704l-149.333334-149.333333c-12.8-12.8-12.8-32 0-44.8 10.666667-10.666667 29.866667-12.8 42.666667-2.133334l2.133333 2.133334 125.866667 125.866666 253.866667-253.866666c10.666667-10.666667 29.866667-12.8 42.666666-2.133334l2.133334 2.133334c12.8 12.8 12.8 32 4.266666 42.666666z" p-id="2945"></path></svg>
        </button>
      </div>

      <div class="results w-2/3 lg:w-3/5 m-auto">
        <div v-for="result in results" :key="result"
        class="results flex flex-row items-center justify-around my-2">
          <div class="score">
            相似度(欧式距离):
            <p>{{ result.score }}</p>
          </div>
          <div class="material">
            <material-detail :eventDetail="result.data">
              <!-- Brief introduction for materials shown in the list. -->
              <div class="flex justify-between items-center border-2 border-gray-400 rounded-lg my-3 mx-12">
                <div class="flex flex-wrap justify-center items-center">
                  <div class="info-field">
                    <span class="field-name">材料ID:</span>
                    <p>{{ result.data.material_id }}</p>
                  </div>
                  <div class="info-field">
                    <span class="field-name">材料缩写名称：</span>
                    <p>{{ result.data.acronym }}</p>
                  </div>
                  <div class="info-field">
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
      </div>
    </template>
  </common-layout>
</template>

<script>
import { onBeforeMount, ref } from 'vue';
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
    const results = ref([])

    // Get similarity analysis result from backend.
    const getSimAnalysis = () => {
      results.value = []
      axios_no_token.get(store.state.backendAPIs.simAnalysisAPI + materialPk.value)
        .then(res => {
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
            axios.get(store.state.backendAPIs.coreAPI + mat_pk)
              .then(res => {
                mat_result.data = res.data
              })
                .catch(err => console.log(err))
            // Add to final results.
             results.value.push(mat_result)
          }
          console.log(results.value)
        })
    }

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
    }
  }
}
</script>

<style>

</style>