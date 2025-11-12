# Ev288
Individual

My Independent Research Project is the summation of all of the scripts written in this repository. My project focuses on the total precipitation amount in the southern United States from 1945 to 2025. In order to examine the Era-5 Data I used, I wrote the IRP.py script, which uses two primary functions: One to import the data and return the data-array being worked with (in this case "tp" for total precipitation), and the other to map the data into a figure with an annotation of the descriptive statistics describing the data. Since the data spans 80 years and is gridded data, I decided to split the data into 4 20-year intervals and graph each interval, as represented by the SPD(years).png files in the repository. The rest of the code involves weighting the latitute and longitude correctly so that the descriptive statistics that I decided to annotate onto each graph were correct, and the dictionaries actually containing the descriptive statistics code. Each other file in this repository either led me to work with the functions used in the IRP script, or helped me practice writing code for both timeseries and gridded data and their figures. 

All that is needed to create the graphs is to run the IRP.py script. If using different data, along with the standard file data, path data and outpath data variables, you would need to select your variable for the import_era5 function, and for the map function: the data-array after dimension reduction variable, title name, and dictionary of descriptive statistics to appear on your graph. 


Code Index:
- 2_Meter_Temperature.py: This script was written for an in class excercise, but failed to work for some reason, potentially because of an invisible character of some sort? Several data structures simply wouldn't work and there was no obvious reason as to why. 
- fun_CDF_dataarrays.py: This script contains a function to import NetCDF data and return two data arrays, gerenally meant for coordinates and time.
- fun_GHCN_data.py: This function imports GHCN data and depoending on the variable selected, prints out a data-point from the column and row desired. 
- fun_gridded_data.py: This function creates a very simple gridded data figure, and was originally used in my Independant Research Project until I decided I needed a more complex function.
- fun_map_figure.py: This script was written for the practical 6 assignment, and contains the "map" and "import_era5" functions, which imports era-5 data and makes a slightly more complex gridded figure
- fun_timeseries_figure.py: This script was for the first part of practical 6, and contains two functions to import GHCN data and make a timeseries function, as well as some extra code to take out anomalies in the data and run descriptive statistics.
- hello_world.py: Test to see that the GitHub was working.
- IRP.py: Independent Research Project, see above.
- trendline_practice.py: This script was written to code a trendline onto a timeseries graph.
- wrap_import_data.py: This was created just to test the fun_GHCN_data script containing the import_data function. 

Everything else in this repository is either data or graphs for the various scripts. The most important graphs/images are the 5 SPD.png graphs pertaining to my independant reserach project, as described above. 

No generative AI was used on this assignment.
