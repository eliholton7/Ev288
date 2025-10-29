import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

path_data = '/Users/eliholton/GitHub/Ev228/'
file_name = 'KRDU_temp_188708-202508.csv'
df = pd.read_csv(path_data+file_name)

#print(df)

unknown_variable = df['M-A-M'][0:] 
print(unknown_variable)
# unknown_variable is a monthly average of temperatures from March-April-May
