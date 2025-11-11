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

#Functions being used.
def import_era5(file_path='', var=''):
    ''' Import ERA5 gridded data '''
    ds = xr.open_dataset(file_path)
    da = ds[var]

    return da

def map(in_da, out_path='', out_name='',title_name='',des_stats={}):
    ''' Plot map from 2D DataArray '''
    fig = plt.figure()
    ax = fig.add_subplot(111)
    lons = in_da.longitude
    lats = in_da.latitude
    image = plt.pcolormesh(lons, lats, in_da)
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.title(title_name,fontsize=15)
    cb = plt.colorbar(image, shrink=.75, orientation="vertical", pad=.02)
    cb.set_label('Precipitation (mm)')
    plt.annotate(des_stats,(-93.8,24),zorder=1000,fontsize=4.7,color='white')
    plt.savefig(out_path + out_name, dpi=400)

#Creating 4 dataarrays of 20 years of precipitation to see how the plots change in 20 year intervals.
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

#Weighting the latitude and longitude so the descriptive statistics are not thrown off.
weights = np.cos(np.deg2rad(da_vt_mn1['latitude']))
da_wghtd1 = da_vt_mn1.weighted(weights)

weights = np.cos(np.deg2rad(da_vt_mn2['latitude']))
da_wghtd2 = da_vt_mn2.weighted(weights)

weights = np.cos(np.deg2rad(da_vt_mn3['latitude']))
da_wghtd3 = da_vt_mn3.weighted(weights)

weights = np.cos(np.deg2rad(da_vt_mn4['latitude']))
da_wghtd4 = da_vt_mn4.weighted(weights)

#descriptive statistics of each 20 year interval
des_stats1 = {
'Mean_1' : da_wghtd1.mean().data,
'STD_1' : da_wghtd1.std().data,
'Max_1' : graph_1.max().data,
'Min_1' : graph_1.min().data
}

des_stats2 = {
'Mean_2' : da_wghtd2.mean().data,
'STD_2' : da_wghtd2.std().data,
'Max_2' : graph_2.max().data,
'Min_2' : graph_2.min().data
}

des_stats3 = {
'Mean_3' : da_wghtd3.mean().data,
'STD_3' : da_wghtd3.std().data,
'Max_3' : graph_3.max().data,
'Min_3' : graph_3.min().data
}

des_stats4 = {
'Mean_4' : da_wghtd4.mean().data,
'STD_4' : da_wghtd4.std().data,
'Max_4' : graph_4.max().data,
'Min_4' : graph_4.min().data
}

print(des_stats1)
print(des_stats2)
print(des_stats3)
print(des_stats4)

#mapping the 4 different dataarrays.
map(da_vt_mn1, fig_path, fig_name1, 'ERA5 Average Total Precipitation from 1945 to 1965',des_stats=des_stats1)
map(da_vt_mn2, fig_path, fig_name2, 'ERA5 Average Total Precipitation from 1965 to 1985',des_stats=des_stats2)
map(da_vt_mn3, fig_path, fig_name3, 'ERA5 Average Total Precipitation from 1985 to 2005',des_stats=des_stats3)
map(da_vt_mn4, fig_path, fig_name4, 'ERA5 Average Total Precipitation from 2005 to 2025',des_stats=des_stats4)

