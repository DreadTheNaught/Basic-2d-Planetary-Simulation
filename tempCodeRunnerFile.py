import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Defining initial values

G = 6.6743e-11 
m_planet1 = 5.972e28
m_planet2 = 5.972e28
m_planet3 = 5.972e28
AU = 1.5e11
daysec = 60*60*24

xi_planet1, yi_planet1 = 0,0
xi_planet2, yi_planet2 = AU,0
xi_planet3, yi_planet3 = 0,AU

x_planet1, y_planet1 = xi_planet1, yi_planet1
x_planet2, y_planet2 = xi_planet2, yi_planet2
x_planet3, y_planet3 = xi_planet3, yi_planet3

vx_planet1, vy_planet1 = -2000, 1000
vx_planet2, vy_planet2 = 1000, 1000