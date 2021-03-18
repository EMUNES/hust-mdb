<template>
  <nav class="flex flex-auto justify-between items-center border-2">
    <ul class="rounded p-1 m-1">
      <button>
        <i class="fas fa-bars"></i>
      </button>

      <router-link to="/">
        首页
      </router-link> | 


      <router-link to="/materials">
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

</style>