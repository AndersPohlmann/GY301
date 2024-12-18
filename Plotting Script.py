# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 10:57:09 2024

@author: ander
"""
 
import numpy as np
import matplotlib.pyplot as plt

# Initial Conditions
L = 5000  # length of the domain in meters (10 km)
dx = 1000
x = np.arange(0, L + dx, dx)

# Assign the filename: file
file_cores = 'Garnet Cores.txt'
# Load the data: data
data_cores = np.genfromtxt(file_cores)
print(data_cores) #ensure dataset has been properly loaded

# Assign the filename: file
file_rims = 'Garnet Rims.txt'
# Load the data: data
data_rims = np.genfromtxt(file_rims)
print(data_rims) #ensure dataset has been properly loaded

# d18O values for different distances
d18Ocalc1km = np.array([-7.968085163, -6.656253902, -5.345183369, -4.034872902, -2.72532184, -1.416529523, -0.108495292, 1.198781512, 2.505301546, 3.811065466, 5.116073931])
d18Ocalc2km = np.array([-7.968085163, -6.655923666, -5.344522216, -4.033880154, -2.723996819, -1.414871553, -0.106503698, 1.201107403, 2.507962406, 3.814061967, 5.119406741])
d18Ocalc3km = np.array([-7.968085163, -6.486000728, -5.004268065, -3.522887046, -2.041857549, -0.561179446, 0.919147386, 2.399123072, 3.878747739, 5.358021509, 6.836944509])
d18Ocalc4km = np.array([-7.968085163, -6.071487335, -4.173756971, -2.274893055, -0.374894572, 1.526239496, 3.428510167, 5.331918461, 7.236465398, 9.142152, 11.04897929])
d18Ocalc5km = np.array([-7.968085163, -5.553285511, -3.134522317, -0.711785813, 1.714933798, 4.145646348, 6.5803617, 9.019089749, 11.46184042, 13.90862369, 16.35944953])

# Plotting
fig, ax1 = plt.subplots(1, 1)
ax1.plot([1000]*len(d18Ocalc1km), d18Ocalc1km, 'o', label='1 km')
ax1.plot([2000]*len(d18Ocalc2km), d18Ocalc2km, 'o', label='2 km')
ax1.plot([3000]*len(d18Ocalc3km), d18Ocalc3km, 'o', label='3 km')
ax1.plot([4000]*len(d18Ocalc4km), d18Ocalc4km, 'o', label='4 km')
ax1.plot([5000]*len(d18Ocalc5km), d18Ocalc5km, 'o', label='5 km')

ax1.axhspan(min(data_rims), max(data_rims), color='red', alpha=0.3, label='Rim Range')
ax1.axhspan(min(data_cores), max(data_cores), color='blue', alpha=0.3, label='Core Range')

 
plt.ylim(-8, 17)
plt.ylabel('d18O')
plt.xlabel('distance (m)')
plt.title('d18O values vs Distance')
plt.legend(loc='upper left')
plt.grid(True)
plt.show()

