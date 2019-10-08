# uncomment the next line if running in a notebook
# %matplotlib inline
import numpy as np
import time
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
start_time = time.time()
# mass, spring constant, initial position and velocity
m = 1
k = 1
x = 0
v = 1

# simulation time, time-step and time
t_max = 100
dt = 0.01
t_array = np.arange(0, t_max, dt)

# initialise empty lists to record trajectories
x_list = []
v_list = []
# Euler integration

x_list_vert = []
v_list_vert = []
m_vert = 1
k_vert = 1
x_vert = 0
v_vert = 1
for t in t_array:

    # append current state to trajectories
    x_list.append(x)
    v_list.append(v)

    # calculate new position and velocity
    a = -k * x / m
    x = x + dt * v
    v = v + dt * a
for t in t_array:
    # Vertlet Integration
    if t == 0:
        x_previous = x_vert;
        x1 = x_vert + dt*v_vert;
        x_list_vert.append(x1)
        v_list_vert.append(v_vert)
    if t !=0:
        x_current = x1
        x1 = x_current*2 - x_previous -((dt*dt)*k*x_current / m)
        x_previous = x_current
        v_vert = (1/(2*dt))*(x1-x_previous);
        x_list_vert.append(x1)
        v_list_vert.append(v_vert)

# convert trajectory lists into arrays, so they can be sliced (useful for Assignment 2)
x_array = np.array(x_list)
v_array = np.array(v_list)

x_vert_array = np.array(x_list_vert)
v_vert_array = np.array(v_list_vert)
end_time = time.time()
time = end_time - start_time
print("Elapsed Time: " + str(time))
# plot the position-time graph
plt.figure(1)
plt.clf()
plt.xlabel('Euler Integration: time (s)')
plt.grid()
plt.plot(t_array, x_array, label='x (m)')
plt.plot(t_array, v_array, label='v (m/s)')
plt.legend()
plt.show()

plt.figure(2)
plt.clf()
plt.xlabel('Vertlet Integration: time (s)')
plt.grid()
plt.plot(t_array, x_vert_array, label='x (m)')
plt.plot(t_array, v_vert_array, label='v (m/s)')
plt.legend()
plt.show()