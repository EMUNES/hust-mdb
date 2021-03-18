<template>
  <nav class="flex flex-auto justify-between items-center border-2">
    <ul class="flex rounded p-1 m-1">
      <button class="ml-3 mr-4">
        <i class="fas fa-bars"></i>
      </button>

      <router-link to="/" class="global-link">
        首页
      </router-link>
      <router-link to="/materials" class="global-link">
        热塑性材料信息
      </router-link>
    </ul>
    <ul class="function">
      <slot>
        
      </slot>
    </ul>
  </nav>
</template>

<script>
export default {

}
</script>

<style>
.global-link {
  @apply border-2 border-gray-400 py-1 px-2 mx-1 rounded-lg;
}
</style>