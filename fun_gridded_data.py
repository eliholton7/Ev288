import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xarray as xr


#Function for making a gridded figure and using dimension reduction to average time.
def gridded_figure(path_data, file_name, spatial_variable, high_dimensional_data):
    '''spatial_variable and high_dimensional_data represent the chosen variables, such as xy coordinates and time,
     and should be entered as a string. '''
    ds = xr.open_dataset(path_data+file_name)
    #print(ds)
    da = ds[spatial_variable]
    #print(da)
    #da.plot(); plt.show()
    dmean = da.mean(high_dimensional_data)
    #print(dmean)
    dmean.plot(); plt.show()