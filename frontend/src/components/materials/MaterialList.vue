<template>
  <div class="list m-auto max-w-4xl rounded-xl">
    <div class="text-xl py-5">
      热塑性材料信息表
    </div>
    
    <!-- Material list with list transition -->
    <transition-group 
    enter-active-class="transition duration-500 ease-out"
    enter-from-class="opacity-0 scale-90"
    enter-to-class="opacity-100 scale-100"
    move-class="transition duration-500 ease-linear">
      <div v-for="eventInfo in events" :key="eventInfo">
        <material-detail :eventDetail="eventInfo" :detailId="detailId" v-bind="$attrs">
          <!-- Brief introduction for materials shown in the list. -->
          <div class="flex justify-between items-center border-2 border-gray-400 rounded-lg my-3 mx-12">
            <div class="id xl w-10">
              <span>{{ eventInfo.id }}</span>
            </div>
            <div class="flex flex-wrap justify-center items-center">
              <div class="info-field">
                <span class="field-name">材料ID:</span>
                <p>{{ eventInfo.material_id }}</p>
              </div>
              <div class="info-field">
                <span class="field-name">材料缩写名称：</span>
                <p>{{ eventInfo.acronym }}</p>
              </div>
              <div class="info-field">
                <span class="field-name">材料类型：</span>
                <p>{{ eventInfo.material_type }}</p>
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
    </transition-group>
  </div>
</template>

<script>
import MaterialDetail from "./MaterialDetail.vue"
import { ref } from 'vue'

export default {
  name: "MaterialList",
  props: {
    events: {
      type: Array,
      requeired: true
    }
  },
  components: {
    MaterialDetail,
  },
  setup(_, context) {
    const detailId = ref(-1)

    const toggleDetail = (e) => {
      if (detailId.value == -1) {
        detailId.value = e.path[2].children[0].innerText
      }
      else {
        detailId.value = -1
      }
    }

    return {
      detailId,
      toggleDetail,
    }
  }
}
</script>

<style>
.field-name {
  @apply mx-2;
}

.info-field {
  @apply m-2 flex
}
</style>