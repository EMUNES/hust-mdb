"""Machine learning configurations.

Storage for machine learning configurations, including params, methods and more.
"""

class pcaConf(object):
    """Configurations for PCA/kernelPCA.
    
    Properties:
        components: The dimention reducted to.
        batch_size: Batches of data for IncrementalPCA to handle altogether.
    """
    
    components = 8 
    
    batches = 16
    

class Conf(object):
    """Configurations for general algorithms.

    Properties:
        results_num: The number of results to return.
    """
    
    results_num = 10