<template>
  <div class="list bg-gray-50 m-auto max-w-3xl rounded-xl">
    <div class="text-xl py-5">
      热塑性材料信息表
    </div>
    <div v-for="eventInfo in events" :key="eventInfo">
      <material-detail :eventDetail="eventInfo" :detailId="detailId">
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
  @apply mx-2;
}

.info-field {
  @apply m-2 flex
}
</style>