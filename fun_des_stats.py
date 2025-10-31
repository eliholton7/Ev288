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
    
def des_stats(da,dx):
    data = (da,dx)
    descriptives = dict{data.mean, np.std(data), np.var(data), stats.skewness(data), stats.kurtosis(data)}
    print(descriptives)

