import pandas as pd
path_data = '/Users/[eliholton]/Ev228_data/'
file_name = 'KRDU_temp_188708-202508.csv'
df = pd.read_csv(file_name)
print(df)