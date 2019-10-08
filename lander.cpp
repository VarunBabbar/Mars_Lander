// Mars lander simulator
// Version 1.11
// Mechanical simulation functions
// Gabor Csanyi and Andrew Gee, August 2019

// Permission is hereby granted, free of charge, to any person obtaining
// a copy of this software and associated documentation, to make use of it
// for non-commercial purposes, provided that (a) its original authorship
// is acknowledged and (b) no modified versions of the source code are
// published. Restriction (b) is designed to protect the integrity of the
// exercise for future generations of students. The authors would be happy
// to receive any suggested modifications by private correspondence to
// ahg@eng.cam.ac.uk and gc121@eng.cam.ac.uk.

#include "lander.h"
#define DECLARE_GLOBAL_VARIABLES
#include <fstream>
#include <random>
#include <cstdlib>
#include <string>

void autopilot (void)
// Autopilot to adjust the engine throttle, parachute and attitude control
{
    static double K_h, K_p, error, Delta,altitude, P_out;
    static vector3d current_velocity,norm,p,q,up, ccoords;
    K_h = 0.015;
    K_p = 0.5;
    Delta = 0.35;
    altitude = position.abs() - MARS_RADIUS;
    norm = position.norm();
    current_velocity = velocity;
    error = -(current_velocity*norm + 0.5 + K_h*altitude);
    P_out = K_p*error;
    if (P_out < -Delta){
        throttle = 0;
    }
    if (-Delta <= P_out) {
        if (P_out < 1- Delta){
            throttle = P_out + Delta;
        }
    }
    if (P_out >= 1- Delta) {
        throttle = 1;
    }
    
        if (safe_to_deploy_parachute())  {
            if (altitude < 60000){
                parachute_status = DEPLOYED;
            }
        }
    attitude_stabilization();
    
    //         Output the autopilot data
    //        string a;
//    string a = to_string((K_h * 100) / 100).substr(0,5);
//    ofstream fout;
//    fout.open("Autopilot_Data_" + a + ".txt",ios_base::app);
//    if (fout) {
//        fout << altitude << ' ' << current_velocity*norm << endl;
//    }
}

void numerical_dynamics (void)
// This is the function that performs the numerical integration to update the
// lander's pose. The time step is delta_t (global variable).
{
    
    static vector3d previous_position,current_position,new_position, previous_velocity,up,axis,left,out,result,ccoords;
    vector3d thrust,drag,grav,force,drag1, drag2,new_velocity;
    string A;
    static double altitude,fuel_mass,lander_mass, total_mass;
    static double pi,lander_area, parachute_area,density;
    bool w;
    static bool integration;
    pi = atan(1)*4;
    lander_area = pi*LANDER_SIZE*LANDER_SIZE;
    parachute_area = 5*4*LANDER_SIZE*LANDER_SIZE;
    altitude = position.abs() - MARS_RADIUS;
    w = wind_enabler();
    integration = t();
    if (w)
    {random_wind = randomwindgenerator();}
    else{
        random_wind = vector3d(0,0,0);
    }
    
    thrust = thrust_wrt_world();
    fuel_mass = fuel*FUEL_CAPACITY*FUEL_DENSITY;
    lander_mass = UNLOADED_LANDER_MASS;
    density = atmospheric_density(position);
    new_velocity = velocity;
    new_position =  position;
    total_mass = lander_mass + fuel_mass;
    if (parachute_status == DEPLOYED){
        drag1 = -0.5*density*DRAG_COEF_LANDER*(lander_area)*new_velocity.abs2()*new_velocity.norm();
        drag2 = -0.5*density*DRAG_COEF_CHUTE*(parachute_area)*new_velocity.abs2()*new_velocity.norm();
        drag = drag1 + drag2;
    }
    
    if (parachute_status == NOT_DEPLOYED or parachute_status == LOST){
        drag = -0.5*density*DRAG_COEF_LANDER*(lander_area)*new_velocity.abs2()*new_velocity.norm();
    }
    grav = GRAVITY*MARS_MASS*total_mass*new_position.norm() / (new_position.abs2());
    
    
    // Vertlet Integration //
    if (integration){
        force = -drag+grav-thrust;
        if (simulation_time == 0){
            previous_position = position;
            new_velocity = velocity;
            new_position = previous_position + delta_t*new_velocity;
            current_position = new_position;
            position = new_position;
            new_velocity = new_velocity+ (delta_t/total_mass)*force;
            velocity = new_velocity;
        }
        else{
            current_position = position;
            new_position = current_position*2 -previous_position - (delta_t*delta_t*force)/total_mass;
            new_velocity = (1/(delta_t*2))*(new_position-previous_position);
            previous_position = current_position;
            position = new_position;
            velocity = new_velocity+random_wind;
        }
    }
    // Euler Integration //
    
    else{
        force = drag-grav+thrust;
        previous_position = position;
        previous_velocity = velocity;
        new_position = previous_position + delta_t*previous_velocity;
        new_velocity = previous_velocity + (delta_t/total_mass)*force;
        velocity = new_velocity+random_wind;
        position = new_position;
    }
    
    // Euler Integration //
    
    //    cout << drag.abs();
    //    cout << "    ";
    //    string a = to_string(velocity.x);
    //    string b = to_string(velocity.y);
    //    string c = to_string(velocity.z);
    //
    //    cout << "X-force is: " + a + " ";
    //    cout << "Y-force is: " + b + " ";
    //    cout << "Z-force is: " + c + " ";
    //     Here we can apply an autopilot to adjust the thrust, parachute and attitude
    if (autopilot_enabled) {
        autopilot();
    }
    
    // Here we can apply 3-axis stabilization to ensure the base is always pointing downwards
    if (stabilized_attitude) attitude_stabilization();
}

