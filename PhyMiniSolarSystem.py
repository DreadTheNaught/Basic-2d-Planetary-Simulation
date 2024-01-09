import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

G = 6.6743e-11
m_sun = 1.9e30
m_earth = 5.972e24
m_mars = 6.39e23
m_asteroid = 2.3e21
AU = 1.5e11
daysec = 60*60*24
GravConstantEarth = G*m_sun*m_earth
GravConstantMars = G*m_sun*m_mars
GravConstantAsteroid = G*m_sun*m_asteroid

xi_sun, yi_sun = 0,0
xi_earth, yi_earth = AU,0
xi_mars, yi_mars = 1.666*AU,0
xi_asteroid, yi_asteroid = 3*AU,0.3*AU

x_sun, y_sun = xi_sun, yi_sun
x_earth, y_earth = xi_earth, yi_earth
x_mars, y_mars = xi_mars, yi_mars
x_asteroid, y_asteroid = xi_asteroid, yi_asteroid

vx_sun, vy_sun = 0,0
vx_earth, vy_earth = 0, 30000
vx_mars, vy_mars = 0, 22500
vx_asteroid, vy_asteroid = 0,7000

t = 0.0
dt = 1*daysec

xlist_sun, ylist_sun = [],[]
xlist_earth, ylist_earth = [],[]
xlist_mars, ylist_mars = [],[]
xlist_asteroid, ylist_asteroid = [],[]

while t<3650*daysec:
    ##EARTH##
    
    rx_earth = x_earth-x_sun
    ry_earth = y_earth-y_sun
    r_earth_mod = (rx_earth**2 + ry_earth**2)**0.5
    
    Fx_earth = -(GravConstantEarth*rx_earth)/(r_earth_mod**3)
    Fy_earth = -(GravConstantEarth*ry_earth)/(r_earth_mod**3)
    
    ax_earth = Fx_earth/m_earth
    ay_earth = Fy_earth/m_earth
    
    vx_earth += ax_earth*dt
    vy_earth += ay_earth*dt
    
    x_earth+=vx_earth*dt
    y_earth+=vy_earth*dt
    
    xlist_earth.append(x_earth)
    ylist_earth.append(y_earth)
    
    ##MARS##
    
    rx_mars = x_mars-x_sun
    ry_mars = y_mars-y_sun
    r_mars_mod = (rx_mars**2 + ry_mars**2)**0.5
    
    Fx_mars = -(GravConstantMars*rx_mars)/(r_mars_mod**3)
    Fy_mars = -(GravConstantMars*ry_mars)/(r_mars_mod**3)
    
    ax_mars = Fx_mars/m_mars
    ay_mars = Fy_mars/m_mars
    
    vx_mars += ax_mars*dt
    vy_mars += ay_mars*dt
    
    x_mars+=vx_mars*dt
    y_mars+=vy_mars*dt
    
    xlist_mars.append(x_mars)
    ylist_mars.append(y_mars)
    
    ##ASTEROID#
    
    rx_asteroid = x_asteroid-x_sun
    ry_asteroid = y_asteroid-y_sun
    r_asteroid_mod = (rx_asteroid**2 + ry_asteroid**2)**0.5
    
    Fx_asteroid = -(GravConstantAsteroid*rx_asteroid)/(r_asteroid_mod**3)
    Fy_asteroid = -(GravConstantAsteroid*ry_asteroid)/(r_asteroid_mod**3)
    
    ax_asteroid = Fx_asteroid/m_asteroid
    ay_asteroid = Fy_asteroid/m_asteroid
    
    vx_asteroid += ax_asteroid*dt
    vy_asteroid += ay_asteroid*dt
    
    x_asteroid+=vx_asteroid*dt
    y_asteroid+=vy_asteroid*dt
    
    xlist_asteroid.append(x_asteroid)
    ylist_asteroid.append(y_asteroid)
    
    t+=daysec
    
print("Data Generated")

##PLOTTING##
frameSize = 4
fig, ax = plt.subplots(figsize=(6,6))
ax.set_facecolor("black")
ax.set_aspect("equal")
ax.axis("equal")
ax.set_xlim(-frameSize*AU, frameSize*AU)
ax.set_ylim(-frameSize*AU, frameSize*AU)

point_earth, = ax.plot([xi_earth], [yi_earth], marker="o", markersize=4, markeredgecolor="blue", markerfacecolor="blue")
point_sun, = ax.plot([xi_sun], [yi_sun], marker="o", markersize=7, markeredgecolor="yellow", markerfacecolor="yellow")
point_mars, = ax.plot([xi_mars], [yi_mars], marker="o", markersize=4, markeredgecolor="red", markerfacecolor="red")
point_asteroid, = ax.plot([xi_asteroid], [yi_asteroid], marker="o", markersize=3, markeredgecolor="white", markerfacecolor="white")
line_earth, = ax.plot([],[],'-g',lw=1,c='blue')
line_mars, = ax.plot([],[],'-g',lw=1,c='red')
line_asteroid, = ax.plot([],[],'-g',lw=1,c='white')

earth_data_x, earth_data_y = [],[]
mars_data_x, mars_data_y = [],[]
asteroid_data_x, asteroid_data_y = [],[]

def update(i):
    
    earth_data_x.append(xlist_earth[i])
    earth_data_y.append(ylist_earth[i])
    mars_data_x.append(xlist_mars[i])
    mars_data_y.append(ylist_mars[i])
    asteroid_data_x.append(xlist_asteroid[i])
    asteroid_data_y.append(ylist_asteroid[i])
    
    point_earth.set_data(xlist_earth[i], ylist_earth[i])
    point_sun.set_data(xi_sun, yi_sun)
    point_mars.set_data(xlist_mars[i],ylist_mars[i])
    point_asteroid.set_data(xlist_asteroid[i],ylist_asteroid[i])
    line_earth.set_data(earth_data_x, earth_data_y)
    line_mars.set_data(mars_data_x, mars_data_y)
    line_asteroid.set_data(asteroid_data_x, asteroid_data_y)
    
    return line_earth, line_mars, line_asteroid, point_earth, point_sun, point_mars, point_asteroid

anim = animation.FuncAnimation(fig, func= update, frames= len(xlist_earth), interval = 1, blit = True)

plt.show()