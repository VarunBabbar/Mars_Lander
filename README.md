# Mars Lander
My solution contains code to simulate the motion of a rover that can orbit / land on Mars. Some unique features of the solution include:
1. An option to switch to either Euler or Vertlet integration methods during the game by pressing the ’i’ key on the keyboard.
2. Enhanced autopilot that can automatically deploy a parachute at lower altitudes when the software deems it safe to be able to do so. This ensures that the autopilot works in all scenarios.
3. Modelling of an aerostationary orbit.
4. Possibility of any-angle attitude control in the plane of the orbit. This can be done by pressing the ’/’ or the ’.’ keys on the keyboard for rotation in either direction. These keys, like the thrust keys, are disabled if the attitude stabilizer or the autopilot is switched on.
5. Basic modelling of random wind gusts. The software contains a random wind generator that can be enabled or disabled by pressing the ’W’ key.

# Running the lander

To run the game, run the following command on terminal

``
g++ lander.cpp
``

This will produce an executable file called a.out, which you can run by typing this in your terminal:

`` 
./a.out
``
