# steering-brake
# Breaking system:
- weight
Regular stop- 2[kg]
Emergency stop- 2.5[kg]

- Performence
The force required on the brake- 600[N]
Minimum time for a full brake- Regular stop- 0.3[sec], Emergency stop- 0.2[sec]
Minimum Braking acceleration- 8[m/s^2]
When the vehicle reaches 40 [km/h] it shold be able to stop in 10 [m] or 0.9[sec] since the moment of the emergency stop.
Full stroke of the pedal 10.8[mm]
# Steering System
- weight
2[kg]

- Performence
Maximum angle change- 200 [c] (100 for each direction)
Minimum angle change- 0.5 [c]
Time for full operation of the mechanism (steering the wheel from edge to edge)- 0.5[sec]
# Wing System
- weight
2[kg]

- Performence
The wing should be able to resist the power of 200[N] for a 225[cm] surface, and to not deviate for more than 10[mm] In the direction of load bearing.
The wing should be able to resist the power of 50[N] for every direction, and to not deviate for more than 25[mm].
The wing should be able to rise from the main surface 50 [mm].
# Regulatory requirements
- **T 11.6.5** To detect hard braking, a brake system pressure sensor must be used. The threshold must be chosen such that there are no locked wheels and the brake pressure is ≤ 30 bar.
- **T 11.8.4** The foot pedal must return to the 0 % position when not actuated. The foot pedal must have a positive stop preventing the mounted sensors from being damaged or overstressed. Two springs must be used to return the foot pedal to the 0 % position and each spring must work when the other is disconnected. Springs in the APPS are not accepted as return springs.
- **T 11.8.12** A fully released accelerator pedal must result in: 
• [EV ONLY] A wheel torque of ≤0 Nm 
• [CV ONLY] An idle position or lower throttle set-point. This may only be exceeded during a gearshift for a maximum of 500 ms.
- **EV 2.3.2** The commanded motor torque must remain at 0 Nm until the APPS signals less than 5 % pedal travel and 0 Nm desired motor torque, regardless of whether the brakes are still actuated or not.
- **EV 4.1.1** The maximum permitted voltage that may occur between any two electrical connections is 600 VDC and for motor controller/inverters internal low power control signals 630 VDC.
- **DV 1.4.3** The RES has two functions: 
• When the remote emergency stop button is pressed, it must trigger the DV Shutdown Circuit (SDC) defined in DV 1.5. 
• Race-control-to-vehicle communication: 
– The race control can send a “Go” signal to the vehicle 
– The “Go” signal replaces green flags.
- **DV 2.2.4** The power supply of the steering and braking actuators must be switched by LVMS and ASMS.
- **DV 2.2.5** When the ASMS is in “Off” position, the following must be fulfilled: 
• No steering, braking and propulsion actuation can be performed by request of the autonomous system. 
• The sensors and the processing units can stay operational. 
• The vehicle must be able to be pushed as specified in A 6.7. 
• It must be possible to operate the vehicle manually as a normal CV or EV. 
- **DV 2.2.6** It is strictly forbidden to switch the ASMS to the “On” position if a person is inside the vehicle. 
- **DV 2.2.7** After switching the ASMS to the “On” position, the vehicle may not start moving and the brakes must remain closed (“AS ready” state, Figure 21) until a “Go” signal is sent via the RES (“AS driving” state, Figure 21).
- **DV 2.3.2** The steering system may remain active during an emergency brake maneuver while vehicle is in movement.
- **DV 3.3.1** The system reaction time (the time between entering the triggered state and the start of the deceleration) must not exceed 200 ms. 
- **DV 3.3.3** Whilst decelerating, the vehicle must remain in a stable driving condition (i.e. no unintended yaw movement). This can be either a controlled deceleration (steering and braking control is active) or a stable braking in a straight line with all four wheels locked.
