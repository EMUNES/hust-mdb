<template>
  <slot>

  </slot>
  <div v-if="showDetail">
    This is the detail.
  </div>
</template>

<script>
import { ref, toRef, watch } from 'vue'

export default {
  name: "MaterialDetail",
  props: {
    eventDetail: {
      required: true
    },
    detailId: {
      required: false
    }
  },
  setup(props, context) {
    const eventDetail = toRef(props, "eventDetail")
    const detailId = toRef(props, "detailId")
    const showDetail = ref(false)

    watch(detailId, (newValue, _) => {
      if (eventDetail.value.id == detailId.value) {
        showDetail.value = true
      }
      else {
        showDetail.value = false
      } 
    })

    return {
      eventDetail,
      showDetail
    }
  }

}
</script>

<style>

</style>