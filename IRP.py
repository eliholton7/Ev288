import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xarray as xr
import fun_gridded_data as fgd
import sys 

#path data and outpath data for figure--can probably copy code gridded data function.
file_data = '/Users/eliholton/GitHub/Ev228/'
file_name = 'Southern_Precipitation_Data.nc'
fig_path = '/Users/eliholton/GitHub/Ev228/'
fig_name = 'SPD.png'

#import function to read .nc data. Can copy code from fun_des_stats function to read a cdf file. 
#fgd.gridded_figure(path_data=file_data, file_name=file_name, spatial_variable='longitude' + 'latitude', high_dimensional_data='Year')


def import_era5(file_path='', var=''):
    ''' Import ERA5 gridded data '''
    ds = xr.open_dataset(file_path)
    da = ds[var]

    return da

def map(in_da, out_path='', out_name=''):
    ''' Plot map from 2D DataArray '''
    fig = plt.figure()
    ax = fig.add_subplot(111)
    lons = in_da.longitude
    lats = in_da.latitude

    image = plt.pcolormesh(lons, lats, in_da)
    plt.xlabel('longitude')
    plt.ylabel('latitude')
    plt.title('ERA5 Average Total Precipitation from 1940 to 2025')
    cb = plt.colorbar(image, shrink=.75, orientation="vertical", pad=.02)
    cb.set_label('precipitation (mm)')
    plt.savefig(out_path + out_name, dpi=400)

da_tp = import_era5(file_path=file_data+file_name, var='tp')
da_tp_timemn = da_tp.mean(dim='valid_time')

map(da_tp_timemn, fig_path, fig_name)
#set the variables that im interested in. 

#plot the graph, can likely use code from the fun_gridded_data function, 
# which also reads the cdf file so maybe fun_des_stats is not needed.

#fousing on the statistics of the data, or focusing on a trend. End year - start year divided by # of years.

