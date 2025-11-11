import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xarray as xr

#Function for importing era5 data and returning a dataarray.
def import_era5(file_path='', var=''):
    ''' Import ERA5 gridded data '''
    ds = xr.open_dataset(file_path)
    da = ds[var]

    return da

#function for mapping gridded data.
def map(in_da, out_path='', out_name=''):
    ''' Plot map from 2D DataArray '''
    fig = plt.figure()
    ax = fig.add_subplot(111)
    lons = in_da.longitude
    lats = in_da.latitude

    image = plt.pcolormesh(lons, lats, in_da)
    plt.xlabel('longitude')
    plt.ylabel('latitude')
    plt.title('ERA5 Wind Speed 1980-1989')
    cb = plt.colorbar(image, shrink=.75, orientation="vertical", pad=.02)
    cb.set_label('meters per second')
    plt.savefig(out_path + out_name, dpi=400)

file_data = '/Users/eliholton/GitHub/Ev228/'
file_name = 'era5_10mwind_1980-1989.nc'
fig_path = '/Users/eliholton/GitHub/Ev228/'
fig_name = 'era5.png'

da_si10 = import_era5(file_path=file_data+file_name, var='si10')
da_si10_timemn = da_si10.mean(dim='valid_time')

map(da_si10_timemn, fig_path, fig_name)

# mean_var = da_si10.mean()
# std_var = da_si10.std()
# max_var = da_si10.max()
# min_var = da_si10.min()
# print(mean_var,std_var,max_var,min_var)