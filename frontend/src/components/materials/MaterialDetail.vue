<template>
  <slot>

  </slot>
  <!-- Detailed information for the drop page. -->
  <div v-if="showDetail"
  class="mx-10 bg-blue-50 rounded-lg">
    <h4 class="text-lg my-2 p-2">
      材料详细信息
    </h4>
    <div class="flex flex-wrap border-b-2 pb-1 border-gray-300">
      <div v-show="eventDetail.series" class="detail-info-field">
        系列： 
        <span class="text-info">
          {{eventDetail.series}}
        </span>
      </div>
      <div v-show="eventDetail.mark" class="detail-info-field">
        牌号: 
        <span class="text-info">
          {{eventDetail.mark}}
        </span>
      </div>
      <div v-show="eventDetail.manufacturer" class="detail-info-field">
        制造商： 
        <span class="text-info">
          {{eventDetail.manufacturer}}
        </span>
      </div>
      <div v-show="eventDetail.acronym" class="detail-info-field">
        缩写：
        <span class="text-info">
          {{eventDetail.acronym}}
        </span>
      </div>
      <div v-show="eventDetail.link" class="detail-info-field">
        链接：
        <span class="text-info">
          {{eventDetail.link}}
        </span>
      </div>
      <div v-show="eventDetail.material_type" class="detail-info-field">
        数据类型：
        <span class="text-info">
          {{eventDetail.material_type}}
        </span>
      </div>
      <div v-show="eventDetail.data_source" class="detail-info-field">
        数据来源：
        <span class="text-info">
          {{eventDetail.data_source}}
        </span>
      </div>
      <div v-show="eventDetail.material_id" class="detail-info-field">
        材料ID：
        <span class="text-info">
          {{eventDetail.material_id}}
        </span>
      </div>
      <div v-show="eventDetail.level_code" class="detail-info-field">
        等级代码：
        <span class="text-info">
          {{eventDetail.level_code}}
        </span>
      </div>
      <div v-show="eventDetail.vendor_code" class="detail-info-field">
        供应商代码：
        <span class="text-info">
          {{eventDetail.vendor_code}}
        </span>
      </div>
      <div v-show="eventDetail.fibre_or_infill" class="detail-info-field">
        纤维、填充物： 
        <span class="text-info">
          {{eventDetail.fibre_or_infill}}
        </span>
      </div>
    </div>
    <div class="grid grid-cols-2 items-start bg-gray-100">
      <button class="detail-param-info">
        <div class="head" @click="togglePhy">
          <span class="params-title">
            物理参数信息
          </span>
          <i v-if="showingPhy" class="fas fa-caret-down"></i>
          <i v-if="!showingPhy" class="fas fa-caret-left"></i>
        </div>
        <div v-show="showingPhy" class="params">
          <div class="param-field">
            <span class="param-name">最大剪切应力：</span>
            <p class="param-value">{{eventDetail.maximum_shear_stress}}</p>
          </div>
          <div class="param-field">
            <span class="param-name">最大剪切速率：</span>
            <p class="param-value">{{eventDetail.maximum_shear_rate}}</p>
          </div>
          <div class="param-field">
            <span class="param-name">熔体密度:</span>
            <p class="param-value">{{eventDetail.melt_density}}</p>
          </div>
          <div class="param-field">
            <span class="param-name">固体密度:</span>
            <p class="param-value">{{eventDetail.solid_density}}</p>
          </div>
          <div class="param-field">
            <span class="param-name">弹性模量E1:</span>
            <p class="param-value">{{eventDetail.elastic_modulus_e1}}</p>
          </div>
          <div class="param-field">
            <span class="param-name">弹性模量E2:</span>
            <p class="param-value">{{eventDetail.elastic_modulus_e2}}</p>
          </div>
          <div class="param-field">
            <span class="param-name">泊松比v12:</span>
            <p class="param-value">{{eventDetail.poisson_ratio_v12}}</p>
          </div>
          <div class="param-field">
            <span class="param-name">泊松比v23:</span>
            <p class="param-value">{{eventDetail.poisson_ratio_v23}}</p>
          </div>
          <div class="param-field">
            <span class="param-name">剪切模量G12:</span>
            <p class="param-value">{{eventDetail.shear_modulus_g12}}</p>
          </div>
          <div class="param-field">
            <span class="param-name">热膨胀数据横向各向同性系数alpha1:</span>
            <p class="param-value">{{eventDetail.thermal_expansion_data_transverse_isotropic_coefficient_alpha1}}</p>
          </div>
          <div class="param-field">
            <span class="param-name">热膨胀数据横向各向同性系数alpha2:</span>
            <p class="param-value">{{eventDetail.thermal_expansion_data_transverse_isotropic_coefficient_alpha2}}</p>
          </div>
        </div>
      </button>

      <button class="detail-param-info">
        <div class="head" @click="toggleTemp">
          <span class="params-title">
            温度参数信息
          </span>
          <i v-if="showingTemp" class="fas fa-caret-down"></i>
          <i v-if="!showingTemp" class="fas fa-caret-left"></i>
        </div>
        <div v-show="showingTemp" class="params">
          <div class="param-field">
            <span class="param-name">模具表面温度：</span>
            <p class="param-value">{{eventDetail.model_surface_temperature}}</p>
          </div>
          <div class="param-field">
            <span class="param-name">熔体温度：</span>
            <p class="param-value">{{eventDetail.melt_temperature}}</p>
          </div>
          <div class="param-field">
            <span class="param-name">模具温度范围（最小值）:</span>
            <p class="param-value">{{eventDetail.mold_temperature_range_min}}</p>
          </div>
          <div class="param-field">
            <span class="param-name">模具温度范围（最大值）:</span>
            <p class="param-value">{{eventDetail.mold_temperature_range_max}}</p>
          </div>
          <div class="param-field">
            <span class="param-name">熔体温度范围（最小值）:</span>
            <p class="param-value">{{eventDetail.melt_temperature_range_min}}</p>
          </div>
          <div class="param-field">
            <span class="param-name">熔体温度范围（最大值）:</span>
            <p class="param-value">{{eventDetail.melt_temperature_range_max}}</p>
          </div>
          <div class="param-field">
            <span class="param-name">绝对最大溶体温度:</span>
            <p class="param-value">{{eventDetail.absolute_maximum_melt_temperature}}</p>
          </div>
          <div class="param-field">
            <span class="param-name">顶出温度:</span>
            <p class="param-value">{{eventDetail.ejection_temperature}}</p>
          </div>
          <div class="param-field">
            <span class="param-name">转换温度:</span>
            <p class="param-value">{{eventDetail.conversion_temperature}}</p>
          </div>
        </div>
      </button>
      
      <button class="detail-param-info">
        <div class="head" @click="togglePVT">
          <span class="params-title">
            pvt参数信息
          </span>
          <i v-if="showingPVT" class="fas fa-caret-down"></i>
          <i v-if="!showingPVT" class="fas fa-caret-left"></i>
        </div>
        <div v-show="showingPVT" class="params">
          <div class="param-field">
            <span class="param-name">pvt_b5:</span>
            <p class="param-value">{{eventDetail.pvt_b5}}</p>
          </div>
          <div class="param-field">
            <span class="param-name">pvt_b6:</span>
            <p class="param-value">{{eventDetail.pvt_b6}}</p>
          </div>
          <div class="param-field">
            <span class="param-name">pvt_b1m:</span>
            <p class="param-value">{{eventDetail.pvt_b1m}}</p>
          </div>
          <div class="param-field">
            <span class="param-name">pvt_b2m:</span>
            <p class="param-value">{{eventDetail.pvt_b2m}}</p>
          </div>
          <div class="param-field">
            <span class="param-name">pvt_b3m:</span>
            <p class="param-value">{{eventDetail.pvt_b3m}}</p>
          </div>
          <div class="param-field">
            <span class="param-name">pvt_b4m:</span>
            <p class="param-value">{{eventDetail.pvt_b4m}}</p>
          </div>
          <div class="param-field">
            <span class="param-name">pvt_b1s:</span>
            <p class="param-value">{{eventDetail.pvt_b1s}}</p>
          </div>
          <div class="param-field">
            <span class="param-name">pvt_b2s:</span>
            <p class="param-value">{{eventDetail.pvt_b2s}}</p>
          </div>
          <div class="param-field">
            <span class="param-name">pvt_b3s:</span>
            <p class="param-value">{{eventDetail.pvt_b3s}}</p>
          </div>
          <div class="param-field">
            <span class="param-name">pvt_b4s:</span>
            <p class="param-value">{{eventDetail.pvt_b4s}}</p>
          </div>
          <div class="param-field">
            <span class="param-name">pvt_b7:</span>
            <p class="param-value">{{eventDetail.pvt_b7}}</p>
          </div>
          <div class="param-field">
            <span class="param-name">pvt_b8:</span>
            <p class="param-value">{{eventDetail.pvt_b8}}</p>
          </div>
          <div class="param-field">
            <span class="param-name">pvt_b9:</span>
            <p class="param-value">{{eventDetail.pvt_b9}}</p>
          </div>
        </div>
      </button>
      <button class="detail-param-info">
        <div class="head" @click="toggleP7">
          <span class="params-title">
            七参数信息
          </span>
          <i v-if="showingP7" class="fas fa-caret-down"></i>
          <i v-if="!showingP7" class="fas fa-caret-left"></i>
        </div>
        <div v-show="showingP7" class="params">
          <div class="param-field">
            <span class="param-name">七参数n:</span>
            <p class="param-value">{{eventDetail.seven_params_n}}</p>
          </div>
          <div class="param-field">
            <span class="param-name">七参数Tau*:</span>
            <p class="param-value">{{eventDetail.seven_params_Tau}}</p>
          </div>
          <div class="param-field">
            <span class="param-name">七参数D1:</span>
            <p class="param-value">{{eventDetail.seven_params_D1}}</p>
          </div>
          <div class="param-field">
            <span class="param-name">七参数D2:</span>
            <p class="param-value">{{eventDetail.seven_params_D2}}</p>
          </div>
          <div class="param-field">
            <span class="param-name">七参数D3:</span>
            <p class="param-value">{{eventDetail.seven_params_D3}}</p>
          </div>
          <div class="param-field">
            <span class="param-name">七参数A1:</span>
            <p class="param-value">{{eventDetail.seven_params_A1}}</p>
          </div>
          <div class="param-field">
            <span class="param-name">七参数A2:</span>
            <p class="param-value">{{eventDetail.seven_params_A2}}</p>
          </div>
        </div>
      </button>
      <button class="detail-param-info">
        <div class="head" @click="toggleOther">
          <span class="params-title">
          其它参数（MFR、c1、c2等）
          </span>
          <i v-if="showingOther" class="fas fa-caret-down"></i>
          <i v-if="!showingOther" class="fas fa-caret-left"></i>
        </div>
        <div v-show="showingOther" class="params">
          <div class="param-field">
            <span class="param-name">c1:</span>
            <p class="param-value">{{eventDetail.c1}}</p>
          </div>
          <div class="param-field">
            <span class="param-name">c2:</span>
            <p class="param-value">{{eventDetail.c2}}</p>
          </div>
          <div class="param-field">
            <span class="param-name">MFR温度:</span>
            <p class="param-value">{{eventDetail.MFR_temperature}}</p>
          </div>
          <div class="param-field">
            <span class="param-name">MFR载入:</span>
            <p class="param-value">{{eventDetail.MFR_loading}}</p>
          </div>
          <div class="param-field">
            <span class="param-name">测量的MFR:</span>
            <p class="param-value">{{eventDetail.measured_MFR}}</p>
          </div>
        </div>
      </button>
    </div>
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
    const showingPhy = ref(false)
    const showingTemp = ref(false)
    const showingPVT = ref(false)
    const showingP7 = ref(false)
    const showingOther = ref(false)

    const togglePhy = () => {
      showingPhy.value = !showingPhy.value
    }

    const toggleTemp = () => {
      showingTemp.value = !showingTemp.value
    }

    const togglePVT = () => {
      showingPVT.value = !showingPVT.value
    }

    const toggleP7 = () => {
      showingP7.value = !showingP7.value
    }

    const toggleOther = () => {
      showingOther.value = !showingOther.value
    }

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
      showDetail,
      showingPhy, 
      togglePhy,
      showingTemp,
      toggleTemp,
      showingPVT,
      togglePVT,
      showingP7,
      toggleP7,
      showingOther,
      toggleOther
    }
  }
}
</script>

<style>
.detail-info-field {
  @apply m-1 flex flex-wrap items-center;
}

.text-info {
  @apply inline-block bg-white mx-1 px-2 py-1 rounded border-b-2;
}

.detail-param-info {
  @apply bg-gray-200 mx-14 my-2 rounded;
}

.params {
  @apply bg-white mx-5 my-2 rounded-sm;
}

.param-field {
  @apply text-sm flex flex-wrap mx-3 justify-between items-center;
}

.param-name {
  @apply text-xs;
}

.param-value {
  @apply px-1;
}
</style>