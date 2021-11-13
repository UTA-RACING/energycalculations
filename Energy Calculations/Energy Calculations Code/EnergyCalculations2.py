import csv
import statistics
from matplotlib import pyplot as plt


#First we need to load and parse the csv files that contain our data
filename ="../../EnduranceData/gpsspeed.csv" #Location of the csv file

velocity =[] 
masscar = 213.6 # cars mass in kilograms
massdriver = 77.1107 #estimated drivers mass in kilograms
mass = masscar + massdriver

with open(filename, "r") as csvfile:
    csvreader = csv.reader(csvfile , delimiter=',')
    linecount = 0
    for line in csvreader:
        velocity.append(line)
time = .002
del velocity[0]
del velocity[0]

velocitylist = [] #In m/s
for i in range(len(velocity)):
    vel = float(velocity[i][2])
    velocitylist.append(vel) 

accelist = [] #In m/s^2
for i in range(len(velocitylist)):
    if (i == 0):
        accel = ((velocitylist[i] - 0)/ time)
        accelist.append(accel)
    else:
        j = i-1
        accel = ((velocitylist[i] - velocitylist[j])/ time)
        accelist.append(accel)

forcelist = [] #In (Kg*m)/(s^2) AKA Newton
for i in range(len(accelist)):
    force = (mass* accelist[i])
    forcelist.append(force)

powerlist = [] #In (Kg*m^2)/(s^3) AKA Watts
for i in range(len(forcelist)):
    power = (forcelist[i] * velocitylist[i])
    powerlist.append(power)

energylist = [] #In Watt*s
for i in range(len(powerlist)):
    energy = powerlist[i] * time 
    energylist.append(energy)

energytotalpos = 0
energytotalneg = 0
for i in range(len(velocity)):
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
plt.vlines(averagehp, 0, 600, color = 'red', label='Average Horsepower')
plt.vlines(firstsigmaleft, 0, 600, color = 'green', label='Average-1sigma')
plt.vlines(firstsigmaright, 0, 600, color = 'green', label='Average+1sigma')
plt.legend()
plt.xlabel("Horsepower")
plt.ylabel("Occurences")
plt.hist(powerlisthp50, bins=50)
plt.show()
print("hello")