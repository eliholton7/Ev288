import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xarray as xr
import fun_des_stats as fds

path_data = '/Users/eliholton/Ev228_data/'
file_name = 'Era5T2M1997-2025.nc'

in_data, in_data2 = fds.CDF_data(path_data,file_name,'t2m','valid_time')
fds.des_stats(in_data)
fds.des_stats(in_data2)

#ds = xr.open_dataset(path_data+file_name)
#print(ds)

# da = ds['t2m']
# #print(da)

# #da.plot(); plt.show()
# dmean = da.mean('valid_time')
# print(dmean)
# dmean.plot(); plt.show()

# def gridded_figure(path_data, file_name, spatial_variable, high_dimensional_data ) 
#     '''spatial_variable and high_dimensional_data represent the chosen variables, such as xy coordinates and time,
#      and should be entered as a string. '''
#     ds = xr.open_dataset(path_data+file_name)
#     #print(ds)
#     da = ds[spatial_variable]
#     #print(da)
#     #da.plot(); plt.show()
#     dmean = da.mean(high_dimensional_data)
#     #print(dmean)
#     dmean.plot(); plt.show()