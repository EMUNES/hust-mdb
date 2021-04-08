<template>
  <div class="list bg-gray-50 m-auto max-w-3xl rounded-xl">
    <div class="text-xl py-5">
      热塑性材料信息表
    </div>
    
    <!-- Material list with list transition -->
    <transition-group 
    enter-active-class="transition duration-1000 ease-out"
    enter-from-class="opacity-0 scale-90"
    enter-to-class="opacity-100 scale-100"
    move-class="transition duration-500 ease-linear">
      <div v-for="eventInfo in events" :key="eventInfo">
        <material-detail :eventDetail="eventInfo" :detailId="detailId" v-bind="$attrs">
          <!-- Brief introduction for materials shown in the list. -->
          <div class="flex justify-between items-center border-2 border-gray-300 rounded-xl my-3 mx-12">
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
            <button class="m-5" @click="toggleDetail">
              <span class="sr-only">More Content</span>
              <svg class="inline w-4 h-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
                <path fillRule="evenodd" d="M15.707 4.293a1 1 0 010 1.414l-5 5a1 1 0 01-1.414 0l-5-5a1 1 0 011.414-1.414L10 8.586l4.293-4.293a1 1 0 011.414 0zm0 6a1 1 0 010 1.414l-5 5a1 1 0 01-1.414 0l-5-5a1 1 0 111.414-1.414L10 14.586l4.293-4.293a1 1 0 011.414 0z" clipRule="evenodd" />
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