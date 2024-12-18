# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 22:58:22 2024

@author: ander
"""
#Purpose Statement
"""
This script simulates the heat diffusion process in a one-dimensional domain
over a specified period. It models the temperature distribution in the ground, 
considering an intrusive body with a significantly higher temperature at one
end of the domain. The script uses the explicit finite difference method to 
solve the heat equation, ensuring numerical stability through a stability 
criterion. Inputs are the diffusion rate, length of domain, total time, 
and initial temperature. Outputs are the temperature distribution which 
is plotted. The final temperature distribution is plotted to visualize the 
effect of heat diffusion over time. 
"""

import numpy as np
import matplotlib.pyplot as plt

# Initial Parameters
L = 10000  # length of the domain in meters (10 km)
totaltime = 100000  # total time in years
nx = 1000  # number of spatial steps
nt = 1000  # number of time steps
D_ms = 1e-6 # thermal diffusivity in m^2/s
D = D_ms * 60 * 60 * 24 * 365  # convert diffusivity to m^2/year
dt=100 # time step in years
dx = 100 # spatial step in meters
x = np.arange(0, L, dx) # spatial grid points
nodes=len(x) # number of nodes

# Initial temperature distribution
T_initial = 20  # initial temperature of the ground in degrees Celsius
T_intrusive = 1000  # temperature of the intrusive body in degrees Celsius



# Stability criterion  
if D * dt / dx**2 > 0.5:
    raise ValueError("The chosen parameters do not satisfy the stability criterion.")
s=dt*D/dx**2 

# Initialize temperature array
T = np.ones(nodes) * T_initial  

# Position of the intrusive body at one end (0 position)
intrusive_position = 0  #Ensures that diffusion is only plotted in one direction instead of equivalent directions. 

# Set initial condition for the intrusive body
T[intrusive_position] = T_intrusive  # This represents the high temperature of the intrusive body at the start of the simulation.

# Define the supply term S
S = np.zeros(nodes) #Supply term array

# Set up the coefficient matrix A for a 5 node problem
A = np.zeros((nodes, nodes+1)) 
## I chose to use a for loop and indexing to set up the matrix
for i in range(1, nodes-1):
    A[i, i-1] = s   ##Left diagonal
    A[i, i] = 1-2*s   ##a diagonal
    A[i, i+1] = s    ##Right diagonal
A[0, 0] = 1   # boundary condition at left end
A[:,-1]= S   
A[-1,-2] = 1    # boundary condition at right end

# Time-stepping loop
time = 0  #Initial time to set up looop
while time <= totaltime: #3600 * 24 * 365 * 10 :
    T_before = np.hstack((T,1))  # extend temperature array for matrix multiplication
    T_after = np.dot(A, T_before)  # compute new temperature
    T[:] = T_after*1 # update temperature array
    time += dt  # increment time
 
plt.show()

# Plot the final temperature distribution
distance = np.linspace(0, L, nx) # spatial grid for plotting
plt.plot(x, T)  # plot distance vs temperature 
plt.xlabel('Distance (m)')  # x-axis label
plt.ylabel('Temperature (°C)')  # y-axis label
plt.title('Temperature Distribution After Heat Diffusion') # plot title
plt.show() # display plot

print ("T at 2000: %s" % T[x==2000])    #Calculates temperature at any given distance
