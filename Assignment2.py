import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# Altitude = 1000 Km
# Velocity for circular orbit = 3124.6 m /s in the y direction
# Velocity for elliptical orbit with eccentricity > 0: 3124.6 < velocity ≤ 4418.87 m / s
# Velocity for hyperbolic orbit >  4418.87 m / s

# mass, spring constant, initial position and velocity
M = 6.42 * (10**23)
G = 6.67*(10**-11)
radius = 3386000.0
# simulation time, time-step and time
t_max = 100000
dt = 1
t_array = np.arange(0, t_max, dt)

# initialise empty lists to record trajectories
x_list = np.array([0,0,0])
v_list = np.array([0,0,0])
# Euler integration

x_vert= np.array([0,4386000,0])
v_vert = np.array([4418,0,0])

altitude = np.linalg.norm(x_vert)-radius
x_value_euler = np.array([])
y_value_euler = np.array([])
z_value_euler = np.array([])
height_euler = np.array([])

for index2 in range(len(t_array)):
    # Euler Integration
    if altitude < 0:
        break;
    # append current state to trajectories
    # calculate new position and velocity
    magnitude_x = np.linalg.norm(x_vert)
    magnitude_v = np.linalg.norm(v_vert)
    altitude = magnitude_x - radius
    height_euler =  np.append(height_euler,altitude)
    a = -np.multiply(x_vert,((G*M)/(magnitude_x**3)))
    x_vert = x_vert + dt * v_vert
    v_vert = v_vert + dt * a
    x_value_euler = np.append(x_value_euler,x_vert[0])
    y_value_euler = np.append(y_value_euler,x_vert[1])
    z_value_euler = np.append(z_value_euler,x_vert[2])

# Vertlet Integration
x_vert= np.array([0,4386000,0])
v_vert = np.array([4418,0,0])
altitude = np.linalg.norm(x_vert)-radius
x_value_vertlet = np.array([])
y_value_vertlet = np.array([])
z_value_vertlet = np.array([])
height_vertlet = np.array([])

for index in range(len(t_array)):
    # Vertlet Integration
    if altitude < 0:
        break;
    if index == 0:
        x_previous = x_vert
        x1 = x_vert + dt*v_vert
    magnitude_x = np.linalg.norm(x1)
    magnitude_v = np.linalg.norm(v_vert)
    altitude = magnitude_x - radius
    current_x = x1
    height_vertlet = np.append(height_vertlet,altitude)
    a = -np.multiply(current_x,(((dt**2)*G*M)/(magnitude_x**3)))
    x1 = current_x*2 - x_previous + a
    v_vert = (1/(2*dt))*(x1-x_previous)
    x_previous = current_x
    x_list_vert = np.column_stack((x_list,x_vert))
    x_value_vertlet = np.append(x_value_vertlet,x1[0])
    y_value_vertlet = np.append(y_value_vertlet,x1[1])
    z_value_vertlet = np.append(z_value_vertlet,x1[2])

figure1 = plt.figure(1)
figure1.suptitle('Altitude vs time graph for Vertlet Integration')
plt.clf()
plt.xlabel('time (s)')
plt.ylabel('altitude (m)')
plt.grid()
plt.plot(t_array[0:len(height_vertlet)], height_vertlet, label='x (m)')
plt.show()

figure2 = plt.figure(2)
figure2.suptitle('Orbital Trajectory for Vertlet Integration')
plt.clf()
plt.xlabel('x-coordinate (m)')
plt.ylabel('y-coordinate (m)')
plt.grid()
plt.plot(x_value_vertlet, y_value_vertlet, label='x (m)')
plt.show()

figure3 = plt.figure(3)
figure3.suptitle('Altitude vs time graph for Euler Integration')
plt.clf()
plt.xlabel('time (s)')
plt.ylabel('altitude (m)')
plt.grid()
plt.plot(t_array[0:len(height_euler)], height_euler, label='x (m)')
plt.show()

figure4 = plt.figure(4)
figure4.suptitle('Orbital Trajectory for Euler Integration')
plt.clf()
plt.xlabel('x-coordinate (m)')
plt.ylabel('y-coordinate (m)')
plt.grid()
plt.plot(x_value_euler, y_value_euler, label='x (m)')
plt.show()