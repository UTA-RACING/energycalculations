import csv

#First we need to load and parse the csv files that contain our data
filename ="../../EnduranceData/newclean.csv" #Location of the csv file

acceleration =[]
masscar = 213.6 # cars mass in kilograms
massdriver = 77.1107 #estimated drivers mass in kilograms
mass = masscar + massdriver

with open(filename, "r") as csvfile:
    csvreader = csv.reader(csvfile , delimiter=',')
    linecount = 0
    for line in csvreader:
        acceleration.append(line)
time = .002
del acceleration[0]
del acceleration[0]

accellist = []
for i in range(len(acceleration)):
    accel = float(acceleration[i][1])*9.81
    accellist.append(accel)

velocitylist = []
for i in range(len(accellist)):
    if (i == 0):
        vel = (0.00 + (accellist[i] * time)) 
        velocitylist.append(vel)
    else:
        j = i-1
        vel = velocitylist[j] + (accellist[i] * time)
        velocitylist.append(vel) 

forcelist = []
for i in range(len(velocitylist)):
    force = (mass * (accellist[i]))
    forcelist.append(force)

powerlist = []
for i in range(len(forcelist)):
    power = (forcelist[i] * velocitylist[i])
    powerlist.append(power)
    
energylist = []
for i in range(len(powerlist)):
    energy = powerlist[i] *time #Watts times second
    energylist.append(energy)

energytotal = 0      
for i in range(len(powerlist)):
    if (energylist[i] > 0):
        energytotal = energytotal + energylist[i]

energytotal = (energytotal/3600000)
print("heloup")

