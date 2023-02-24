#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 22:29:05 2023

@author: hallvard
"""

import requests
import numpy as np
import matplotlib.pyplot as plt


Lower_Troposphere = 'http://vortex.nsstc.uah.edu/data/msu/v6.0/tlt/uahncdc_lt_6.0.txt'
Mid_Troposphere = ' http://vortex.nsstc.uah.edu/data/msu/v6.0/tmt/uahncdc_mt_6.0.txt'
Tropopause = ' http://vortex.nsstc.uah.edu/data/msu/v6.0/ttp/uahncdc_tp_6.0.txt'
Lower_Stratosphere =  'http://vortex.nsstc.uah.edu/data/msu/v6.0/tls/uahncdc_ls_6.0.txt' 
def wrigth_url_to_file(url, name):
    #https://www.geeksforgeeks.org/downloading-files-web-using-python/
    # URL of the image to be downloaded is defined as image_url
    r = requests.get(url) # create HTTP response object
      
    # send a HTTP request to the server and save
    # the HTTP response in a response object called r
    with open(name+".txt",'wb') as f:
      
        # Saving received content as a png file in
        # binary format
      
        # write the contents of the response (r.content)
        # to a new file in binary mode.
        f.write(r.content)
        
        
wrigth_url_to_file(Lower_Troposphere, 'Lower_Troposphere')        
wrigth_url_to_file(Mid_Troposphere,'Mid_Troposphere')
wrigth_url_to_file(Tropopause,'Tropopause')
wrigth_url_to_file(Lower_Stratosphere,'Lower_Stratosphere')
#%%

Lower_Troposphere_arr  = np.loadtxt('Lower_Troposphere' + '.txt', skiprows=15, usecols= 2, max_rows=515)
Mid_Troposphere_arr = np.loadtxt('Mid_Troposphere' + '.txt', skiprows=15, usecols= 2, max_rows=515) 
Tropopause_arr = np.loadtxt('Tropopause' + '.txt', skiprows=15, usecols= 2, max_rows=515)
Lower_Stratosphere_arr = np.loadtxt('Lower_Stratosphere' + '.txt', skiprows=15, usecols= 2, max_rows=515)
year =np.loadtxt('Lower_Troposphere' + '.txt', skiprows=15, usecols= 0, max_rows=515)

window = 12 # 10 month in each year
def moving_average(x, w):
    #https://stackoverflow.com/questions/14313510/how-to-calculate-rolling-moving-average-using-python-numpy-scipy
    return np.convolve(x, np.ones(w), 'same') / w

plt.figure()
plt.title('Global Temp. 1980_2022')
plt.plot(year, Lower_Troposphere_arr , label ='Lower_Troposphere' )
plt.plot(year, Mid_Troposphere_arr , label ='Mid_Troposphere' )
plt.plot(year, Tropopause_arr , label ='Tropopause' )
plt.plot(year, Lower_Stratosphere_arr , label ='Lower_Stratosphere' )
plt.legend()
plt.show()


plt.figure()
plt.title('Global Temp 12 months  Moving Avrage 1980-2022 ')
plt.plot(year, moving_average(Lower_Troposphere_arr,window) , label ='Lower_Troposphere' )
plt.plot(year, moving_average(Mid_Troposphere_arr,window) , label ='Mid_Troposphere' )
plt.plot(year, moving_average(Tropopause_arr,window) , label ='Tropopause' )
plt.plot(year, moving_average(Lower_Stratosphere_arr,window) , label ='Lower_Stratosphere' )
plt.legend()
plt.show()

plt.title('Both_Global_Temp_And_12_months_Moving_Avrage_1980_2022')
plt.plot(year, Lower_Troposphere_arr , label ='Lower_Troposphere' )
plt.plot(year, Mid_Troposphere_arr , label ='Mid_Troposphere' )
plt.plot(year, Tropopause_arr , label ='Tropopause' )
plt.plot(year, Lower_Stratosphere_arr , label ='Lower_Stratosphere' )

plt.plot(year, moving_average(Lower_Troposphere_arr,window) , label ='MA: Lower_Troposphere' )
plt.plot(year, moving_average(Mid_Troposphere_arr,window) , label ='MA: Mid_Troposphere' )
plt.plot(year, moving_average(Tropopause_arr,window) , label ='MA: Tropopause' )
plt.plot(year, moving_average(Lower_Stratosphere_arr,window) , label ='MA: Lower_Stratosphere' )
plt.legend()



