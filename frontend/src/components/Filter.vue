<template>
  <div v-if="showing" @click.self="closeThis"
  class="fixed z-40 inset-0 overflow-x-hidden overflow-y-auto opacity-25 bg-black">
  </div>
  
  <transition
  enter-active-class="transition duration-300 ease-in"
  enter-from-class="opacity-0 scale-75"
  enter-to-class="opcaity-100 scale-100"
  leave-active-class="transistion duration-300 ease-out"
  leave-from-class="opacity-90 scale-100"
  leave-to-class="opacity-0 scale-60">
    <div  v-if="showing"
    class="fixed text-left w-1/3 right-1/3 top-20 max-w-2xl z-50 bg-white text-black rounded-lg">
      <form class="text-black m-3">
        <div class="text-black text-3xl m-2 p-2 border-b">
            筛选
          <button @click.prevent="closeThis"
          class="absolute right-3 w-5 h-5 align-top">
            <span class="sr-only">Close</span>
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
              <path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd" />
            </svg>
          </button>
        </div>
        <div class="m-2">
          <label for="系列">系列: </label>
          <input type="text" v-model="series" @keydown.enter="submitThis"
          class="filter-input">
        </div>
        <div class="m-2">
          <label for="牌号">牌号: </label>
          <input type="text" v-model="mark" @keydown.enter="submitThis"
          class="filter-input">
        </div>
        <div class="m-2">
          <label for="制造商">制造商: </label>
          <input type="text" v-model="manufacturer" @keydown.enter="submitThis"
          class="filter-input">
        </div>
        <div class="m-2">
          <label for="材料名称缩写">材料名称缩写: </label>
          <input type="text" v-model="acronym" @keydown.enter="submitThis"
          class="filter-input">
        </div>
        <div class="m-2">
          <label for="材料类型">材料类型: </label>
          <input type="text" v-model="material_type" @keydown.enter="submitThis"
          class="filter-input">
        </div>
        <div class="m-2">
          <label for="数据来源">数据来源: </label>
          <input type="text" v-model="data_source" @keydown.enter="submitThis"
          class="filter-input">
        </div>
        <div class="m-2">
          <label for="材料ID">材料ID: </label>
          <input type="text" v-model="material_id" @keydown.enter="submitThis"
          class="filter-input">
        </div>
        <div class="m-2">
          <label for="等级代码">等级代码: </label>
          <input type="text" v-model="level_code" @keydown.enter="submitThis"
          class="filter-input">
        </div>
        <div class="m-2">
          <label for="供应商代码">供应商代码: </label>
          <input type="text" v-model="vendor_code" @keydown.enter="submitThis"
          class="filter-input">
        </div>
        <div class="m-2">
          <label for="纤维/填充物">纤维/填充物: </label>
          <input type="text" v-model="fibre_or_infill" @keydown.enter="submitThis"
          class="filter-input">
        </div>
      </form>
      <div class="text-center">
        <button @click.prevent="submitThis" aria-label="submit"
        class="mr-10 border-2 py-1 px-2 border-blue-200 my-2 rounded-xl">
          确定
        </button>
        <button @click.prevent="closeThis" aria-label="close"
        class="ml-10 border-2 py-1 px-2 border-red-200 my-2 rounded-xl">
          取消
        </button>
      </div>
    </div>
  </transition>
</template>

<script>
import { ref } from 'vue'
import { useStore } from 'vuex';

export default {
  name: "Filter",
  props: {
    showing: {
      type: Boolean,
      required: true
    }
  },
  emits:['closeFilter', 'addFilter'],
  setup(props, context) {
    const store = useStore()
    const series = ref('')
    const mark = ref('')
    const manufacturer = ref('')
    const acronym = ref('')
    const material_type = ref('')
    const data_source = ref('')
    const material_id = ref('')
    const level_code = ref('')
    const vendor_code = ref('')
    const fibre_or_infill = ref('')

    const closeThis = () => {
      context.emit('closeFilter')
    }   

    const submitThis = () => {
      store.commit('getFilter', {
        series: series.value,
        mark: mark.value,
        manufacturer: manufacturer.value,
        acronym: acronym.value,
        material_type: material_type.value,
        data_source: data_source.value,
        material_id: material_id.value,
        level_code: level_code.value,
        vendor_code: vendor_code.value,
        fibre_or_infill: fibre_or_infill.value
      })
      context.emit('addFilter')
    }

    return {
      series,
      mark,
      manufacturer,
      acronym,
      material_type,
      data_source,
      material_id,
      level_code,
      vendor_code,
      fibre_or_infill,
      closeThis,
      submitThis
    }
  }
}
</script>

<style>
.filter-input {
  @apply block w-full border-b-2 outline-none border-gray-800;
}
</style>