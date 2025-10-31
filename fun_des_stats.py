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
    
def des_stats(in_data):
    # data = data['valid_time'].index.to_pydatetime()
    descriptives_dict = {
        'mean_stat': np.mean(in_data),
        'std_stat': in_data.std(),
        # 'var_stat': np.var(in_data), 
        # 'max_stat': np.max(in_data),
        # 'min_stat': np.min(in_data),
    }
    print(descriptives_dict)

