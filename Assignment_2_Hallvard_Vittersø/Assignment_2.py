#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 15:09:55 2023

@author: hallvard
"""


#From: 
####################################################
#https://www.geeksforgeeks.org/scrape-tables-from-any-website-using-python/
###################################################

# Library for opening url and creating
# requests
import urllib.request
 
# pretty-print python data structures
from pprint import pprint
 
# for parsing all the tables present
# on the website
from html_table_parser.parser import HTMLTableParser
 
# for converting the parsed data in a
# pandas dataframe
import pandas as pd
 
 
# Opens a website and read its
# binary contents (HTTP Response Body)
def url_get_contents(url):
 
    # Opens a website and read its
    # binary contents (HTTP Response Body)
 
    #making request to the website
    req = urllib.request.Request(url=url)
    f = urllib.request.urlopen(req)
 
    #reading contents of the website
    return f.read()
 
# defining the html contents of a URL.
xhtml = url_get_contents('https://www.motor.no/aktuelt/motors-store-vintertest-av-rekkevidde-pa-elbiler/217132').decode('utf-8')
 
# Defining the HTMLTableParser object
p = HTMLTableParser()
 
# feeding the html contents in the
# HTMLTableParser object
p.feed(xhtml)
 
# Now finally obtaining the data of
# the table required
pprint(p.tables[1])

# converting the parsed data to
# dataframe
print("\n\nPANDAS DATAFRAME\n")
print(pd.DataFrame(p.tables[1]))
#########################################################################
#############################################

#%%
import numpy as np
import matplotlib.pyplot as plt

tabel0 = pd.DataFrame(p.tables[0])

tabel1 = pd.DataFrame(p.tables[1])


wtp = tabel0[1]
wtp = [ wtp.split()[0] for wtp in wtp[1:]  ]
wtp.pop(25)
wtp.pop(18)
wtp = np.array(wtp, dtype = float)








stop =  tabel0[2]
stop = [ st.split()[0] for st in stop[1:]  ]
stop.pop(25)
stop.pop(18)
stop = np.array(stop, dtype = float)




from scipy import stats
#https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.linregress.html

res = stats.linregress(wtp, stop)

x = np.arange(200,600)
y = np.arange(200,600)

plt.plot(wtp, stop, 'o', label='original data')
plt.plot(x,y,'g', label='45')
plt.plot(wtp, res.intercept + res.slope*wtp, 'r', label='fitted line')

plt.legend()

plt.show()

print(res.slope)
# 0.86712
# the slope is not 1 but allomst. 














