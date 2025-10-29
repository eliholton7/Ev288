import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def import_data(path_data,file_name,column,row):
    df = pd.read_csv(path_data+file_name)
    print(df)
    #selected_column = df[column]
    #selected_data_point = selected_column[row] 
    #print(selected_column)
    #print(selected_data_point)
    data_point = df.iloc[row,column]
    print(data_point)
