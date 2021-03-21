<template>
  <div class="list bg-blue-100 m-auto max-w-3xl rounded-xl">
    <div class="text-xl pt-5">
      热塑性材料信息表
    </div>
    <div v-for="eventInfo in events" :key="eventInfo">
      <material-detail :eventDetail="eventInfo" :detailId="detailId">
        <div class="flex justify-between items-center text p-3 border-2 border-blue-400 bg-blue-200 rounded-xl my-5 mx-12">
          <div class="id xl w-10">
            <span>{{ eventInfo.id }}</span>
          </div>
          <div class="info inline-grid grid-cols-2 flex-auto justify-center">
            <div class="info-field">
              <span class="field-name">系列</span>
              {{ eventInfo.series }}
            </div>
            <div class="info-field">
              <span class="block">牌号</span>
              {{ eventInfo.mark }}
            </div>
            <span class="info-field">材料缩写名称：{{ eventInfo.acronym }}</span>
            <span class="info-field">材料类型：{{ eventInfo.material_type }}</span>
          </div>
          <button class="m-5" @click="toggleDetail">
            <i class="fas fa-arrow-down"></i>
          </button>
        </div>
      </material-detail>
    </div>
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
  setup() {
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
      toggleDetail
    }
  }
}
</script>

<style>
.field-name {
  @apply block mx-4;
}

.info-field {
  @apply bg-blue-50 m-2 rounded flex justify-between ;
}
</style>