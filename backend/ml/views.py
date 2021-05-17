from django.http import JsonResponse
from django.views import View
from django.core.serializers.json import DjangoJSONEncoder
from django.core.serializers import serialize
import numpy as np
from sklearn.preprocessing import StandardScaler, Normalizer

from core.models import Material
from ml.pca.works import run_kernel_pca
from ml.config import Conf, pcaConf


class PreView(View):
    """Return machine learning params.
    """
    
    def get(self, request):
        return JsonResponse({
            "components": pcaConf.components,
            "batches": pcaConf.batches,
            "results_num": Conf.results_num
        })


class SimAnalysisView(View):
    
    def _extract_data(self) -> np.ndarray:
        """Extract numerical data for data analysis.
        
        The data generated here should be able to be directly used
        in machine learning packages such as sklearn.
        
        Computational data for machine learning:
            type: ndarray.
            format: rows(instancs) x columns(features), 2-D array.
            
        Returns:
            mat_arrays: Material data in ndarray format.
        """
        
        mats = Material.objects.all()
        
        mat_arrays = []
        for mat in mats: # django queryset -> python list
            mat_features = []
            
            # Add data
            # Some data are missing here.
            #TODO: Delete those if sentences after cleaning the data.
            mat_features.append(mat.model_surface_temperature if mat.model_surface_temperature!=None else 0)
            mat_features.append(mat.melt_temperature if mat.melt_temperature!=None else 0)
            mat_features.append(mat.mold_temperature_range_min if mat.mold_temperature_range_min!=None else 0)
            mat_features.append(mat.mold_temperature_range_max if mat.mold_temperature_range_max!=None else 0)
            mat_features.append(mat.melt_temperature_range_min if mat.melt_temperature_range_min!=None else 0)
            mat_features.append(mat.melt_temperature_range_max if mat.melt_temperature_range_max!=None else 0)
            mat_features.append(mat.absolute_maximum_melt_temperature if mat.absolute_maximum_melt_temperature!=None else 0)
            mat_features.append(mat.ejection_temperature if mat.ejection_temperature!=None else 0)
            mat_features.append(mat.maximum_shear_stress if mat.maximum_shear_stress!=None else 0)
            mat_features.append(mat.maximum_shear_rate if mat.maximum_shear_rate!=None else 0)
            mat_features.append(mat.melt_density if mat.melt_density!=None else 0)
            mat_features.append(mat.solid_density if mat.solid_density!=None else 0)
            mat_features.append(mat.pvt_b5 if mat.pvt_b5!=None else 0)
            mat_features.append(mat.pvt_b6 if mat.pvt_b6!=None else 0)
            mat_features.append(mat.pvt_b1m if mat.pvt_b1m!=None else 0)
            mat_features.append(mat.pvt_b2m if mat.pvt_b2m!=None else 0)
            mat_features.append(mat.pvt_b2m if mat.pvt_b2m!=None else 0)
            mat_features.append(mat.pvt_b4m if mat.pvt_b4m!=None else 0)
            mat_features.append(mat.pvt_b1s if mat.pvt_b1s!=None else 0)
            mat_features.append(mat.pvt_b2s if mat.pvt_b2s!=None else 0)
            mat_features.append(mat.pvt_b3s if mat.pvt_b3s!=None else 0)
            mat_features.append(mat.pvt_b4s if mat.pvt_b4s!=None else 0)
            mat_features.append(mat.pvt_b7 if mat.pvt_b7!=None else 0)
            mat_features.append(mat.pvt_b8 if mat.pvt_b8!=None else 0)
            mat_features.append(mat.pvt_b9 if mat.pvt_b9!=None else 0)
            mat_features.append(mat.elastic_modulus_e1 if mat.elastic_modulus_e1!=None else 0)
            mat_features.append(mat.elastic_modulus_e2 if mat.elastic_modulus_e2!=None else 0)
            mat_features.append(mat.poisson_ratio_v12 if mat.poisson_ratio_v12!=None else 0)
            mat_features.append(mat.poisson_ratio_v23 if mat.poisson_ratio_v23!=None else 0)
            mat_features.append(mat.shear_modulus_g12 if mat.shear_modulus_g12!=None else 0.)
            mat_features.append(mat.thermal_expansion_data_transverse_isotropic_coefficient_alpha1 if mat.thermal_expansion_data_transverse_isotropic_coefficient_alpha1!=None else 0.)
            mat_features.append(mat.thermal_expansion_data_transverse_isotropic_coefficient_alpha2 if mat.thermal_expansion_data_transverse_isotropic_coefficient_alpha2!=None else 0.)
            mat_features.append(mat.seven_params_n if mat.seven_params_n!=None else 0.)
            mat_features.append(mat.seven_params_Tau if mat.seven_params_Tau!=None else 0.)
            mat_features.append(mat.seven_params_D1 if mat.seven_params_D1!=None else 0.)
            mat_features.append(mat.seven_params_D2 if mat.seven_params_D2!=None else 0.)
            mat_features.append(mat.seven_params_D3 if mat.seven_params_D3!=None else 0.)
            mat_features.append(mat.seven_params_A1 if mat.seven_params_A1!=None else 0.)
            mat_features.append(mat.seven_params_A2 if mat.seven_params_A2!=None else 0.)
            mat_features.append(mat.c1 if mat.c1!=None else 0.)
            mat_features.append(mat.c2 if mat.c2!=None else 0.)
            mat_features.append(mat.conversion_temperature if mat.conversion_temperature!=None else 0.)
            mat_features.append(mat.MFR_temperature if mat.MFR_temperature!=None else 0.)
            mat_features.append(mat.MFR_loading if mat.MFR_loading!=None else 0.)
            mat_features.append(mat.measured_MFR if mat.measured_MFR!=None else 0.)
            
            mat_arrays.append(mat_features)
            
        # Get numpy arrays.
        mat_arrays = np.array(mat_arrays, dtype=np.float64)
        
        return mat_arrays
    
    def _extract_imp_data(self) -> np.ndarray:
        """Extract PVT and 7-Param data for data analysis.
        
        Only extract the most important features, which are PVT data and
        7-Param data for machine learning algorithm.
        
        Computational data for machine learning:
            type: ndarray.
            format: rows(instances) x columns(features), 2-D array.
            
        Returns:
            mat_arrays: Material data in ndarray format.
        """
        
        mats = Material.objects.all()
        
        mat_arrays = []
        for mat in mats: # django queryset -> python list
            mat_features = []
            
            # Add data
            # Some data are missing here.
            #TODO: Delete those if sentences after cleaning the data.
            mat_features.append(mat.pvt_b5 if mat.pvt_b5!=None else 0)
            mat_features.append(mat.pvt_b6 if mat.pvt_b6!=None else 0)
            mat_features.append(mat.pvt_b1m if mat.pvt_b1m!=None else 0)
            mat_features.append(mat.pvt_b2m if mat.pvt_b2m!=None else 0)
            mat_features.append(mat.pvt_b2m if mat.pvt_b2m!=None else 0)
            mat_features.append(mat.pvt_b4m if mat.pvt_b4m!=None else 0)
            mat_features.append(mat.pvt_b1s if mat.pvt_b1s!=None else 0)
            mat_features.append(mat.pvt_b2s if mat.pvt_b2s!=None else 0)
            mat_features.append(mat.pvt_b3s if mat.pvt_b3s!=None else 0)
            mat_features.append(mat.pvt_b4s if mat.pvt_b4s!=None else 0)
            mat_features.append(mat.pvt_b7 if mat.pvt_b7!=None else 0)
            mat_features.append(mat.pvt_b8 if mat.pvt_b8!=None else 0)
            mat_features.append(mat.pvt_b9 if mat.pvt_b9!=None else 0)
            mat_features.append(mat.seven_params_n if mat.seven_params_n!=None else 0.)
            mat_features.append(mat.seven_params_Tau if mat.seven_params_Tau!=None else 0.)
            mat_features.append(mat.seven_params_D1 if mat.seven_params_D1!=None else 0.)
            mat_features.append(mat.seven_params_D2 if mat.seven_params_D2!=None else 0.)
            mat_features.append(mat.seven_params_D3 if mat.seven_params_D3!=None else 0.)
            mat_features.append(mat.seven_params_A1 if mat.seven_params_A1!=None else 0.)
            mat_features.append(mat.seven_params_A2 if mat.seven_params_A2!=None else 0.)
     
            mat_arrays.append(mat_features)
            
        # Get numpy arrays.
        mat_arrays = np.array(mat_arrays, dtype=np.float64)
        
        return mat_arrays

    def _preprocess(self, data, normalize=False) -> np.ndarray:
        """Preprocess data after extracted for ml.
        
        As the the scale between features are very difference, running
        scaling normalization before put data into machine learning algorithm
        is essential.
        
        Args: 
            data: Extracted data, expected ndarray.
            normalize: Whether to use normalization instead of Standardization.
        """
        
        preprocessor = StandardScaler() if not normalize else Normalizer()

        data = preprocessor.fit_transform(data)
        
        return data
    
    def get(self, request, mat_pk:int, params:str="all", target_results:int=Conf.results_num, components:int=pcaConf.components):
        """Run the data similarity analysis for the project.
        
        After getting a get request, the application run the 
        data similarity analysis and give back the possible results.
        """
        
        # Get data from database and prepocess those data.
        # Preprocess use Standardization or Normalization.
        if params == "all":
            mats_data = self._extract_data().tolist() # ndarray 
        if params == "imp":
            mats_data = self._extract_imp_data().tolist()
        mats_data = self._preprocess(mats_data)
        
        # Calling machine learning algorithms to finish similarity anaylys
        # and returns the final result.
        mats_data_reducted = run_kernel_pca(mats_data, components=components) # ndarray
        mats_data_reducted = mats_data_reducted.tolist()
        
        # Material instance to compare.
        mat_protocol = mats_data_reducted[mat_pk]
        mats_data_to_compare = np.delete(mats_data_reducted, mat_pk, 0)
        
        # Calculate euclidean distance for each instance and get the best.
        results = []
        for mat_idx, mat_data in enumerate(mats_data_to_compare):
            mat_dist = np.sum(np.square(mat_protocol - mat_data))
            mat_dist_tuple = (mat_idx, mat_dist)
            results.append(mat_dist_tuple)
        results.sort(key=lambda x:x[1])
                    
        return JsonResponse({
            "data_results": results[:target_results], # Material data in json format
            "data_returned_num": Conf.results_num, # Returned data numbers.
            "data_total_num": len(mats_data_reducted), # length of materials in analysis
            "data_reducted_dim": len(mats_data_reducted[0]) # Reducted data dimention
        })
    
    # TODO: If frontend can implement this function. There is no need to keep post method.
    def post(self, request, mat_pk, conf):
        """Receive params set by user and change ml setting.
        
        After receiving a post request with params, the application
        will receive those data and change the machine learning algorithm
        settings using them.
        """
        pass