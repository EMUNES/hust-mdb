<template>
  <slot>

  </slot>
  <!-- Detailed information for the drop page. -->
  <!-- A great trick for list transtion is here! Use abosulte while leaving!!! -->
  <transition 
  enter-active-class="transition duration-700 ease-out"
  enter-from-class="opacity-0 scale-75"
  enter-to-class="opacity-100 scale-100"
  leave-active-class="transition duration-500 ease-in absolute max-w-2xl"
  leave-from-class="opacity-100 scale-100"
  leave-to-class="opacity-0 scale-50">
    <div v-if="showDetail"
    class="mx-10 border-2 border-gray-500 rounded-xl">
      <div class="detail-bar flex items-center justify-between border-b-2">
        <h4 class="text-2xl my-2 ml-3 p-2">
          材料详细信息
        </h4>

        <div class="mr-5">
          <button @click.prevent="toggleAll" >
            <svg v-if="!showingAll" 
            t="1617420789815" class="h-7 w-7 opacity-50" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="2915" width="200" height="200">
              <path d="M512 836.266667C230.4 836.266667 74.666667 533.333333 68.266667 520.533333c-4.266667-8.533333-4.266667-19.2 0-29.866666 6.4-12.8 164.266667-315.733333 443.733333-315.733334 281.6 0 437.333333 305.066667 443.733333 317.866667 4.266667 8.533333 4.266667 19.2 0 29.866667-6.4 10.666667-162.133333 313.6-443.733333 313.6zM132.266667 505.6c34.133333 57.6 170.666667 266.666667 379.733333 266.666667s345.6-209.066667 379.733333-266.666667c-34.133333-57.6-170.666667-266.666667-379.733333-266.666667S166.4 448 132.266667 505.6z" p-id="2916"></path><path d="M512 650.666667c-76.8 0-138.666667-61.866667-138.666667-138.666667s61.866667-138.666667 138.666667-138.666667 138.666667 61.866667 138.666667 138.666667-61.866667 138.666667-138.666667 138.666667z m0-213.333334c-40.533333 0-74.666667 34.133333-74.666667 74.666667s34.133333 74.666667 74.666667 74.666667 74.666667-34.133333 74.666667-74.666667-34.133333-74.666667-74.666667-74.666667z" p-id="2917"></path>
            </svg>
            <svg v-if="showingAll"
            t="1617420945505" class="h-7 w-7 opacity-50" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="3052" width="200" height="200">
              <path d="M917.333333 573.866667l-87.466666-87.466667c34.133333-32 66.133333-68.266667 91.733333-108.8 8.533333-14.933333 4.266667-34.133333-10.666667-44.8-14.933333-8.533333-34.133333-4.266667-44.8 10.666667-76.8 125.866667-209.066667 200.533333-356.266666 200.533333-145.066667 0-279.466667-74.666667-354.133334-198.4-8.533333-14.933333-29.866667-19.2-44.8-10.666667-14.933333 8.533333-19.2 29.866667-10.666666 44.8 25.6 40.533333 55.466667 76.8 91.733333 108.8l-85.333333 85.333334c-12.8 12.8-12.8 32 0 44.8 6.4 6.4 14.933333 8.533333 23.466666 8.533333s17.066667-2.133333 23.466667-8.533333l91.733333-91.733334c38.4 25.6 81.066667 46.933333 125.866667 59.733334l-34.133333 130.133333c-4.266667 17.066667 6.4 34.133333 23.466666 38.4 2.133333 0 6.4 2.133333 8.533334 2.133333 14.933333 0 27.733333-8.533333 29.866666-23.466666l36.266667-132.266667c25.6 4.266667 51.2 6.4 78.933333 6.4 27.733333 0 55.466667-2.133333 83.2-6.4l36.266667 132.266667c4.266667 14.933333 17.066667 23.466667 29.866667 23.466666 2.133333 0 6.4 0 8.533333-2.133333 17.066667-4.266667 27.733333-21.333333 23.466667-38.4L661.333333 584.533333c44.8-12.8 85.333333-34.133333 123.733334-59.733333l91.733333 91.733333c6.4 6.4 14.933333 8.533333 23.466667 8.533334s17.066667-2.133333 23.466666-8.533334c6.4-10.666667 6.4-29.866667-6.4-42.666666z" p-id="3053"></path>
            </svg>
          </button>

          <button @click="toggleModal" class="mx-5">
            <svg t="1617421105074" class="h-7 w-7 opacity-50" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="3316" width="200" height="200"><path d="M522.666667 458.666667c-17.066667 0-32 14.933333-32 32v362.666666c0 17.066667 14.933333 32 32 32S554.666667 870.4 554.666667 853.333333V490.666667c0-17.066667-14.933333-32-32-32zM341.333333 554.666667H106.666667c-17.066667 0-32 14.933333-32 32S89.6 618.666667 106.666667 618.666667h74.666666v234.666666c0 17.066667 14.933333 32 32 32s32-14.933333 32-32V618.666667H341.333333c17.066667 0 32-14.933333 32-32S358.4 554.666667 341.333333 554.666667zM693.333333 373.333333c0-17.066667-14.933333-32-32-32h-106.666666V170.666667c0-17.066667-14.933333-32-32-32S490.666667 153.6 490.666667 170.666667v170.666666h-106.666667c-17.066667 0-32 14.933333-32 32S366.933333 405.333333 384 405.333333h277.333333c17.066667 0 32-14.933333 32-32zM917.333333 618.666667H682.666667c-17.066667 0-32 14.933333-32 32S665.6 682.666667 682.666667 682.666667h96v170.666666c0 17.066667 14.933333 32 32 32s32-14.933333 32-32v-170.666666H917.333333c17.066667 0 32-14.933333 32-32S934.4 618.666667 917.333333 618.666667zM213.333333 458.666667c17.066667 0 32-14.933333 32-32V170.666667c0-17.066667-14.933333-32-32-32S181.333333 153.6 181.333333 170.666667v256c0 17.066667 14.933333 32 32 32zM810.666667 522.666667c17.066667 0 32-14.933333 32-32V170.666667c0-17.066667-14.933333-32-32-32s-32 14.933333-32 32v320c0 17.066667 14.933333 32 32 32z" p-id="3317"></path></svg>
          </button>

          <button @click="deleteMaterial" class="mr-5"> 
            <svg t="1617550603711" class="h-7 w-7 opacity-50" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="11841" width="200" height="200"><path d="M341.013333 394.666667l27.754667 393.450666h271.829333l27.733334-393.450666h64.106666L704.426667 792.618667a64 64 0 0 1-63.829334 59.498666H368.768a64 64 0 0 1-63.829333-59.52L276.885333 394.666667h64.128z m139.306667 19.818666v298.666667h-64v-298.666667h64z m117.013333 0v298.666667h-64v-298.666667h64zM181.333333 288h640v64h-640v-64z m453.482667-106.666667v64h-256v-64h256z" p-id="11842"></path></svg>
          </button>

          <button @click.prevent="showDetail=false">
            <svg 
            t="1617421012551" class="h-7 w-7 opacity-50" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="3184" width="200" height="200"><path d="M556.8 512L832 236.8c12.8-12.8 12.8-32 0-44.8-12.8-12.8-32-12.8-44.8 0L512 467.2l-275.2-277.333333c-12.8-12.8-32-12.8-44.8 0-12.8 12.8-12.8 32 0 44.8l275.2 277.333333-277.333333 275.2c-12.8 12.8-12.8 32 0 44.8 6.4 6.4 14.933333 8.533333 23.466666 8.533333s17.066667-2.133333 23.466667-8.533333L512 556.8 787.2 832c6.4 6.4 14.933333 8.533333 23.466667 8.533333s17.066667-2.133333 23.466666-8.533333c12.8-12.8 12.8-32 0-44.8L556.8 512z" p-id="3185"></path></svg>
          </button>
        </div>
      </div>
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
      <div class="grid grid-cols-2 items-start bg-blue-50 border-b-2 border-gray-300">
        <button class="detail-param-info" @click="togglePhy">
          <div class="head">
            <span class="params-title">
              物理参数信息
            </span>
            <svg v-if="!showingPhy" t="1617333230208" class="inline h-3 w-3" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="2915" width="200" height="200"><path d="M268.8 480L633.6 149.333333c17.066667-14.933333 44.8-14.933333 59.733333 2.133334 6.4 8.533333 10.666667 19.2 10.666667 29.866666v661.333334c0 23.466667-19.2 42.666667-42.666667 42.666666-10.666667 0-21.333333-4.266667-27.733333-10.666666l-362.666667-330.666667c-17.066667-14.933333-19.2-42.666667-2.133333-59.733333-2.133333-2.133333 0-2.133333 0-4.266667z" p-id="2916"></path>
            </svg>
            <svg v-if="showingPhy" t="1617333301312" class="inline h-3 w-3" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="3051" width="200" height="200"><path d="M482.133333 738.133333L136.533333 392.533333c-17.066667-17.066667-17.066667-42.666667 0-59.733333 8.533333-8.533333 19.2-12.8 29.866667-12.8h689.066667c23.466667 0 42.666667 19.2 42.666666 42.666667 0 10.666667-4.266667 21.333333-12.8 29.866666L541.866667 738.133333c-17.066667 17.066667-42.666667 17.066667-59.733334 0z" p-id="3052"></path>
            </svg>
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
            <svg v-if="!showingTemp" t="1617333230208" class="inline h-3 w-3" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="2915" width="200" height="200"><path d="M268.8 480L633.6 149.333333c17.066667-14.933333 44.8-14.933333 59.733333 2.133334 6.4 8.533333 10.666667 19.2 10.666667 29.866666v661.333334c0 23.466667-19.2 42.666667-42.666667 42.666666-10.666667 0-21.333333-4.266667-27.733333-10.666666l-362.666667-330.666667c-17.066667-14.933333-19.2-42.666667-2.133333-59.733333-2.133333-2.133333 0-2.133333 0-4.266667z" p-id="2916"></path>
            </svg>
            <svg v-if="showingTemp" t="1617333301312" class="inline h-3 w-3" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="3051" width="200" height="200"><path d="M482.133333 738.133333L136.533333 392.533333c-17.066667-17.066667-17.066667-42.666667 0-59.733333 8.533333-8.533333 19.2-12.8 29.866667-12.8h689.066667c23.466667 0 42.666667 19.2 42.666666 42.666667 0 10.666667-4.266667 21.333333-12.8 29.866666L541.866667 738.133333c-17.066667 17.066667-42.666667 17.066667-59.733334 0z" p-id="3052"></path>
            </svg>
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
            <svg v-if="!showingPVT" t="1617333230208" class="inline h-3 w-3" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="2915" width="200" height="200"><path d="M268.8 480L633.6 149.333333c17.066667-14.933333 44.8-14.933333 59.733333 2.133334 6.4 8.533333 10.666667 19.2 10.666667 29.866666v661.333334c0 23.466667-19.2 42.666667-42.666667 42.666666-10.666667 0-21.333333-4.266667-27.733333-10.666666l-362.666667-330.666667c-17.066667-14.933333-19.2-42.666667-2.133333-59.733333-2.133333-2.133333 0-2.133333 0-4.266667z" p-id="2916"></path>
            </svg>
            <svg v-if="showingPVT" t="1617333301312" class="inline h-3 w-3" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="3051" width="200" height="200"><path d="M482.133333 738.133333L136.533333 392.533333c-17.066667-17.066667-17.066667-42.666667 0-59.733333 8.533333-8.533333 19.2-12.8 29.866667-12.8h689.066667c23.466667 0 42.666667 19.2 42.666666 42.666667 0 10.666667-4.266667 21.333333-12.8 29.866666L541.866667 738.133333c-17.066667 17.066667-42.666667 17.066667-59.733334 0z" p-id="3052"></path>
            </svg>
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
            <svg v-if="!showingP7" t="1617333230208" class="inline h-3 w-3" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="2915" width="200" height="200"><path d="M268.8 480L633.6 149.333333c17.066667-14.933333 44.8-14.933333 59.733333 2.133334 6.4 8.533333 10.666667 19.2 10.666667 29.866666v661.333334c0 23.466667-19.2 42.666667-42.666667 42.666666-10.666667 0-21.333333-4.266667-27.733333-10.666666l-362.666667-330.666667c-17.066667-14.933333-19.2-42.666667-2.133333-59.733333-2.133333-2.133333 0-2.133333 0-4.266667z" p-id="2916"></path>
            </svg>
            <svg v-if="showingP7" t="1617333301312" class="inline h-3 w-3" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="3051" width="200" height="200"><path d="M482.133333 738.133333L136.533333 392.533333c-17.066667-17.066667-17.066667-42.666667 0-59.733333 8.533333-8.533333 19.2-12.8 29.866667-12.8h689.066667c23.466667 0 42.666667 19.2 42.666666 42.666667 0 10.666667-4.266667 21.333333-12.8 29.866666L541.866667 738.133333c-17.066667 17.066667-42.666667 17.066667-59.733334 0z" p-id="3052"></path>
            </svg>
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
            <svg v-if="!showingOther" t="1617333230208" class="inline h-3 w-3" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="2915" width="200" height="200"><path d="M268.8 480L633.6 149.333333c17.066667-14.933333 44.8-14.933333 59.733333 2.133334 6.4 8.533333 10.666667 19.2 10.666667 29.866666v661.333334c0 23.466667-19.2 42.666667-42.666667 42.666666-10.666667 0-21.333333-4.266667-27.733333-10.666666l-362.666667-330.666667c-17.066667-14.933333-19.2-42.666667-2.133333-59.733333-2.133333-2.133333 0-2.133333 0-4.266667z" p-id="2916"></path>
            </svg>
            <svg v-if="showingOther" t="1617333301312" class="inline h-3 w-3" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="3051" width="200" height="200"><path d="M482.133333 738.133333L136.533333 392.533333c-17.066667-17.066667-17.066667-42.666667 0-59.733333 8.533333-8.533333 19.2-12.8 29.866667-12.8h689.066667c23.466667 0 42.666667 19.2 42.666666 42.666667 0 10.666667-4.266667 21.333333-12.8 29.866666L541.866667 738.133333c-17.066667 17.066667-42.666667 17.066667-59.733334 0z" p-id="3052"></path>
            </svg>
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
  </transition>

  <material-modal :showModal="showModal" :eventDetail="eventDetail" @close="closeModal" v-bind="$attrs">

  </material-modal>
