import csv
import matplotlib.pyplot as plt
time = []
#altitude = [-7.7, 20.8, 43.6,75.7,105.3,78.5,95.3,65.9,140.6,115.2,123.1,113.2,128.2,122.0,108.1,105.9,105.3,105.5,104.2,102.1,100.8,101.0,99.6,97.6,96.2,95.5,94.2,93.3,91.3,89.0,89.3,89.1,88.0,87.1,86.6,84.6,82.9,82.0,80.3,79.1,77.4,75.1,72.9,71.5,69.5,68.5,66.9,65.5,63.5,60.6,58.8,57.8,57.6,56.3,54.3,53.0,51.3,50.6,48.6,47.1,45.7,45.1,44.4,43.3,41.8,40.6,40.6,39.9,38.4,36.6,36.3,34.6,34.0,33.6,31.5,29.8,28.4,28.1,26.9,26.1,25.5,24.6,23.8,22.9,21.3,20.9,20.7,20.4,19.6,18.3,17.4,17.3,17.3,16.7,17.0,16.0,14.7,15.3,15.3,15.2,15.0,14.7,14.5,13.1,13.1,12.3,11.3,11.0,10.8,11.1,11.0,10.8,10.6,10.9,10.8,10.8,10.7,10.9,10.1,8.6,8.6,9.1,8.7,8.8,5.1,5.0,6.3,5.5,5.4,5.2,4.9,5.2]
time_series = []
altitude = []
GyroX = []
GyroY = []
GyroZ = []
AccelX = []
AccelY = []
AccelZ = []
Pitch = []
Roll = []
Heading = []

with open('flight data.txt', 'r') as file:
    data = file.readlines()
    for line in data:
        alt = line.find('relative altitude: ')
        if alt != -1:
            output = (line[alt+20:alt+23])
            output = output.replace(',','').replace(' ','')
            altitude.append(float(output))
    
    for line in data:
        GyroX_Find = line.find('G: ')
        if GyroX_Find != -1:
            output = (line[GyroX_Find+3:GyroX_Find+9])
            output = output.replace(',','').replace(' ','')
            GyroX.append(float(output))

    for line in data: 
        GyroY_Find = line.find('G: ')
        if GyroY_Find != -1:
            output = (line[GyroY_Find+10:GyroY_Find+14])
            output = output.replace(',','').replace(' ','')
            GyroY.append(float(output))

    for line in data:
        GyroZ_Find = line.find('G: ')
        if GyroZ_Find != -1:
            output = (line[GyroZ_Find+16:GyroZ_Find+24])
            #Scan the string output to find the thrid number after two commas
            #string sample: G: -273.25, -77.53, 102.97 deg/s
            output = output.replace(',','').replace(' ','').replace('d','').replace('g','').replace('e','')
            #print('Normal Data: ',output)
            if output == '2-35.2' or '7-286.' or '1-54.8' or '4-93.5' or '6-99.7' or '9-88.5' or '5-25.1' or '0-63.3':
                output = output.replace('2-','').replace('7-','').replace('1-','').replace('4-','').replace('6-','').replace('9-','').replace('5-','').replace('0-','')
                GyroZ.append(float(output))
            else:
                output = output.replace('669.24','69.24').replace('7197.3','197.3').replace('8286.6','286.6').replace('7286.0','286.0').replace('53102.0','102.0').replace('7495.','495.2')
                GyroZ.append(float(output))
    
    for line in data:
        AccelX_Find = line.find('A: ')
        if AccelX_Find != -1:
            output = (line[AccelX_Find+3:AccelX_Find+8])
            output = output.replace(',','').replace(' ','')
            AccelX.append(float(output))

    for line in data:
        AccelY_Find = line.find('A: ')
        if AccelY_Find != -1:
            output = (line[AccelY_Find+10:AccelY_Find+14])
            output = output.replace(',','').replace(' ','')
            AccelY.append(float(output))

    for line in data:
        AccelZ_Find = line.find('A: ')
        if AccelZ_Find != -1:
            output = (line[AccelZ_Find+16:AccelZ_Find+22])
            output = output.replace(',','').replace(' ','').replace('d','').replace('g','').replace('e','')
            AccelZ.append(float(output))
    
    for line in data:
        Pitch_find = line.find('Pitch, Roll: ')
        if Pitch_find != -1:
            output = (line[Pitch_find+14:Pitch_find+19])
            output = output.replace(',','').replace(' ','')
            Pitch.append(float(output))

    for line in data:
        Roll_find = line.find('Roll, Pitch: ')
        if Roll_find != -1:
            output = (line[Roll_find+19:Roll_find+24])
            output = output.replace(',','').replace(' ','')
            Roll.append(float(output))

    for line in data:
        Heading_find = line.find('Heading: ')
        if Heading_find != -1:
            output = (line[Heading_find+10:Heading_find+15])
            output = output.replace(',','').replace(' ','')
            Heading.append(float(output))

