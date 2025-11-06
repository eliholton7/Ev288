import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import fun_GHCN_data as GHCN

#testing the GHCN import function.
GHCN.import_data('/Users/eliholton/GitHub/Ev228/Practical4_Data/','USW00093009_temp_190801-202508.csv',2,3)