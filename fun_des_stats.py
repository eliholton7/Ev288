import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xarray as xr
import scipy.stats as stats

#Function for downloading NetCDF files and returning two dataarrays.
def CDF_data(path_data,file_name,spatial_variable,high_dimensional_data):
    ds = xr.open_dataset(path_data+file_name)
    #print(ds)
    da = ds[spatial_variable]
    dx = ds[high_dimensional_data]
    return da, dx
    
