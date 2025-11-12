import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xarray as xr
import fun_CDF_dataarrays as halloween

path_data = '/Users/eliholton/Ev228_data/'
file_name = 'Era5T2M1997-2025.nc'

#trying to use the function but dictionaries just aren't working for some reason. 
in_data, in_data2 = halloween.CDF_data(path_data,file_name,'t2m','valid_time')
# stat = np.std(in_data)
# print(stat)
# d = {
#     'stat': stat,
# }
halloween.des_stats(in_data)
halloween.des_stats(in_data2)

#ds = xr.open_dataset(path_data+file_name)
#print(ds)

# da = ds['t2m']
# #print(da)

# #da.plot(); plt.show()
# dmean = da.mean('valid_time')
# print(dmean)
# dmean.plot(); plt.show()

#plotting the data
def gridded_figure(path_data, file_name, spatial_variable, high_dimensional_data ) 
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