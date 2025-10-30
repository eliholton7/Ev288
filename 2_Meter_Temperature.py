import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xarray as xr

path_data = '/Users/eliholton/Ev228_data/'
ds = xr.open_dataset(path_data+'Era5T2M1997-2025.nc')
print(ds)