#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

// t  =  100, dt = 0.00001
// Execution time for Python code with Vertlet Integration is: 17.146 seconds
// Execution time for C++ code with Vertlet Integration and no optimization is: 1.561 seconds
// Execution time for C++ code with Vertlet Integration and fast optimization is: 0.445 seconds
// Execution time for C++ code with Vertlet Integration and faster optimization is: 0.399 seconds
// Execution time for C++ code with Vertlet Integration and fastest optimization is: 0.392 seconds
// Execution time for C++ code with Vertlet Integration and fastest, smallest optimization is: 0.399 seconds
// Execution time for C++ code with Vertlet Integration and fastest, agressive optimization is: 0.393 seconds



int main() {
    clock_t start, end;
    start = clock();
    // declare variables
    double m, k, x, v, t_max, dt, t,x_previous,x1,x_current;
    vector<double> t_list, x_list, v_list;
    
    // mass, spring constant, initial position and velocity
    m = 1;
    k = 1;
    x = 0;
    v = 1;
    
    // simulation time and timestep
    t_max = 100;
    dt = 0.00001;
    
    // Vertlet integration
    for (t = 0; t <= t_max; t = t + dt) {
        if(t == 0){
            x_previous = x;
            x1 = x + dt*v;
        }
        // append current state to trajectories
        x_current = x1;
        x1 = x_current*2 - x_previous -((dt*dt)*k*x_current / m);
        x_previous = x_current;
        v = (1/(2*dt))*(x1-x_previous);
        t_list.push_back(t);
        x_list.push_back(x1);
        v_list.push_back(v);
    }
    // Write the trajectories to file
    ofstream fout;
    fout.open("trajectories.txt");
    if (fout) { // file opened successfully
        for (int i = 0; i < t_list.size(); i = i + 1) {
            fout << t_list[i] << ' ' << x_list[i] << ' ' << v_list[i] << endl;
        }
    } else { // file did not open successfully
        cout << "Could not open trajectory file for writing" << endl;
    }
    end = clock();
    double time_taken = double(end-start) / double(CLOCKS_PER_SEC);
    cout << "Time taken by program is : " << fixed
    << time_taken;
    cout << " sec " << endl;
    /* The file can be loaded and visualised in Python as follows:
     
     import numpy as np
     import matplotlib.pyplot as plt
     results = np.loadtxt('trajectories.txt')
     plt.figure(1)
     plt.clf()
     plt.xlabel('time (s)')
     plt.grid()
     plt.plot(results[:, 0], results[:, 1], label='x (m)')
     plt.plot(results[:, 0], results[:, 2], label='v (m/s)')
     plt.legend()
     plt.show()
     
     */
}
