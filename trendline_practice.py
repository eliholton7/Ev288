import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt

#path data and outpath data
file_path = '/Users/eliholton/GitHub/Ev228/'
file_name = 'KRDU_temp_188708-202508.csv'
fig_path = '/Users/eliholton/GitHub/Ev228/'
fig_name = 'Trendline.png'

#function for reading the file and naming the variables.
df = pd.read_csv(file_name)
df_yr = df['YEAR']
df_temp = df['metANN']

#trendline function and printing the returns. 
slope, y_int, r_val, p_val, stderr, = stats.linregress(df_yr, df_temp)
print(slope, y_int, r_val, p_val, stderr,)

#plotting the data and adding the trendline.
plt.plot(df_yr, df_temp, color='#dc6b2b', linewidth=2.5)
plt.scatter(df_yr,df_temp)
plt.plot(df_yr, y_int + slope * df_yr)
plt.xlabel('years')
plt.xlim(1887, 2025)
plt.ylabel('annual temperature (deg C)')
plt.title('Raleigh Durham Station 1887-2025')
plt.savefig(fig_path + fig_name, dpi=400)