"""Run PCA.
"""

import numpy as np
from sklearn.decomposition import KernelPCA, PCA

from ml.config import pcaConf

def run_pca(data: np.ndarray, components=pcaConf.components):
    """Running normal PCA.
    """
    
    mat_PCA = PCA(n_components=components)
    X = mat_PCA.fit_transform(data)
    
    return X
    
def run_kernel_pca(data: np.ndarray, components=pcaConf.components):
    """Running kernel PCA.
    
    Sklearn KernelPCA may fits better for material data, which contain no linear
    features.
    """
    
    mat_kernelPCA = KernelPCA(n_components=components)
    X = mat_kernelPCA.fit_transform(data)
    
    return X
