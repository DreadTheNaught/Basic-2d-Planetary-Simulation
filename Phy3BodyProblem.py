import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Defining initial values

G = 6.6743e-11 
m_planet1 = (5.972e27)*5
m_planet2 = 5.972e24
m_planet3 = 5.972e24
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
vx_planet3, vy_planet3 = -2500, 5000


t = 0.0
dt = 10000*5

xlist_planet1, ylist_planet1 = [],[]
xlist_planet2 ,ylist_planet2 = [],[]
xlist_planet3 ,ylist_planet3 = [],[]

while t<3650*daysec :
    ##PLANET1##
    
    rx_planet12 = x_planet1-x_planet2
    ry_planet12 = y_planet1-y_planet2
    rx_planet13 = x_planet1-x_planet3
    ry_planet13 = y_planet1-y_planet3
    r_planet_mod12 = (rx_planet12**2 + ry_planet12**2)**0.5
    r_planet_mod13 = (rx_planet13**2 + ry_planet13**2)**0.5
    
    Fx_planet12 = -(G*m_planet1*m_planet2*rx_planet12)/(r_planet_mod12**3)
    Fy_planet12 = -(G*m_planet1*m_planet2*ry_planet12)/(r_planet_mod12**3)
    Fx_planet13 = -(G*m_planet1*m_planet3*rx_planet13)/(r_planet_mod13**3)
    Fy_planet13 = -(G*m_planet1*m_planet3*ry_planet13)/(r_planet_mod13**3)
    Fx_planet1 = Fx_planet12 + Fx_planet13
    Fy_planet1 = Fy_planet12 + Fy_planet13
    
    ax_planet1 = Fx_planet1/m_planet1
    ay_planet1 = Fy_planet1/m_planet1
    
    vx_planet1 += ax_planet1*dt
    vy_planet1 += ay_planet1*dt
    
    x_planet1+=vx_planet1*dt
    y_planet1+=vy_planet1*dt
    
    xlist_planet1.append(x_planet1)
    ylist_planet1.append(y_planet1)
    
    ##PLANET2##
    
    rx_planet21 = x_planet2-x_planet1
    ry_planet21 = y_planet2-y_planet1
    rx_planet23 = x_planet2-x_planet3
    ry_planet23 = y_planet2-y_planet3
    r_planet_mod21 = (rx_planet21**2 + ry_planet21**2)**0.5
    r_planet_mod23 = (rx_planet23**2 + ry_planet23**2)**0.5
    
    Fx_planet21 = -(G*m_planet2*m_planet1*rx_planet21)/(r_planet_mod21**3)
    Fy_planet21 = -(G*m_planet2*m_planet1*ry_planet21)/(r_planet_mod21**3)
    Fx_planet23 = -(G*m_planet2*m_planet3*rx_planet23)/(r_planet_mod23**3)
    Fy_planet23 = -(G*m_planet2*m_planet3*ry_planet23)/(r_planet_mod23**3)
    Fx_planet2 = Fx_planet21 + Fx_planet23
    Fy_planet2 = Fy_planet21 + Fy_planet23
    
    ax_planet2 = Fx_planet2/m_planet2
    ay_planet2 = Fy_planet2/m_planet2
    
    vx_planet2 += ax_planet2*dt
    vy_planet2 += ay_planet2*dt
    
    x_planet2+=vx_planet2*dt
    y_planet2+=vy_planet2*dt
    
    xlist_planet2.append(x_planet2)
    ylist_planet2.append(y_planet2)
    
    ##PLANET3##
    
    rx_planet31 = x_planet3-x_planet1
    ry_planet31 = y_planet3-y_planet1
    rx_planet32 = x_planet3-x_planet2
    ry_planet32 = y_planet3-y_planet2
    r_planet_mod31 = (rx_planet31**2 + ry_planet31**2)**0.5
    r_planet_mod32 = (rx_planet32**2 + ry_planet32**2)**0.5
    
    Fx_planet31 = -(G*m_planet3*m_planet1*rx_planet31)/(r_planet_mod31**3)
    Fy_planet31 = -(G*m_planet3*m_planet1*ry_planet31)/(r_planet_mod31**3)
    Fx_planet32 = -(G*m_planet3*m_planet2*rx_planet32)/(r_planet_mod32**3)
    Fy_planet32 = -(G*m_planet3*m_planet2*ry_planet32)/(r_planet_mod32**3)
    Fx_planet3 = Fx_planet31 + Fx_planet32
    Fy_planet3 = Fy_planet31 + Fy_planet32
    
    ax_planet3 = Fx_planet3/m_planet3
    ay_planet3 = Fy_planet3/m_planet3
    
    vx_planet3 += ax_planet3*dt
    vy_planet3 += ay_planet3*dt
    
    x_planet3+=vx_planet3*dt
    y_planet3+=vy_planet3*dt
    
    xlist_planet3.append(x_planet3)
    ylist_planet3.append(y_planet3)
    
   
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

point_planet1, = ax.plot([xi_planet1], [yi_planet1], marker="o", markersize=4, markeredgecolor="blue", markerfacecolor="blue")
point_planet2, = ax.plot([xi_planet2], [yi_planet2], marker="o", markersize=4, markeredgecolor="red", markerfacecolor="red")
point_planet3, = ax.plot([xi_planet3], [yi_planet3], marker="o", markersize=4, markeredgecolor="green", markerfacecolor="green")


def update(i):
    
    point_planet1.set_data(xlist_planet1[i], ylist_planet1[i])
    point_planet2.set_data(xlist_planet2[i], ylist_planet2[i])
    point_planet3.set_data(xlist_planet3[i], ylist_planet3[i])
    
    return point_planet1, point_planet2, point_planet3

anim = animation.FuncAnimation(fig, func= update, frames= len(xlist_planet1), interval = 1, blit = True)

plt.show()