<template>
  <div class="bg-white px-4 py-3 flex justify-center items-center border-t border-gray-200 sm:px-6">
    <nav class="relative z-0 inline-flex rounded-md shadow-sm -space-x-px" aria-label="Pagination">
      <a href="javascript: void(0)" @click="toFirstPage" v-if="pageCurrent > 1"
      class="relative inline-flex items-center px-2 py-2 border border-gray-300 bg-white text-sm font-medium text-gray-500 hover:bg-gray-50">
        <span class="sr-only">Last</span>
       <svg class="h-4 w-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
        <path fill-rule="evenodd" d="M15.707 15.707a1 1 0 01-1.414 0l-5-5a1 1 0 010-1.414l5-5a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 010 1.414zm-6 0a1 1 0 01-1.414 0l-5-5a1 1 0 010-1.414l5-5a1 1 0 011.414 1.414L5.414 10l4.293 4.293a1 1 0 010 1.414z" clip-rule="evenodd" />
      </svg>
      </a>
      <a href="javascript: void(0)" @click="pageDown" v-if="pageCurrent > 1"
      class="relative inline-flex items-center px-2 py-2 border border-gray-300 bg-white text-sm font-medium text-gray-500 hover:bg-gray-50">
        <span class="sr-only">Previous</span>
        <svg class="h-5 w-5" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
          <path fill-rule="evenodd" d="M12.707 5.293a1 1 0 010 1.414L9.414 10l3.293 3.293a1 1 0 01-1.414 1.414l-4-4a1 1 0 010-1.414l4-4a1 1 0 011.414 0z" clip-rule="evenodd" />
        </svg>
      </a>
      <a href="javascript: void(0)" v-if="pageCurrent == pageLast"
      class="relative inline-flex items-center px-2 py-2 border border-gray-300 bg-white text-sm font-medium text-gray-500 hover:bg-gray-50">
        <span class="sr-only">More</span>
        <svg class="h-5" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
          <path d="M6 10a2 2 0 11-4 0 2 2 0 014 0zM12 10a2 2 0 11-4 0 2 2 0 014 0zM16 12a2 2 0 100-4 2 2 0 000 4z" />
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
      <a href="javascript: void(0)" v-if="pageCurrent < pageLast" @click="openJump"
      class="relative inline-flex items-center px-2 py-2 border border-gray-300 bg-white text-sm font-medium text-gray-500 hover:bg-gray-50">
        <div v-show="!jump">
          <span class="sr-only">More</span>
          <svg class="h-5" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
            <path d="M6 10a2 2 0 11-4 0 2 2 0 014 0zM12 10a2 2 0 11-4 0 2 2 0 014 0zM16 12a2 2 0 100-4 2 2 0 000 4z" />
          </svg>
        </div> 
        <input type="text" v-show="jump" v-model="destPage" @keypress.enter="finishJump(destPage)"
        class="h-5 w-8">
      </a>
      <a href="javascript: void(0)" v-if="pageLast1" @click="pageTo(pageLast1)"
      class="relative inline-flex items-center px-4 py-2 border border-gray-300 bg-white text-sm font-medium text-gray-700 hover:bg-gray-50">
        {{pageLast1}}
      </a>
      <a href="javascript: void(0)" v-if="showLast" @click="pageTo(pageLast)"
      class="relative inline-flex items-center px-4 py-2 border border-gray-300 bg-white text-sm font-medium text-gray-700 hover:bg-gray-50">
        {{pageLast}}
      </a>
      <a href="javascript: void(0)" @click="pageUp" v-if="pageCurrent < pageLast"
      class="relative inline-flex items-center px-2 py-2 border border-gray-300 bg-white text-sm font-medium text-gray-500 hover:bg-gray-50">
        <span class="sr-only">Next</span>
        <svg class="h-5 w-5" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
          <path fill-rule="evenodd" d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z" clip-rule="evenodd" />
        </svg>
      </a>
      <a href="javascript: void(0)" @click="toLastPage" v-if="pageCurrent < pageLast"
      class="relative inline-flex items-center px-2 py-2 border border-gray-300 bg-white text-sm font-medium text-gray-500 hover:bg-gray-50">
        <span class="sr-only">Last</span>
        <svg class="h-4 w-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
          <path fillRule="evenodd" d="M10.293 15.707a1 1 0 010-1.414L14.586 10l-4.293-4.293a1 1 0 111.414-1.414l5 5a1 1 0 010 1.414l-5 5a1 1 0 01-1.414 0z" clipRule="evenodd" />
          <path fillRule="evenodd" d="M4.293 15.707a1 1 0 010-1.414L8.586 10 4.293 5.707a1 1 0 011.414-1.414l5 5a1 1 0 010 1.414l-5 5a1 1 0 01-1.414 0z" clipRule="evenodd" />
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
    const jump = ref(false)
    const destPage = ref(null)

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

    const toFirstPage = () => {
      pageCurrent.value = 1
      updatePages()
    }

    const toLastPage = () => {
      pageCurrent.value = pageLast.value
      updatePages()
    }

    const openJump = () => {
      jump.value = true
    }

    const finishJump = (dest) => {
      if (dest >=1 & dest <= pageLast.value) {
        pageCurrent.value = Number(dest)
        updatePages()
      }
      else {
        console.log("Page number out of index!!!")
      }
      jump.value = false
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
      jump,
      destPage,
      updatePages,
      pageDown,
      pageUp,
      pageTo,
      toFirstPage,
      toLastPage,
      openJump,
      finishJump
    }
  },
}
</script>

<style>

</style>