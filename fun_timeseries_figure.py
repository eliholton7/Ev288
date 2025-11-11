import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


file_data = '/Users/eliholton/GitHub/Ev228/'
file_name = 'ASM00094998_temp_194804-202508.csv'
fig_path = '/Users/eliholton/GitHub/Ev228/'
fig_name = 'ASM.png'
var = 'metANN'
time_var = 'YEAR'

#Function for importing GHCN data. Timeseries function is for plotting timeseries data. Combining these two imports 
#and graphs timeseries data, and removes any data point major anomalies and NAN values.
def import_ghcn(file_path='', var=''):
    ''' Import GHCN weather station data '''
    df = pd.read_csv(file_path)
    df_data = df[var]
    df_yr = df['YEAR']

    return df_data, df_yr

#function for plotting timeseries data.
def timeseries(in_df, in_x=None, out_path='', out_name=''):
    ''' Plot timeseries from 1D dataframe '''
    fig = plt.figure()
    ax = fig.add_subplot(111)

    plt.plot(in_x, in_df, color='#dc6b2b', linewidth=2.5)
    plt.xlabel('years')
    plt.xlim(1948, 2025)
    plt.ylabel('annual temperature (deg C)')
    plt.title('Macquarie Island, Australia - Annual Temperature from 1948-2025')
    plt.savefig(out_path + out_name, dpi=400)

#Filtering out anomalies in data.
df_data, df_yr = import_ghcn(file_path=file_data+file_name, var=var)
filter_data = df_data[df_data != 999.9]
filter_year = df_yr[df_data != 999.9]
timeseries(filter_data, in_x=filter_year, out_path=fig_path, out_name=fig_name)


#Descriptive Statistics
mean_var = np.mean(filter_data)
std_var = np.std(filter_data)
max_var = np.max(filter_data)
min_var = np.min(filter_data)
print(mean_var,std_var,max_var,min_var)