<template>
  <div v-if="showModal" @click.self="closeThis"
  class="fixed z-40 inset-0 opacity-25 bg-black">
  </div>

  <div v-if="showModal"
  class="fixed z-50 inset-0 w-2/3 m-auto h-3/4 text-black bg-white overflow-x-hidden overflow-y-scroll max-w-4xl">
    <div>
      <h1 class="text-xl m-5 pb-5 border-b-2 border-gray-300">热塑性材料信息表单</h1>
    </div>
    <form @submit.prevent="modifyDetail"
    class="text-left border-b-2 border-gray-300 mx-5">
      <div>
        <div class="detail-form-text">
          <label for="series">系列:</label> 
          <input class="text-info" :placeholder="eventDetail.series" v-model="series">
        </div>
        <div class="detail-form-text">
          <label for="mark">牌号:</label> 
          <input class="text-info" :placeholder="eventDetail.mark" v-model="mark">
        </div>
        <div class="detail-form-text">
          <label for="manufacturer">制造商:</label> 
          <input class="text-info" :placeholder="eventDetail.manufacturer" v-model="manufacturer">
        </div>
        <div class="detail-form-text">
          <label for="acronym">缩写:</label> 
          <input class="text-info" :placeholder="eventDetail.acronym" v-model="acronym">
        </div>
        <div class="detail-form-text">
          <label for="link">链接:</label> 
          <input class="text-info" :placeholder="eventDetail.link" v-model="link">
        </div>
        <div class="detail-form-text">
          <label for="material_type">数据类型:</label> 
          <input class="text-info" :placeholder="eventDetail.material_type" v-model="material_type">
        </div>
        <div class="detail-form-text">
          <label for="data_source">数据来源:</label> 
          <input class="text-info" :placeholder="eventDetail.data_source" v-model="data_source">
        </div>
        <div class="detail-form-text">
          <label for="material_id">材料ID:</label> 
          <input class="text-info" :placeholder="eventDetail.material_id" v-model="material_id">
        </div>
        <div class="detail-form-text">
          <label for="level_code">等级代码:</label> 
          <input class="text-info" :placeholder="eventDetail.level_code" v-model="level_code">
        </div>
        <div class="detail-form-text">
          <label for="vendor_code">供应商代码:</label> 
          <input class="text-info" :placeholder="eventDetail.vendor_code" v-model="vendor_code">
        </div>
        <div class="detail-form-text">
          <label for="fibre_or_infill">纤维、填充物:</label> 
          <input class="text-info" :placeholder="eventDetail.fibre_or_infill" v-model="fibre_or_infill">
        </div>
        
        <div>
          <div class="head">
            <span class="form-params-title">
              物理参数信息
            </span>
          </div>
          <div class="form-param-field">
            <label for="maximum_shear_stress">最大剪切应力:</label>
            <input :placeholder="eventDetail.maximum_shear_stress" v-model="maximum_shear_stress">
          </div>
          <div class="form-param-field">
            <label for="maximum_shear_rate">最大剪切速率:</label>
            <input :placeholder="eventDetail.maximum_shear_rate" v-model="maximum_shear_rate">
          </div>
          <div class="form-param-field">
            <label for="melt_density">熔体密度:</label>
            <input :placeholder="eventDetail.melt_density" v-model="melt_density">
          </div>
          <div class="form-param-field">
            <label for="solid_density">固体密度:</label>
            <input :placeholder="eventDetail.solid_density" v-model="solid_density">
          </div>
          <div class="form-param-field">
            <label for="elastic_modulus_e1">弹性模量E1:</label>
            <input :placeholder="eventDetail.elastic_modulus_e1" v-model="elastic_modulus_e1">
          </div>
          <div class="form-param-field">
            <label for="elastic_modulus_e2">弹性模量E2:</label>
            <input :placeholder="eventDetail.elastic_modulus_e2" v-model="elastic_modulus_e2">
          </div>
          <div class="form-param-field">
            <label for="poisson_ratio_v12">泊松比v12:</label>
            <input :placeholder="eventDetail.poisson_ratio_v12" v-model="poisson_ratio_v12">
          </div>
          <div class="form-param-field">
            <label for="poisson_ratio_v23">泊松比v23:</label>
            <input :placeholder="eventDetail.poisson_ratio_v23" v-model="poisson_ratio_v23">
          </div>
          <div class="form-param-field">
            <label for="shear_modulus_g12">剪切模量G12:</label>
            <input :placeholder="eventDetail.shear_modulus_g12" v-model="shear_modulus_g12">
          </div>
          <div class="form-param-field">
            <label for="thermal_expansion_data_transverse_isotropic_coefficient_alpha1">热膨胀数据横向各向同性系数alpha1:</label>
            <input :placeholder="eventDetail.thermal_expansion_data_transverse_isotropic_coefficient_alpha1" v-model="thermal_expansion_data_transverse_isotropic_coefficient_alpha1">
          </div>
          <div class="form-param-field">
            <label for="thermal_expansion_data_transverse_isotropic_coefficient_alpha2">热膨胀数据横向各向同性系数alpha2:</label>
            <input :placeholder="eventDetail.thermal_expansion_data_transverse_isotropic_coefficient_alpha2" v-model="thermal_expansion_data_transverse_isotropic_coefficient_alpha2">
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
            <input :placeholder="eventDetail.model_surface_temperature" v-model="model_surface_temperature">
          </div>
          <div class="form-param-field">
            <label for="melt_temperature">熔体温度:</label>
            <input :placeholder="eventDetail.melt_temperature" v-model="melt_temperature">
          </div>
          <div class="form-param-field">
            <label for="mold_temperature_range_min">模具温度范围（最小值）:</label>
            <input :placeholder="eventDetail.mold_temperature_range_min" v-model="mold_temperature_range_min">
          </div>
          <div class="form-param-field">
            <label for="mold_temperature_range_max">模具温度范围（最大值）:</label>
            <input :placeholder="eventDetail.mold_temperature_range_max" v-model="mold_temperature_range_max">
          </div>
          <div class="form-param-field">
            <label for="melt_temperature_range_min">熔体温度范围（最小值）:</label>
            <input :placeholder="eventDetail.melt_temperature_range_min" v-model="melt_temperature_range_min">
          </div>
          <div class="form-param-field">
            <label for="melt_temperature_range_max">熔体温度范围（最大值）:</label>
            <input :placeholder="eventDetail.melt_temperature_range_max" v-model="melt_temperature_range_max">
          </div>
          <div class="form-param-field">
            <label for="absolute_maximum_melt_temperature">绝对最大溶体温度:</label>
            <input :placeholder="eventDetail.absolute_maximum_melt_temperature" v-model="absolute_maximum_melt_temperature">
          </div>
          <div class="form-param-field">
            <label for="ejection_temperature">顶出温度:</label>
            <input :placeholder="eventDetail.ejection_temperature" v-model="ejection_temperature">
          </div>
          <div class="form-param-field">
            <label for="conversion_temperature">转换温度:</label>
            <input :placeholder="eventDetail.conversion_temperature" v-model="conversion_temperature">
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
            <input :placeholder="eventDetail.pvt_b5" v-model="pvt_b5">
          </div>
          <div class="form-param-field">
            <label for="pvt_b6">pvt_b6:</label>
            <input :placeholder="eventDetail.pvt_b6" v-model="pvt_b6">
          </div>
          <div class="form-param-field">
            <label for="pvt_b1m">pvt_b1m:</label>
            <input :placeholder="eventDetail.pvt_b1m" v-model="pvt_b1m">
          </div>
          <div class="form-param-field">
            <label for="pvt_b2m">pvt_b2m:</label>
            <input :placeholder="eventDetail.pvt_b2m" v-model="pvt_b2m">
          </div>
          <div class="form-param-field">
            <label for="pvt_b3m">pvt_b3m:</label>
            <input :placeholder="eventDetail.pvt_b3m" v-model="pvt_b3m">
          </div>
          <div class="form-param-field">
            <label for="pvt_b4m">pvt_b4m:</label>
            <input :placeholder="eventDetail.pvt_b4m" v-model="pvt_b4m">
          </div>
          <div class="form-param-field">
            <label for="pvt_b1s">pvt_b1s:</label>
            <input :placeholder="eventDetail.pvt_b1s" v-model="pvt_b1s">
          </div>
          <div class="form-param-field">
            <label for="pvt_b2s">pvt_b2s:</label>
            <input :placeholder="eventDetail.pvt_b2s" v-model="pvt_b2s">
          </div>
          <div class="form-param-field">
            <label for="pvt_b3s">pvt_b3s:</label>
            <input :placeholder="eventDetail.pvt_b3s" v-model="pvt_b3s">
          </div>   
          <div class="form-param-field">
            <label for="pvt_b4s">pvt_b4s:</label>
            <input :placeholder="eventDetail.pvt_b4s" v-model="pvt_b4s">
          </div>
          <div class="form-param-field">
            <label for="pvt_b7">pvt_b7:</label>
            <input :placeholder="eventDetail.pvt_b7" v-model="pvt_b7">
          </div>
          <div class="form-param-field">
            <label for="pvt_b8">pvt_b8:</label>
            <input :placeholder="eventDetail.pvt_b8" v-model="pvt_b8">
          </div>
          <div class="form-param-field">
            <label for="pvt_b9">pvt_b9:</label>
            <input :placeholder="eventDetail.pvt_b9" v-model="pvt_b9">
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
            <input :placeholder="eventDetail.seven_params_n" v-model="seven_params_n">
          </div>
          <div class="form-param-field">
            <label for="seven_params_Tau">七参数Tau:</label>
            <input :placeholder="eventDetail.seven_params_Tau" v-model="seven_params_Tau">
          </div>
          <div class="form-param-field">
            <label for="seven_params_D1">七参数D1:</label>
            <input :placeholder="eventDetail.seven_params_D1" v-model="seven_params_D1">
          </div>
          <div class="form-param-field">
            <label for="seven_params_D2">七参数D2:</label>
            <input :placeholder="eventDetail.seven_params_D2" v-model="seven_params_D2">
          </div>
          <div class="form-param-field">
            <label for="seven_params_D3">七参数D3:</label>
            <input :placeholder="eventDetail.seven_params_D3" v-model="seven_params_D3">
          </div>
          <div class="form-param-field">
            <label for="seven_params_A1">七参数A1:</label>
            <input :placeholder="eventDetail.seven_params_A1" v-model="seven_params_A1">
          </div>
          <div class="form-param-field">
            <label for="seven_params_A2">七参数A2:</label>
            <input :placeholder="eventDetail.seven_params_A2" v-model="seven_params_A2">
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
            <input :placeholder="eventDetail.c1" v-model="c1">
          </div>
          <div class="form-param-field">
            <label for="c2">c2:</label>
            <input :placeholder="eventDetail.c2" v-model="c2">
          </div>
          <div class="form-param-field">
            <label for="MFR_temperature">MFR温度:</label>
            <input :placeholder="eventDetail.MFR_temperature" v-model="MFR_temperature">
          </div>
          <div class="form-param-field">
            <label for="MFR_loading">MFR载入:</label>
            <input :placeholder="eventDetail.MFR_loading" v-model="MFR_loading">
          </div>
          <div class="form-param-field">
            <label for="measured_MFR">测量的MFR:</label>
            <input :placeholder="eventDetail.measured_MFR" v-model="measured_MFR">
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
import { toRef, ref } from 'vue'
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
    'close',
    'modalFormSubmit'
  ],
  setup(props, context) {
    const eventDetail = toRef(props, 'eventDetail')
    const id = ref(eventDetail.value.id)
    const series = ref(eventDetail.value.series)
    const mark = ref(eventDetail.value.mark)
    const manufacturer = ref(eventDetail.value.manufacturer)
    const link = ref(eventDetail.value.link)
    const acronym = ref(eventDetail.value.acronym)
    const material_type = ref(eventDetail.value.material_type)
    const data_source = ref(eventDetail.value.data_source)
    const last_modified_date = ref(eventDetail.value.last_modified_date)
    const test_date = ref(eventDetail.value.test_date)
    const data_status = ref(eventDetail.value.data_status)
    const material_id = ref(eventDetail.value.material_id)
    const level_code = ref(eventDetail.value.level_code)
    const vendor_code = ref(eventDetail.value.vendor_code)
    const fibre_or_infill = ref(eventDetail.value.fibre_or_infill)
    const model_surface_temperature = ref(eventDetail.value.model_surface_temperature)
    const melt_temperature = ref(eventDetail.value.melt_temperature)
    const mold_temperature_range_min = ref(eventDetail.value.mold_temperature_range_min)
    const mold_temperature_range_max = ref(eventDetail.value.mold_temperature_range_max)
    const melt_temperature_range_min = ref(eventDetail.value.melt_temperature_range_min)
    const melt_temperature_range_max = ref(eventDetail.value.melt_temperature_range_max)
    const absolute_maximum_melt_temperature = ref(eventDetail.value.absolute_maximum_melt_temperature)
    const ejection_temperature = ref(eventDetail.value.ejection_temperature)
    const maximum_shear_stress = ref(eventDetail.value.maximum_shear_stress)
    const maximum_shear_rate = ref(eventDetail.value.maximum_shear_rate)
    const melt_density = ref(eventDetail.value.melt_density)
    const solid_density = ref(eventDetail.value.solid_density)
    const pvt_b5 = ref(eventDetail.value.pvt_b5)
    const pvt_b6 = ref(eventDetail.value.pvt_b6)
    const pvt_b1m = ref(eventDetail.value.pvt_b1m)
    const pvt_b2m = ref(eventDetail.value.pvt_b2m)
    const pvt_b3m = ref(eventDetail.value.pvt_b3m)
    const pvt_b4m = ref(eventDetail.value.pvt_b4m)
    const pvt_b1s = ref(eventDetail.value.pvt_b1s)
    const pvt_b2s = ref(eventDetail.value.pvt_b2s)
    const pvt_b3s = ref(eventDetail.value.pvt_b3s)
    const pvt_b4s = ref(eventDetail.value.pvt_b4s)
    const pvt_b7 = ref(eventDetail.value.pvt_b7)
    const pvt_b8 = ref(eventDetail.value.pvt_b8)
    const pvt_b9 = ref(eventDetail.value.pvt_b9)
    const elastic_modulus_e1 = ref(eventDetail.value.elastic_modulus_e1)
    const elastic_modulus_e2 = ref(eventDetail.value.elastic_modulus_e2)
    const poisson_ratio_v12 = ref(eventDetail.value.poisson_ratio_v12)
    const poisson_ratio_v23 = ref(eventDetail.value.poisson_ratio_v23)
    const shear_modulus_g12 = ref(eventDetail.value.shear_modulus_g12)
    const thermal_expansion_data_transverse_isotropic_coefficient_alpha1 = ref(eventDetail.value.thermal_expansion_data_transverse_isotropic_coefficient_alpha1)
    const thermal_expansion_data_transverse_isotropic_coefficient_alpha2 = ref(eventDetail.value.thermal_expansion_data_transverse_isotropic_coefficient_alpha2)
    const seven_params_n = ref(eventDetail.value.seven_params_n)
    const seven_params_Tau = ref(eventDetail.value.seven_params_Tau)
    const seven_params_D1 = ref(eventDetail.value.seven_params_D1)
    const seven_params_D2 = ref(eventDetail.value.seven_params_D2)
    const seven_params_D3 = ref(eventDetail.value.seven_params_D3)
    const seven_params_A1 = ref(eventDetail.value.seven_params_A1)
    const seven_params_A2 = ref(eventDetail.value.seven_params_A2)
    const c1 = ref(eventDetail.value.c1)
    const c2 = ref(eventDetail.value.c2)
    const conversion_temperature = ref(eventDetail.value.conversion_temperature)
    const MFR_temperature = ref(eventDetail.value.MFR_temperature)
    const MFR_loading = ref(eventDetail.value.MFR_loading)
    const measured_MFR = ref(eventDetail.value.measured_MFR)

    const closeThis = () => {
      context.emit('close')
    }

    const modifyDetail = () => {
      context.emit('modalFormSubmit', {
        id: id.value,
        series: series.value,
        mark: mark.value,
        manufacturer: manufacturer.value,
        link: link.value,
        acronym: acronym.value,
        material_type: material_type.value,
        data_source: data_source.value,
        last_modified_date: last_modified_date.value,
        test_date: test_date.value,
        data_status: data_status.value,
        material_id: material_id.value,
        level_code: level_code.value,
        vendor_code: vendor_code.value,
        fibre_or_infill: fibre_or_infill.value,
        model_surface_temperature: model_surface_temperature.value,
        melt_temperature: melt_temperature.value,
        mold_temperature_range_min: mold_temperature_range_min.value,
        mold_temperature_range_max: mold_temperature_range_max.value,
        melt_temperature_range_min: melt_temperature_range_min.value,
        melt_temperature_range_max: melt_temperature_range_max.value,
        absolute_maximum_melt_temperature: absolute_maximum_melt_temperature.value,
        ejection_temperature: ejection_temperature.value,
        maximum_shear_stress: maximum_shear_stress.value,
        maximum_shear_rate: maximum_shear_rate.value,
        melt_density: melt_density.value,
        solid_density: solid_density.value,
        pvt_b5: pvt_b5.value,
        pvt_b6: pvt_b6.value,
        pvt_b1m: pvt_b1m.value,
        pvt_b2m: pvt_b2m.value,
        pvt_b3m: pvt_b3m.value,
        pvt_b4m: pvt_b4m.value,
        pvt_b1s: pvt_b1s.value,
        pvt_b2s: pvt_b2s.value,
        pvt_b3s: pvt_b3s.value,
        pvt_b4s: pvt_b4s.value,
        pvt_b7: pvt_b7.value,
        pvt_b8: pvt_b8.value,
        pvt_b9: pvt_b9.value,
        elastic_modulus_e1: elastic_modulus_e1.value,
        elastic_modulus_e2: elastic_modulus_e2.value,
        poisson_ratio_v12: poisson_ratio_v12.value,
        poisson_ratio_v23: poisson_ratio_v23.value,
        shear_modulus_g12: shear_modulus_g12.value,
        thermal_expansion_data_transverse_isotropic_coefficient_alpha1: thermal_expansion_data_transverse_isotropic_coefficient_alpha1.value,
        thermal_expansion_data_transverse_isotropic_coefficient_alpha2: thermal_expansion_data_transverse_isotropic_coefficient_alpha2.value,
        seven_params_n: seven_params_n.value,
        seven_params_Tau: seven_params_Tau.value,
        seven_params_D1: seven_params_D1.value,
        seven_params_D2: seven_params_D2.value,
        seven_params_D3: seven_params_D3.value,
        seven_params_A1: seven_params_A1.value,
        seven_params_A2: seven_params_A2.value,
        c1: c1.value,
        c2: c2.value,
        conversion_temperature: conversion_temperature.value,
        MFR_temperature: MFR_temperature.value,
        MFR_loading: MFR_loading.value,
        measured_MFR: measured_MFR.value
      })
      closeThis()
    }

    return {
      closeThis,
      modifyDetail,
      series,
      mark,
      manufacturer,
      link,
      acronym,
      material_type,
      data_source,
      last_modified_date,
      test_date,
      data_status,
      material_id,
      level_code,
      vendor_code,
      fibre_or_infill,
      model_surface_temperature,
      melt_temperature,
      mold_temperature_range_min,
      mold_temperature_range_max,
      melt_temperature_range_min,
      melt_temperature_range_max,
      absolute_maximum_melt_temperature,
      ejection_temperature,
      maximum_shear_stress,
      maximum_shear_rate,
      melt_density,
      solid_density,
      pvt_b5,
      pvt_b6,
      pvt_b1m,
      pvt_b2m,
      pvt_b3m,
      pvt_b4m,
      pvt_b1s,
      pvt_b2s,
      pvt_b3s,
      pvt_b4s,
      pvt_b7,
      pvt_b8,
      pvt_b9,
      elastic_modulus_e1,
      elastic_modulus_e2,
      poisson_ratio_v12,
      poisson_ratio_v23,
      shear_modulus_g12,
      thermal_expansion_data_transverse_isotropic_coefficient_alpha1,
      thermal_expansion_data_transverse_isotropic_coefficient_alpha2,
      seven_params_n,
      seven_params_Tau,
      seven_params_D1,
      seven_params_D2,
      seven_params_D3,
      seven_params_A1,
      seven_params_A2,
      c1,
      c2,
      conversion_temperature,
      MFR_temperature,
      MFR_loading,
      measured_MFR
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
  @apply outline-none text-gray-500;
}

.detail-form-text {
  @apply my-1 px-2 border-2 border-gray-400 rounded;
}

.detail-form-text input {
  @apply outline-none text-gray-500 w-4/5 min-w-max;
}
</style>