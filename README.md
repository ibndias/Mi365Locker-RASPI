# Xiaomi Scooter Program

This program send commands to Xiaomi m365 scooters over Bluetooth Low Energy for Linux systems.
# Install

Uses python3.

Requires [bluepy](https://github.com/IanHarvey/bluepy) to run correctly. 

Install bluepy with `sudo pip3 install bluepy`

# Run

The program takes two arguments: 
   1) the type of scan 
   2) command to send to the scooter

The first argument can either be `scan` which scans all available devices or `saved` which scans all known devices saved in a file. If during a `scan` the program succesfully locates a scooter it will save its address in the known devices file.

The second argument can be one the following commands:

   - `lock` - this locks the scooter
   - `unlock` - this unlocks the scooter
   
Sudo is required to run the progarm in order to gain access to the lower bluetooth functions. 

Example to run the program:

`sudo python3 scooter-scan.py scan unlock`