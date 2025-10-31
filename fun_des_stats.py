import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xarray as xr
import scipy.stats as stats

def CDF_data(path_data,file_name,spatial_variable,high_dimensional_data):
    ds = xr.open_dataset(path_data+file_name)
    #print(ds)
    da = ds[spatial_variable]
    dx = ds[high_dimensional_data]
    return da, dx
    
def des_stats(data):
    descriptives_dict = {
        'mean_stat': np.mean(data),
        'std_stat': np.std(data),
        'var_stat': np.var(data), 
        'skewness_stat': stats.skew(data), 
        'kurtosis_stat': stats.kurtosis(data)
    }
    print(descriptives_dict)

