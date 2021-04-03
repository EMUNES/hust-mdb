<template>
  <div v-if="showModal" @click.self="closeThis"
  class="fixed z-40 inset-0 opacity-25 bg-black">
  </div>

  <div v-if="showModal"
  class="fixed z-50 inset-0 w-2/3 m-auto h-3/4 text-black bg-white overflow-x-hidden overflow-y-scroll">
    <div>
      <h1 class="text-xl m-5 pb-5 border-b-2 border-gray-300">热塑性材料信息表单</h1>
    </div>
    <form @submit.prevent="modify"
    class="text-left border-b-2 border-gray-300 mx-5">
      <div>
        <div class="detail-form-text">
          <label for="series">系列:</label> 
          <input class="text-info" :placeholder="eventDetail.series">
        </div>
        <div class="detail-form-text">
          <label for="mark">牌号:</label> 
          <input class="text-info" :placeholder="eventDetail.mark">
        </div>
        <div class="detail-form-text">
          <label for="manufacturer">制造商:</label> 
          <input class="text-info" :placeholder="eventDetail.manufacturer">
        </div>
        <div class="detail-form-text">
          <label for="acronym">缩写:</label> 
          <input class="text-info" :placeholder="eventDetail.acronym">
        </div>
        <div class="detail-form-text">
          <label for="link">链接:</label> 
          <input class="text-info" :placeholder="eventDetail.link">
        </div>
        <div class="detail-form-text">
          <label for="material_type">数据类型:</label> 
          <input class="text-info" :placeholder="eventDetail.material_type">
        </div>
        <div class="detail-form-text">
          <label for="data_source">数据来源:</label> 
          <input class="text-info" :placeholder="eventDetail.data_source">
        </div>
        <div class="detail-form-text">
          <label for="material_id">材料ID:</label> 
          <input class="text-info" :placeholder="eventDetail.material_id">
        </div>
        <div class="detail-form-text">
          <label for="level_code">等级代码:</label> 
          <input class="text-info" :placeholder="eventDetail.level_code">
        </div>
        <div class="detail-form-text">
          <label for="vendor_code">供应商代码:</label> 
          <input class="text-info" :placeholder="eventDetail.vendor_code">
        </div>
        <div class="detail-form-text">
          <label for="fibre_or_infill">纤维、填充物:</label> 
          <input class="text-info" :placeholder="eventDetail.fibre_or_infill">
        </div>
        
        <div>
          <div class="head">
            <span class="form-params-title">
              物理参数信息
            </span>
          </div>
          <div class="form-param-field">
            <label for="maximum_shear_stress">最大剪切应力:</label>
            <input :placeholder="eventDetail.maximum_shear_stress">
          </div>
          <div class="form-param-field">
            <label for="maximum_shear_rate">最大剪切速率:</label>
            <input :placeholder="eventDetail.maximum_shear_rate">
          </div>
          <div class="form-param-field">
            <label for="melt_density">熔体密度:</label>
            <input :placeholder="eventDetail.melt_density">
          </div>
          <div class="form-param-field">
            <label for="solid_density">固体密度:</label>
            <input :placeholder="eventDetail.solid_density">
          </div>
          <div class="form-param-field">
            <label for="elastic_modulus_e1">弹性模量E1:</label>
            <input :placeholder="eventDetail.elastic_modulus_e1">
          </div>
          <div class="form-param-field">
            <label for="elastic_modulus_e2">弹性模量E2:</label>
            <input :placeholder="eventDetail.elastic_modulus_e2">
          </div>
          <div class="form-param-field">
            <label for="poisson_ratio_v12">泊松比v12:</label>
            <input :placeholder="eventDetail.poisson_ratio_v12">
          </div>
          <div class="form-param-field">
            <label for="poisson_ratio_v23">泊松比v23:</label>
            <input :placeholder="eventDetail.poisson_ratio_v23">
          </div>
          <div class="form-param-field">
            <label for="shear_modulus_g12">剪切模量G12:</label>
            <input :placeholder="eventDetail.shear_modulus_g12">
          </div>
          <div class="form-param-field">
            <label for="thermal_expansion_data_transverse_isotropic_coefficient_alpha1">热膨胀数据横向各向同性系数alpha1:</label>
            <input :placeholder="eventDetail.thermal_expansion_data_transverse_isotropic_coefficient_alpha1">
          </div>
          <div class="form-param-field">
            <label for="thermal_expansion_data_transverse_isotropic_coefficient_alpha2">热膨胀数据横向各向同性系数alpha2:</label>
            <input :placeholder="eventDetail.thermal_expansion_data_transverse_isotropic_coefficient_alpha2">
          </div>
        </div>

        <div>
          <div class="head">
            <span class="form-params-title">
              温度参数信息
            </span>
          </div>
          <div class="form-param-field">
            <label for="model_surface_temperature">模具表面温度:</label>
            <input :placeholder="eventDetail.model_surface_temperature">
          </div>
          <div class="form-param-field">
            <label for="melt_temperature">熔体温度:</label>
            <input :placeholder="eventDetail.melt_temperature">
          </div>
          <div class="form-param-field">
            <label for="mold_temperature_range_min">模具温度范围（最小值）:</label>
            <input :placeholder="eventDetail.mold_temperature_range_min">
          </div>
          <div class="form-param-field">
            <label for="mold_temperature_range_max">模具温度范围（最大值）:</label>
            <input :placeholder="eventDetail.mold_temperature_range_max">
          </div>
          <div class="form-param-field">
            <label for="melt_temperature_range_min">熔体温度范围（最小值）:</label>
            <input :placeholder="eventDetail.melt_temperature_range_min">
          </div>
          <div class="form-param-field">
            <label for="melt_temperature_range_max">熔体温度范围（最大值）:</label>
            <input :placeholder="eventDetail.melt_temperature_range_max">
          </div>
          <div class="form-param-field">
            <label for="absolute_maximum_melt_temperature">绝对最大溶体温度:</label>
            <input :placeholder="eventDetail.absolute_maximum_melt_temperature">
          </div>
          <div class="form-param-field">
            <label for="ejection_temperature">顶出温度:</label>
            <input :placeholder="eventDetail.ejection_temperature">
          </div>
          <div class="form-param-field">
            <label for="conversion_temperature">转换温度:</label>
            <input :placeholder="eventDetail.conversion_temperature">
          </div>     
        </div>

        <div>
          <div class="head">
            <span class="form-params-title">
              pvt参数信息
            </span>
          </div>
          <div class="form-param-field">
            <label for="pvt_b5">pvt_b5:</label>
            <input :placeholder="eventDetail.pvt_b5">
          </div>
          <div class="form-param-field">
            <label for="pvt_b6">pvt_b6:</label>
            <input :placeholder="eventDetail.pvt_b6">
          </div>
          <div class="form-param-field">
            <label for="pvt_b1m">pvt_b1m:</label>
            <input :placeholder="eventDetail.pvt_b1m">
          </div>
          <div class="form-param-field">
            <label for="pvt_b2m">pvt_b2m:</label>
            <input :placeholder="eventDetail.pvt_b2m">
          </div>
          <div class="form-param-field">
            <label for="pvt_b3m">pvt_b3m:</label>
            <input :placeholder="eventDetail.pvt_b3m">
          </div>
          <div class="form-param-field">
            <label for="pvt_b4m">pvt_b4m:</label>
            <input :placeholder="eventDetail.pvt_b4m">
          </div>
          <div class="form-param-field">
            <label for="pvt_b1s">pvt_b1s:</label>
            <input :placeholder="eventDetail.pvt_b1s">
          </div>
          <div class="form-param-field">
            <label for="pvt_b2s">pvt_b2s:</label>
            <input :placeholder="eventDetail.pvt_b2s">
          </div>
          <div class="form-param-field">
            <label for="pvt_b3s">pvt_b3s:</label>
            <input :placeholder="eventDetail.pvt_b3s">
          </div>   
          <div class="form-param-field">
            <label for="pvt_b4s">pvt_b4s:</label>
            <input :placeholder="eventDetail.pvt_b4s">
          </div>
          <div class="form-param-field">
            <label for="pvt_b7">pvt_b7:</label>
            <input :placeholder="eventDetail.pvt_b7">
          </div>
          <div class="form-param-field">
            <label for="pvt_b8">pvt_b8:</label>
            <input :placeholder="eventDetail.pvt_b8">
          </div>
          <div class="form-param-field">
            <label for="pvt_b9">pvt_b9:</label>
            <input :placeholder="eventDetail.pvt_b9">
          </div> 
        </div>

        <div>
          <div class="head">
            <span class="form-params-title">
              七参数信息
            </span>
          </div>
          <div class="form-param-field">
            <label for="seven_params_n">七参数n:</label>
            <input :placeholder="eventDetail.seven_params_n">
          </div>
          <div class="form-param-field">
            <label for="seven_params_Tau">七参数Tau:</label>
            <input :placeholder="eventDetail.seven_params_Tau">
          </div>
          <div class="form-param-field">
            <label for="seven_params_D1">七参数D1:</label>
            <input :placeholder="eventDetail.seven_params_D1">
          </div>
          <div class="form-param-field">
            <label for="seven_params_D2">七参数D2:</label>
            <input :placeholder="eventDetail.seven_params_D2">
          </div>
          <div class="form-param-field">
            <label for="seven_params_D3">七参数D3:</label>
            <input :placeholder="eventDetail.seven_params_D3">
          </div>
          <div class="form-param-field">
            <label for="seven_params_A1">七参数A1:</label>
            <input :placeholder="eventDetail.seven_params_A1">
          </div>
          <div class="form-param-field">
            <label for="seven_params_A2">七参数A2:</label>
            <input :placeholder="eventDetail.seven_params_A2">
          </div>
        </div>

        <div>
          <div class="head">
            <span class="form-params-title">
              其它参数（MFR、c1、c2等）
            </span>
          </div>
          <div class="form-param-field">
            <label for="c1">c1:</label>
            <input :placeholder="eventDetail.c1">
          </div>
          <div class="form-param-field">
            <label for="c2">c2:</label>
            <input :placeholder="eventDetail.c2">
          </div>
          <div class="form-param-field">
            <label for="MFR_temperature">MFR温度:</label>
            <input :placeholder="eventDetail.MFR_temperature">
          </div>
          <div class="form-param-field">
            <label for="MFR_loading">MFR载入:</label>
            <input :placeholder="eventDetail.MFR_loading">
          </div>
          <div class="form-param-field">
            <label for="measured_MFR">测量的MFR:</label>
            <input :placeholder="eventDetail.measured_MFR">
          </div>
        </div>
      </div>

      <div class="text-center flex justify-around items-center my-3">
        <button type="submit">
          <svg t="1617439778736" class="h-10 w-10 rounded-full opacity-60" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="3047" width="200" height="200"><path d="M853.333333 96c40.533333 0 74.666667 34.133333 74.666667 74.666667v682.666666c0 40.533333-34.133333 74.666667-74.666667 74.666667H170.666667c-40.533333 0-74.666667-34.133333-74.666667-74.666667V170.666667c0-40.533333 34.133333-74.666667 74.666667-74.666667h682.666666zM748.8 384c-12.8-12.8-32-12.8-44.8 0L460.8 616.533333 343.466667 490.666667l-2.133334-2.133334c-12.8-10.666667-29.866667-10.666667-42.666666 0-12.8 12.8-12.8 32-2.133334 44.8l140.8 149.333334 2.133334 2.133333c12.8 10.666667 32 10.666667 42.666666-2.133333L746.666667 426.666667l2.133333-2.133334c10.666667-10.666667 10.666667-29.866667 0-40.533333z" p-id="3048"></path></svg>
        </button>
        <button @click="closeThis">
          <svg t="1617439861275" class="h-10 w-10 rounded-full opacity-60" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="3183" width="200" height="200"><path d="M853.333333 96H170.666667C130.133333 96 96 130.133333 96 170.666667v682.666666c0 40.533333 34.133333 74.666667 74.666667 74.666667h682.666666c40.533333 0 74.666667-34.133333 74.666667-74.666667V170.666667c0-40.533333-34.133333-74.666667-74.666667-74.666667z m-128 448H298.666667c-17.066667 0-32-14.933333-32-32s14.933333-32 32-32h426.666666c17.066667 0 32 14.933333 32 32s-14.933333 32-32 32z" p-id="3184"></path></svg>
        </button>
      </div>
    </form>
  </div>
</template>

<script>
export default {
  name: 'MaterialModal',
  props: {
    showModal: {
      type: Boolean,
      required: true
    },
    eventDetail: {
      type: Object,
      required: false
    }
  },
  emits: [
    'close'
  ],
  setup(props, context) {
    const closeThis = () => {
      context.emit('close')
    }

    const modify = () => {
      console.log('submitted')
    }

    return {
      closeThis,
      modify
    }
  }
}
</script>

<style>
.form-params-title {
  @apply text-lg mx-2 mt-3 block border-b-2 border-dotted;
}

.form-param-field {
  @apply flex items-center justify-between text-sm my-1 py-1 px-2 border-b-2 border-l-2 border-gray-400;
}

.form-param-field input{
  @apply outline-none;
}

.detail-form-text {
  @apply my-1 px-2 border-2 border-gray-400 rounded;
}

.detail-form-text input {
  @apply outline-none;
}
</style>