import csv

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

velocitylist = []
for i in range(len(velocity)):
    vel = float(velocity[i][2])
    velocitylist.append(vel)

accelist = []
for i in range(len(velocitylist)):
    if (i == 0):
        accel = ((velocitylist[i] - 0)/ time)
        accelist.append(accel)
    else:
        j = i-1
        accel = ((velocitylist[i] - velocitylist[j])/ time)
        accelist.append(accel)

forcelist = []
for i in range(len(accelist)):
    force = (mass* accelist[i])
    forcelist.append(force)

powerlist = []
for i in range(len(forcelist)):
    power = (forcelist[i] * velocitylist[i])
    powerlist.append(power)

energylist = []
for i in range(len(powerlist)):
    energy = powerlist[i] * time #Watt*s
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

print("hello")