void initialize_simulation (void)
// Lander pose initialization - selects one of 10 possible scenarios
{
    // The parameters to set are:
    // position - in Cartesian planetary coordinate system (m)
    // velocity - in Cartesian planetary coordinate system (m/s)
    // orientation - in lander coordinate system (xyz Euler angles, degrees)
    // delta_t - the simulation time step
    // boolean state variables - parachute_status, stabilized_attitude, autopilot_enabled
    // scenario_description - a descriptive string for the help screen
    
    scenario_description[0] = "circular orbit";
    scenario_description[1] = "descent from 10km";
    scenario_description[2] = "elliptical orbit, thrust changes orbital plane";
    scenario_description[3] = "polar launch at escape velocity (but drag prevents escape)";
    scenario_description[4] = "elliptical orbit that clips the atmosphere and decays";
    scenario_description[5] = "descent from 200km";
    scenario_description[6] = "Aerostationary Orbit";
    scenario_description[7] = "";
    scenario_description[8] = "";
    scenario_description[9] = "";
    
    switch (scenario) {
            
        case 0:
            // a circular equatorial orbit
            position = vector3d(1.2*MARS_RADIUS, 0.0, 0.0);
            velocity = vector3d(0.0, -3247.087385863725, 0.0);
            orientation = vector3d(0.0, 90.0, 0.0);
            delta_t = 0.1;
            parachute_status = NOT_DEPLOYED;
            stabilized_attitude = false;
            autopilot_enabled = false;
            break;
            
        case 1:
            // a descent from rest at 10km altitude
            position = vector3d(0.0, -(MARS_RADIUS + 10000.0), 0.0);
            velocity = vector3d(0.0, 0.0, 0.0);
            orientation = vector3d(0.0, 0.0, 90.0);
            delta_t = 0.1;
            parachute_status = NOT_DEPLOYED;
            stabilized_attitude = true;
            autopilot_enabled = false;
            break;
            
        case 2:
            // an elliptical polar orbit
            position = vector3d(0.0, 0.0, 1.2*MARS_RADIUS);
            velocity = vector3d(3500.0, 0.0, 0.0);
            orientation = vector3d(0.0, 0.0, 90.0);
            delta_t = 0.1;
            parachute_status = NOT_DEPLOYED;
            stabilized_attitude = false;
            autopilot_enabled = false;
            break;
            
        case 3:
            // polar surface launch at escape velocity (but drag prevents escape)
            position = vector3d(0.0, 0.0, MARS_RADIUS + LANDER_SIZE/2.0);
            velocity = vector3d(0.0, 0.0, 5027.0);
            orientation = vector3d(0.0, 0.0, 0.0);
            delta_t = 0.1;
            parachute_status = NOT_DEPLOYED;
            stabilized_attitude = false;
            autopilot_enabled = false;
            break;
            
        case 4:
            // an elliptical orbit that clips the atmosphere each time round, losing energy
            position = vector3d(0.0, 0.0, MARS_RADIUS + 100000.0);
            velocity = vector3d(4000.0, 0.0, 0.0);
            orientation = vector3d(0.0, 90.0, 0.0);
            delta_t = 0.1;
            parachute_status = NOT_DEPLOYED;
            stabilized_attitude = false;
            autopilot_enabled = false;
            break;
            
        case 5:
            // a descent from rest at the edge of the exosphere
            position = vector3d(0.0, -(MARS_RADIUS + EXOSPHERE), 0.0);
            velocity = vector3d(0.0, 0.0, 0.0);
            orientation = vector3d(0.0, 0.0, 90.0);
            delta_t = 0.1;
            parachute_status = NOT_DEPLOYED;
            stabilized_attitude = true;
            autopilot_enabled = false;
            break;
            
        case 6:
            // Aerostationary Orbit
            position = vector3d(20426573.1, 0.0, 0.0);
            velocity = vector3d(0.0, 1447.88, 0.0);
            orientation = vector3d(0, 0, 90.0);
            delta_t = 0.1;
            parachute_status = NOT_DEPLOYED;
            stabilized_attitude = false;
            autopilot_enabled = false;
            break;
        case 7:
            //
            
            
            
            break;
            
        case 8:
            break;
            
        case 9:
            break;
            
    }
}

