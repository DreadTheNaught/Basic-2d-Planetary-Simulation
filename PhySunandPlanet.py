G = 6.6743e-11 # Gravitational constant
m_sun = 1.9e30 # Mass of the Sun
m_planet = 5.972e24 # Mass of the planet
AU = 1.5e11 # Distance between planet and the Sun
daysec = 60*60*24 # Seconds in a day
GravConstant = G*m_sun*m_planet # Constant value for calculating force

# Initial distances
xi_sun, yi_sun = 0,0
xi_planet, yi_planet = AU,0

x_sun, y_sun = xi_sun, yi_sun
x_planet, y_planet = xi_planet, yi_planet

# Initial Velocities
vx_sun, vy_sun = 0,0
vx_planet, vy_planet = 0, 30000

# Initializing the time and change in time
t = 0.0
dt = 1*daysec

# Initilaizing the lists that store the positions of the bodies
xlist_sun,ylist_sun = [],[]
xlist_planet,ylist_planet = [],[]

##MAIN LOOP#
while t<3650*daysec:
    ##PLANET##
    
    # Calculating the r vector
    rx_planet = x_planet-x_sun
    ry_planet = y_planet-y_sun
    r_planet_mod = (rx_planet**2 + ry_planet**2)**0.5
    
    # Getting force from the r vector
    Fx_planet = -(GravConstant*rx_planet)/(r_planet_mod**3)
    Fy_planet = -(GravConstant*ry_planet)/(r_planet_mod**3)
    
    # Getting acceleration from force
    ax_planet = Fx_planet/m_planet
    ay_planet = Fy_planet/m_planet
    
    # Calculating change in velocity
    vx_planet += ax_planet*dt
    vy_planet += ay_planet*dt
    
    # Calculating change in position
    x_planet+=vx_planet*dt
    y_planet+=vy_planet*dt
    
    # Appending the updated position values to the lists
    xlist_planet.append(x_planet)
    ylist_planet.append(y_planet)
    
    ##SUN##
    
    # Calculating the r vector
    rx_sun = x_sun-x_planet
    ry_sun = y_sun-y_planet
    r_sun_mod = (rx_sun**2 + ry_sun**2)**0.5
    
    # Getting force from the r vector
    Fx_sun = -(GravConstant*rx_sun)/(r_sun_mod**3)
    Fy_sun = -(GravConstant*ry_sun)/(r_sun_mod**3)
    
    # Getting acceleration from force
    ax_sun = Fx_sun/m_sun
    ay_sun = Fy_sun/m_sun
    
    # Calculating change in velocity
    vx_sun += ax_sun*dt
    vy_sun += ay_sun*dt
    
    # Calculating change in position
    x_sun+=vx_sun*dt
    y_sun+=vy_sun*dt
    
    # Appending the updated position values to the lists
    xlist_sun.append(x_sun)
    ylist_sun.append(y_sun)
    
    #Updating the time by one day
    t+=daysec
    
print("Data Generated")

##PLOTTING##
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


frameSize = 2 #Setting the size of the frame
fig, ax = plt.subplots(figsize=(6,6)) #Defining the figure
ax.set_facecolor("black") #Setting the plot colour
ax.set_aspect("equal") #Making sure the plot and axes are equal
ax.axis("equal")
ax.set_xlim(-frameSize*AU, frameSize*AU) #Setting the Frame sizes
ax.set_ylim(-frameSize*AU, frameSize*AU)

#Defining the points for the sun and planet
point_planet, = ax.plot([xi_planet], [yi_planet], marker="o", markersize=4, markeredgecolor="blue", markerfacecolor="blue")
point_sun, = ax.plot([xi_sun], [yi_sun], marker="o", markersize=7, markeredgecolor="yellow", markerfacecolor="yellow")
line_planet, = ax.plot([], [], '-g', lw=1, c='blue')
planet_data_x, planet_data_y = [], []

def update(i):
    #Appending the data into a new list for the orbit line
    planet_data_x.append(xlist_planet[i])
    planet_data_y.append(ylist_planet[i])
    
    #Updating the data for the animation
    point_planet.set_data(xlist_planet[i], ylist_planet[i])
    point_sun.set_data(xlist_sun[i], ylist_sun[i])
    line_planet.set_data(planet_data_x, planet_data_y)
    
    return point_planet, point_sun, line_planet

#Animating the data
anim = animation.FuncAnimation(fig, func= update, frames= len(xlist_planet), interval = 1, blit = True)

#Displaying the plot
plt.show()