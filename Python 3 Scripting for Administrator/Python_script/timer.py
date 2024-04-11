#!/usr/bin/env python3.8

from time import localtime, strftime, mktime

# start time
start_time = localtime()
print(f"Timer started at: {strftime('%X', start_time)}")

# Wait for user input enter
input("Press 'Enter' Key to stop timer ")

# Stop time
stop_time = localtime()
print(f"Timer stopped at: {strftime('%X',stop_time)}")

#Total timer
differ_timer = mktime(stop_time) - mktime(start_time)
print(f"Total timer: {differ_timer} seconds ")
