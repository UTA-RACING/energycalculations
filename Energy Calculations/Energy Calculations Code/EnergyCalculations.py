import csv
import statistics
from matplotlib import pyplot as plt

#First we need to load and parse the csv files that contain our data
filename ="../../EnduranceData/truenewclean.csv" #Location of the csv file

data =[]
masscar = 213.6 # cars mass in kilograms
massdriver = 77.1107 #estimated drivers mass in kilograms
mass = masscar + massdriver

with open(filename, "r") as csvfile:
    csvreader = csv.reader(csvfile , delimiter=',')
    linecount = 0
    for line in csvreader:
        data.append(line)
time = .002
del data[0]
del data[0]

accellist = [] #acceleration in m/s
for i in range(len(data)):
    accel = float(data[i][1])*9.81
    accellist.append(accel)

velocitylist = []#Velocity in m/s
for i in range(len(accellist)):
    vel = float(data[i][2])*(5/18)
    velocitylist.append(vel)

forcelist = []#In (Kg*m)/(s^2) AKA Newton
for i in range(len(velocitylist)):
    force = (mass * (accellist[i]))
    if (accellist[i] > 0):
        force = force + .5*(1.55)*(1.2)*(velocitylist[i]**2) #Aero force .5(CdA)(rho)(V^2)
        forcelist.append(force)
    else:
        force = force - .5*(1.55)*(1.2)*(velocitylist[i]**2) #Aero force .5(CdA)(rho)(V^2)
        forcelist.append(force)

powerlist = []#In (Kg*m^2)/(s^3) AKA Watts
for i in range(len(forcelist)):
    power = (forcelist[i] * velocitylist[i])
    powerlist.append(power)
    
energylist = []#In Watt*s
for i in range(len(powerlist)):
    energy = powerlist[i] *time #Watts times second
    energylist.append(energy)

energytotalpos = 0
energytotalneg = 0
for i in range(len(data)):
    if (energylist[i] > 0):
        energytotalpos = energytotalpos + energylist[i]
    else:
        energytotalneg = energytotalneg + energylist[i]

energytotalpos = (energytotalpos/3600000) #Conversion to KWH
energytotalneg = (energytotalneg/3600000) #Conversion to KWH
    
powerlisthp = [] #Power in hp
for i in range (len(powerlist)):
    if (powerlist[i] > 0):
        powerhp = powerlist[i]/746
        powerlisthp.append(powerhp)

powerlisthp50 = []
newpower = 0
for i in range (len(powerlisthp)):
    if ((i % 100) != 0):
        newpower = newpower + powerlisthp[i]
    else:
        newpower = newpower/100
        powerlisthp50.append(newpower)
        newpower = 0



#Plotting
averagehp = statistics.mean(powerlisthp)
hpstd = statistics.stdev(powerlisthp)
firstsigmaleft = averagehp - hpstd
firstsigmaright = averagehp + hpstd
plt.vlines(averagehp, 0, 200, color = 'red', label='Average Horsepower')
plt.vlines(firstsigmaleft, 0, 200, color = 'green', label='Average-1sigma')
plt.vlines(firstsigmaright, 0, 200, color = 'yellow', label='Average+1sigma')
plt.legend()
plt.xlabel("Horsepower")
plt.ylabel("Occurences")
plt.hist(powerlisthp50, bins=50)
plt.show()
print("hello")