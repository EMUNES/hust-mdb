<template>
  <div class="bg-white px-4 py-3 flex justify-center items-center border-t border-gray-200 sm:px-6">
    <nav class="relative z-0 inline-flex rounded-md shadow-sm -space-x-px" aria-label="Pagination">
      <a href="javascript: void(0)" @click="pageDown" v-if="pageCurrent > 1"
      class="relative inline-flex items-center px-2 py-2 rounded-l-md border border-gray-300 bg-white text-sm font-medium text-gray-500 hover:bg-gray-50">
        <span class="sr-only">Previous</span>
        <svg class="h-5 w-5" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
          <path fill-rule="evenodd" d="M12.707 5.293a1 1 0 010 1.414L9.414 10l3.293 3.293a1 1 0 01-1.414 1.414l-4-4a1 1 0 010-1.414l4-4a1 1 0 011.414 0z" clip-rule="evenodd" />
        </svg>
      </a>
      <a href="javascript: void(0)" @click="pageTo(pageCurrent)"
      class="relative inline-flex items-center px-4 py-2 border border-gray-300 bg-white text-sm font-medium text-gray-700 hover:bg-gray-50">
        {{pageCurrent}}
      </a>
      <a href="javascript: void(0)" v-if="pageNext1" @click="pageTo(pageNext1)"
      class="relative inline-flex items-center px-4 py-2 border border-gray-300 bg-white text-sm font-medium text-gray-700 hover:bg-gray-50">
        {{pageNext1}}
      </a>
      <a href="javascript: void(0)" v-if="pageNext2" @click="pageTo(pageNext2)"
      class="hidden md:inline-flex relative items-center px-4 py-2 border border-gray-300 bg-white text-sm font-medium text-gray-700 hover:bg-gray-50">
        {{pageNext2}}
      </a>
      <span v-if="pageHasGap"
       class="relative inline-flex items-center px-4 py-2 border border-gray-300 bg-white text-sm font-medium text-gray-700">
        ...
      </span>
      <a href="javascript: void(0)" v-if="pageLast1" @click="pageTo(pageLast1)"
      class="relative inline-flex items-center px-4 py-2 border border-gray-300 bg-white text-sm font-medium text-gray-700 hover:bg-gray-50">
        {{pageLast1}}
      </a>
      <a href="javascript: void(0)" v-if="showLast" @click="pageTo(pageLast)"
      class="relative inline-flex items-center px-4 py-2 border border-gray-300 bg-white text-sm font-medium text-gray-700 hover:bg-gray-50">
        {{pageLast}}
      </a>
      <a href="javascript: void(0)" @click="pageUp"
      class="relative inline-flex items-center px-2 py-2 rounded-r-md border border-gray-300 bg-white text-sm font-medium text-gray-500 hover:bg-gray-50">
        <span class="sr-only">Next</span>
        <svg class="h-5 w-5" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
          <path fill-rule="evenodd" d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z" clip-rule="evenodd" />
        </svg>
      </a>
    </nav>
  </div>
</template>

<script>
import { ref, toRef, watch } from 'vue';

export default {
  name: "Paginator",
  props: {
    totalPages: {
      type: Number,
      required: false,
    }
  },
  emits: ['pageUpdated'],
  setup(props, context) {
    const pageCurrent = ref(1)
    const pageLast = toRef(props, 'totalPages')
    const pageNext1 = ref(0)
    const pageNext2 = ref(0)
    const pageLast1 = ref(0)
    const pageHasGap = ref(false)
    const showLast = ref(false)

    const updatePages = () => {
      // Enough pages for gap (at least 7 pages)?
      let pageGap = pageLast.value - pageCurrent.value
      if (pageGap >= 5) {
        pageHasGap.value = true
        pageNext1.value = pageCurrent.value + 1
        pageNext2.value = pageCurrent.value + 2
        pageLast1.value = pageLast.value - 1
        showLast.value = true
      }
      else if(pageGap >= 4) {
        pageHasGap.value = false
        pageNext1.value = pageCurrent.value + 1
        pageNext2.value = pageCurrent.value + 2
        pageLast1.value = pageLast.value - 1
        showLast.value = true
      }
      else if(pageGap >= 3) {
        pageHasGap.value = false
        pageNext1.value = pageCurrent.value + 1
        pageNext2.value = pageCurrent.value + 2
        pageLast1.value = 0
        showLast.value = true
      }
      else if(pageGap >= 2) {
        pageHasGap.value = false
        pageNext1.value = pageCurrent.value + 1
        pageNext2.value = 0
        pageLast1.value = 0
        showLast.value = true
      }
      else if(pageGap >=1) {
        pageHasGap.value = false
        pageNext1.value = 0
        pageNext2.value = 0
        pageLast1.value = 0
        showLast.value = true
      }
      else {  
        pageHasGap.value = false
        pageNext1.value = 0
        pageNext2.value = 0
        pageLast1.value = 0
        showLast.value = false
      }
    }

    const emitCurrentPage = () => {
      // Emit current page.
      context.emit('pageUpdated', {
        page: pageCurrent
      })
    }

    const pageDown = () => {
      if (pageCurrent.value > 1) {
        pageCurrent.value -= 1
      }
    }

    const pageTo = (pageNum) => {
        pageCurrent.value = pageNum
    }

    const pageUp = () => {
      if (pageCurrent.value < pageLast.value) {
        pageCurrent.value += 1
      }
    }

    watch(pageCurrent, () => {
      updatePages()
      emitCurrentPage()
    })

    return {
      pageCurrent,
      pageLast,
      pageNext1,
      pageNext2,
      pageLast1,
      pageHasGap,
      showLast,
      updatePages,
      pageDown,
      pageUp,
      pageTo
    }
  },
}
</script>

<style>

</style>