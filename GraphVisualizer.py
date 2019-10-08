import numpy as np
import matplotlib.pyplot as plt

# Instructions:
# 1) Uncomment the part of the code in lander.cpp that outputs data to a .txt file.
# 2) Run the code in scenario 1 until the lander crashes / lands for different values of K_h with autopilot enabled
# 3) Copy the path of the .txt files generated and replace them with the paths below (the variable 'results' loads the .txt files from the path)

fig, axs = plt.subplots(3, 3,sharex=True)
line_labels = ["Actual Descent Rate",  "Target Descent Rate"]
results = np.loadtxt('/Users/varunbabbar/Library/Developer/Xcode/DerivedData/lander-fozniwaqqpgqwxeajmzyvkqtdyzd/Build/Products/Debug/Autopilot_Data_0.010.txt')
l1 = axs[0, 0].plot(results[:,0]/1000, results[:,1], label = 'Actual Descent Rate')[0]
axs[0, 0].set_title('Kh = 0.010')
altitude = np.linspace(0, 10, num = 200)
l2 = axs[0,0].plot(altitude, -(0.5 + 0.01*altitude*1000),label = 'Target Descent Rate')[0];
plt.xlabel('Altitude (m) x 10^3')
plt.ylabel('Descent rate')
results = np.loadtxt('/Users/varunbabbar/Library/Developer/Xcode/DerivedData/lander-fozniwaqqpgqwxeajmzyvkqtdyzd/Build/Products/Debug/Autopilot_Data_0.015.txt')
l3 = axs[0, 1].plot(results[:,0]/1000, results[:,1], label = 'Actual Descent Rate')
axs[0, 1].set_title('Kh = 0.015')
altitude = np.linspace(0, 10, num = 200)
l4 = axs[0,1].plot(altitude, -(0.5 + 0.015*altitude*1000),label = 'Target Descent Rate')[0];
plt.xlabel('Altitude (m) x 10^3')
plt.ylabel('Descent rate')
results = np.loadtxt('/Users/varunbabbar/Library/Developer/Xcode/DerivedData/lander-fozniwaqqpgqwxeajmzyvkqtdyzd/Build/Products/Debug/Autopilot_Data_0.018.txt')
l5 = axs[0, 2].plot(results[:,0]/1000, results[:,1], label = 'Actual Descent Rate')[0]
axs[0, 2].set_title('Kh = 0.018')
plt.xlabel('Altitude (m) x 10^3')
plt.ylabel('Descent rate')
altitude = np.linspace(0, 10, num = 200)
l6 = axs[0,2].plot(altitude, -(0.5 + 0.018*altitude*1000),label = 'Target Descent Rate')[0];
plt.xlabel('Altitude (m) x 10^3')
plt.ylabel('Descent rate')
results = np.loadtxt('/Users/varunbabbar/Library/Developer/Xcode/DerivedData/lander-fozniwaqqpgqwxeajmzyvkqtdyzd/Build/Products/Debug/Autopilot_Data_0.020.txt')
l7 = axs[1, 0].plot(results[:,0]/1000, results[:,1], label = 'Actual Descent Rate')[0]
axs[1, 0].set_title('Kh = 0.020')
plt.xlabel('Altitude (m) x 10^3')
plt.ylabel('Descent rate')
altitude = np.linspace(0, 10, num = 200)
l8 = axs[1 ,0].plot(altitude, -(0.5 + 0.020*altitude*1000),label = 'Target Descent Rate')[0];
plt.xlabel('Altitude (m) x 10^3')
plt.ylabel('Descent rate')
results = np.loadtxt('/Users/varunbabbar/Library/Developer/Xcode/DerivedData/lander-fozniwaqqpgqwxeajmzyvkqtdyzd/Build/Products/Debug/Autopilot_Data_0.030.txt')
l9 = axs[1, 1].plot(results[:,0]/1000, results[:,1], label = 'Actual Descent Rate')[0]
axs[1, 1].set_title('Kh = 0.030')
plt.xlabel('Altitude (m) x 10^3')
plt.ylabel('Descent rate')
altitude = np.linspace(0, 10, num = 200)
l10 = axs[1 ,1].plot(altitude, -(0.5 + 0.03*altitude*1000),label = 'Target Descent Rate')[0];
plt.xlabel('Altitude (m) x 10^3')
plt.ylabel('Descent rate')
results = np.loadtxt('/Users/varunbabbar/Library/Developer/Xcode/DerivedData/lander-fozniwaqqpgqwxeajmzyvkqtdyzd/Build/Products/Debug/Autopilot_Data_0.040.txt')
l11 = axs[1, 2].plot(results[:,0]/1000, results[:,1], label = 'Actual Descent Rate')[0]
axs[1, 2].set_title('Kh = 0.040')
plt.xlabel('Altitude (m) x 10^3')
plt.ylabel('Descent rate')
altitude = np.linspace(0, 10, num = 200)
l12 = axs[1 ,2].plot(altitude, -(0.5 + 0.04*altitude*1000),label = 'Target Descent Rate')[0];
plt.xlabel('Altitude (m) x 10^3')
plt.ylabel('Descent rate')
results = np.loadtxt('/Users/varunbabbar/Library/Developer/Xcode/DerivedData/lander-fozniwaqqpgqwxeajmzyvkqtdyzd/Build/Products/Debug/Autopilot_Data_0.050.txt')
l13  = axs[2, 0].plot(results[:,0]/1000, results[:,1])
axs[2, 0].set_title('Kh = 0.050')
plt.xlabel('Altitude (m) x 10^3')
plt.ylabel('Descent rate')
altitude = np.linspace(0, 10, num = 200)
l14 = axs[2 ,0].plot(altitude, -(0.5 + 0.05*altitude*1000),label = 'Target Descent Rate')[0];
plt.xlabel('Altitude (m) x 10^3')
plt.ylabel('Descent rate')
results = np.loadtxt('/Users/varunbabbar/Library/Developer/Xcode/DerivedData/lander-fozniwaqqpgqwxeajmzyvkqtdyzd/Build/Products/Debug/Autopilot_Data_0.060.txt')
l13  = axs[2, 1].plot(results[:,0]/1000, results[:,1])
axs[2, 1].set_title('Kh = 0.060')
plt.xlabel('Altitude (m) x 10^3')
plt.ylabel('Descent rate')
altitude = np.linspace(0, 10, num = 200)
l14 = axs[2 ,1].plot(altitude, -(0.5 + 0.06*altitude*1000),label = 'Target Descent Rate')[0];
plt.xlabel('Altitude (m) x 10^3')
plt.ylabel('Descent rate')
results = np.loadtxt('/Users/varunbabbar/Library/Developer/Xcode/DerivedData/lander-fozniwaqqpgqwxeajmzyvkqtdyzd/Build/Products/Debug/Autopilot_Data_0.070.txt')
l13  = axs[2, 2].plot(results[:,0]/1000, results[:,1])
axs[2, 2].set_title('Kh = 0.070')
plt.xlabel('Altitude (m) x 10^3')
plt.ylabel('Descent rate')
altitude = np.linspace(0, 10, num = 200)
l14 = axs[2 ,2].plot(altitude, -(0.5 + 0.07*altitude*1000),label = 'Target Descent Rate')[0];
plt.xlabel('Altitude (m) x 10^3')
plt.ylabel('Descent rate')
for ax in axs.flat:
    ax.set(xlabel='Altitude (m) x 10^3', ylabel='Descent rate')
for ax in axs.flat:
    ax.label_outer()
fig.legend([l1, l2],
           labels=line_labels,
           loc="upper right",
           borderaxespad=0.1,
           title=""
           )
plt.show()