</template>

<script>
import { ref, toRef, watch } from 'vue'
import MaterialModal from './MaterialModal.vue';

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
  components: {
    MaterialModal,
  },
  emits: [
    'deleteMaterial'
  ],
  setup(props, context) {
    const eventDetail = toRef(props, "eventDetail")
    const detailId = toRef(props, "detailId")
    const showDetail = ref(false)
    const showingPhy = ref(false)
    const showingTemp = ref(false)
    const showingPVT = ref(false)
    const showingP7 = ref(false)
    const showingOther = ref(false)
    const showingAll = ref(false)
    const showModal = ref(false)

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

    const toggleAll = () => {
      showingAll.value = !showingAll.value
    }

    const toggleModal = () => {
      showModal.value = !showModal.value
    }

    const closeModal = () => {
      showModal.value = false
    }

    const deleteMaterial = () => {
      context.emit('deleteMaterial', {
        targetID: eventDetail.value.id
      })
    }

    watch(detailId, () => {
      if (eventDetail.value.id == detailId.value) {
        showDetail.value = true
      }
      else {
        showDetail.value = false
      } 
    })

    watch(showingAll, () => {
      if (showingAll.value == true) {
        showingPhy.value = true
        showingTemp.value = true
        showingPVT.value = true
        showingP7.value = true
        showingOther.value = true
      }
      else {
        showingPhy.value = false
        showingTemp.value = false
        showingPVT.value = false
        showingP7.value = false
        showingOther.value = false
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
      toggleOther,
      showingAll,
      toggleAll,
      showModal,
      toggleModal,
      closeModal,
      deleteMaterial
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
  @apply bg-gray-50 mx-14 my-2 rounded;
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