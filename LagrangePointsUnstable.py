import numpy as np

G = 6.6743e-11 # Gravitational constant
m_sun = 1.9e30 # Mass of the Sun
m_planet = 5.972e24 # Mass of the planet
m_sat = 1000
AU = 1.5e11 # Distance between Earth and the Sun
daysec = 60*60*24 # Seconds in a day


# Initial distances
xi_sun, yi_sun = 0,0
xi_planet, yi_planet = AU,0
xi_L1, yi_L1 = 0.99 * AU, 0

x_sun, y_sun = xi_sun, yi_sun
x_planet, y_planet = xi_planet, yi_planet
x_L1, y_L1 = xi_L1, yi_L1

# Initial Velocities

vx_sun, vy_sun = 0,0
vx_planet, vy_planet = 0, 30000
vx_L1, vy_L1 = 0, 30000

# Initializing the time and change in time
t = 0.0
dt = 1*daysec

# Initilaizing the lists that store the positions of the bodies
xlist_sun,ylist_sun = [],[]
xlist_planet,ylist_planet = [],[]
xlist_L4, ylist_L4 = [],[]
xlist_L1, ylist_L1 = [],[]

##MAIN LOOP#
while t<3650*daysec:
    ##PLANET##
    
    rx_planet = x_planet-x_sun
    ry_planet = y_planet-y_sun
    r_planet_mod = (rx_planet**2 + ry_planet**2)**0.5
    
    Fx_planet = -(G*m_sun*m_planet*rx_planet)/(r_planet_mod**3)
    Fy_planet = -(G*m_sun*m_planet*ry_planet)/(r_planet_mod**3)
    
    ax_planet = Fx_planet/m_planet
    ay_planet = Fy_planet/m_planet
    
    vx_planet += ax_planet*dt
    vy_planet += ay_planet*dt
    
    x_planet+=vx_planet*dt
    y_planet+=vy_planet*dt
    
    xlist_planet.append(x_planet)
    ylist_planet.append(y_planet)
    
    ##SUN##
    
    rx_sun = x_sun-x_planet
    ry_sun = y_sun-y_planet
    r_sun_mod = (rx_sun**2 + ry_sun**2)**0.5
    
    Fx_sun = -(G*m_sun*m_planet*rx_sun)/(r_sun_mod**3)
    Fy_sun = -(G*m_sun*m_planet*ry_sun)/(r_sun_mod**3)
    
    ax_sun = Fx_sun/m_sun
    ay_sun = Fy_sun/m_sun
    
    vx_sun += ax_sun*dt
    vy_sun += ay_sun*dt
    
    x_sun+=vx_sun*dt
    y_sun+=vy_sun*dt
    
    xlist_sun.append(x_sun)
    ylist_sun.append(y_sun)

    ## SATELITE L1 ##
    
    rx_L1_sun = x_L1-x_sun
    ry_L1_sun = y_L1-y_sun
    rx_L1_planet = x_L1 - x_planet
    ry_L1_planet = y_L1 - y_planet

    r_L1_sun_mod = (rx_L1_sun**2 + ry_L1_sun**2)**0.5
    r_L1_planet_mod = (rx_L1_planet**2 + ry_L1_planet**2)**0.5

    Fx_L1_sun = -(G*m_sat*m_sun*rx_L1_sun)/(r_L1_sun_mod**3)
    Fy_L1_sun = -(G*m_sat*m_sun*ry_L1_sun)/(r_L1_sun_mod**3)

    Fx_L1_planet = -(G*m_sat*m_planet*rx_L1_planet)/(r_L1_planet_mod**3)
    Fy_L1_planet = -(G*m_sat*m_planet*ry_L1_planet)/(r_L1_planet_mod**3)

    Fx_L1_net = Fx_L1_sun + Fx_L1_planet
    Fy_L1_net = Fy_L1_sun + Fy_L1_planet

    ax_L1 = Fx_L1_net/m_sat
    ay_L1 = Fy_L1_net/m_sat

    vx_L1 += ax_L1*dt
    vy_L1 += ay_L1*dt

    x_L1 += vx_L1*dt
    y_L1 += vy_L1*dt

    xlist_L1.append(x_L1)
    ylist_L1.append(y_L1)
    
    t+=daysec
    
print("Data Generated")

##PLOTTING##

import matplotlib.pyplot as plt
import matplotlib.animation as animation


frameSize = 2
fig, ax = plt.subplots(figsize=(6,6))
ax.set_facecolor("black")
ax.set_aspect("equal")
ax.axis("equal")
ax.set_xlim(-frameSize*AU, frameSize*AU)
ax.set_ylim(-frameSize*AU, frameSize*AU)

point_planet, = ax.plot([xi_planet], [yi_planet], marker="o", markersize=4, markeredgecolor="blue", markerfacecolor="blue")
point_sun, = ax.plot([xi_sun], [yi_sun], marker="o", markersize=7, markeredgecolor="yellow", markerfacecolor="yellow")
point_L1, = ax.plot([xi_L1], [yi_L1], marker="o", markersize=3,markeredgecolor="white", markerfacecolor="white")


def update(i):
     
    point_planet.set_data(xlist_planet[i], ylist_planet[i])
    point_sun.set_data(x_sun, y_sun)
    point_L1.set_data(xlist_L1[i], ylist_L1[i])
    
    return point_planet, point_sun, point_L1

anim = animation.FuncAnimation(fig, func= update, frames= len(xlist_planet), interval = 1, blit = True)

plt.show()