for i in range (len(GyroX)):
    GyroX[i] = float(GyroX[i])
    #print('GyroX: ',GyroX[i])     

for i in range (len(GyroY)):
    GyroY[i] = float(GyroY[i])
    #print('GyroY: ',GyroY[i])

for i in range (len(GyroZ)):
    GyroZ[i] = float(GyroZ[i])
    if GyroZ[i] > 1000:
        if GyroZ[i] == 53102.0:
            GyroZ[i] = 102.0
        elif GyroZ[i] == 7495.2:
            GyroZ[i] = 495.5
        elif GyroZ[i] == 7197.3:
            GyroZ[i] = 197.3
        elif GyroZ[i] == 8286.6:
            GyroZ[i] = 286.6
        elif GyroZ[i] == 7286.0:
            GyroZ[i] = 286.0
        elif GyroZ[i] == 7286.6:
            GyroZ[i] = 286.6
        elif GyroZ[i] == 72286.0:
            GyroZ[i] = 286.0
        elif GyroZ[i] == 4286.6:
            GyroZ[i] = 286.6


for i in range (len(AccelX)):
    AccelX[i] = float(AccelX[i]*9.8)
    #print('AccelX: ',AccelX[i])

for i in range (len(AccelY)):
    AccelY[i] = float(AccelY[i]*9.8)
    #print('AccelY: ',AccelY[i])

for i in range (len(AccelZ)):
    AccelZ[i] = float(AccelZ[i]*9.8)
    #print('AccelZ: ',AccelZ[i])

for i in range (len(altitude)):
    altitude[i] = float(altitude[i])
    #print('Altitude: ',altitude[i])

for i in range (0,len(altitude)):
    time_series.append(float(i)*0.25)
    print('Time: ',time_series[i])

print(len(altitude))

#for i in range(0,len(altitude)):
 #   time[i] = float(time[i]*0.25)
  #  print()
#with open('flight data.csv', 'w') as file:
 #   writer = csv.writer(file)
  #  writer.writerow(['time','Altitude','GyroX','GyroY','GyroZ','AccelX','AccelY','AccelZ'])
   # writer.writerows(zip(time_series,altitude,GyroX,GyroY,GyroZ,AccelX,AccelY,AccelZ))
    #file.close()


with open('accz-data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['time_series','AccelZ'])
    writer.writerows(zip(time_series,AccelZ))
    file.close()


#with open('alt.csv' ,'w') as file:
 #   write = csv.writer(file)
  #  write.writerow(['time','altitude'])
   # write.writerows(zip(time_series,altitude))
    #file.close()

plt.title('2021 STL Mission Flight Performance Plot')
plt.xlabel(r'time in seconds(discrete time, interval(250 ms))')
#plt.ylabel(r'alt (altitude  in meters)')
plt.ylabel(r'Acceleration (m/s^2)')
#plt.plot(time, altitude, 'r', label='altitude')

#Plots the dynamics data from the altitude, gyroscope, and accelerometer
plt.plot(time_series,altitude)
#plt.plot(altitude)
plt.plot(time_series,AccelX)
plt.plot(time_series,AccelY)
plt.plot(time_series,AccelZ)

#plt.plot(GyroX)
#plt.plot(GyroY)
#plt.plot(GyroZ)

#plt.plot(Pitch)
#plt.plot(Roll)
#plt.plot(Heading)
plt.grid()
plt.legend(['Alt','AccelX','AccelY','AccelZ','GyroX','GyroY','GyroZ','Pitch','Roll','Heading'], loc='upper right')

#plt.legend(['altitude','GyroX','GyroY','GyroZ', 'AccelX', 'AccelY', 'AccelZ'], loc='upper right')

plt.show()