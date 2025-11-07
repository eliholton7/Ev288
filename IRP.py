import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xarray as xr
import sys 

#path data and outpath data for figure--can probably copy code gridded data function.
file_data = '/Users/eliholton/GitHub/Ev228/'
file_name = 'Southern_Precipitation_Data.nc'
fig_path = '/Users/eliholton/GitHub/Ev228/'
fig_name1 = 'SPD1945-1965.png'
fig_name2 = 'SPD1965-1985.png'
fig_name3 = 'SPD1985-2005.png'
fig_name4 = 'SPD2005-2025.png'

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
graph_1_data = np.arange(59,300)
graph_2_data = np.arange(300,540)
graph_3_data = np.arange(540,780)
graph_4_data = np.arange(780,1029)

graph_1 = da_tp.isel(valid_time = graph_1_data)
graph_2 = da_tp.isel(valid_time = graph_2_data)
graph_3 = da_tp.isel(valid_time = graph_3_data)
graph_4 = da_tp.isel(valid_time = graph_4_data)

da_vt_mn1 = graph_1.mean(dim = 'valid_time')
da_vt_mn2 = graph_2.mean(dim = 'valid_time')
da_vt_mn3 = graph_3.mean(dim = 'valid_time')
da_vt_mn4 = graph_4.mean(dim = 'valid_time')

map(da_vt_mn1, fig_path, fig_name1)
map(da_vt_mn2, fig_path, fig_name2)
map(da_vt_mn3, fig_path, fig_name3)
map(da_vt_mn4, fig_path, fig_name4)


#plot the graph, can likely use code from the fun_gridded_data function, 
# which also reads the cdf file so maybe fun_des_stats is not needed.

#fousing on the statistics of the data, or focusing on a trend. End year - start year divided by # of years.

