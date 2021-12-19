import numpy as np
import matplotlib.pyplot as plt

noiseConst = 0.1
altModel = 
altMeter_Data
timeInterval = 0.25
Max_Time_Duration = 10
IMU_Data

def Optimal_Altitude_Estimation(altModel, altMeter_Data, timeInterval, Max_Time_Duration):
    # Initialize the variables
    time = 0
    alt = 0
    alt_est = 0
    alt_est_array = []
    alt_array = []
    time_array = []
    # Calculate the altitude
    while time < Max_Time_Duration:
        alt_est = altModel(alt, time)
        alt_est_array.append(alt_est)
        alt_array.append(alt)
        time_array.append(time)
        time += timeIntervalXC