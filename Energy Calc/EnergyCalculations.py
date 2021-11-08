import csv

#First we need to load and parse the csv files that contain our data
filename ="newclean.csv" #Location of the csv file

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

velocitylist = []
for i in range(len(acceleration)):
    if (i == 0 ):
        vel = (0.00 + (float(acceleration[i][1])*9.8) * time) 
        velocitylist.append(vel)
    else:
        j = i-1
        vel = velocitylist[j] + ((float(acceleration[i][1])*9.8) * time)
        velocitylist.append(vel) 

forcelist = []
for i in range(len(acceleration)):
    force = (mass * (float(acceleration[i][1])*9.8))
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
for i in range(len(acceleration)):
    if (float(acceleration[i][1]) > 0):
        energytotal = energytotal + powerlist[i]

energytotal = (energytotal/1000)
energytotal = (energytotal/3600) 
velocitylist2 =  sorted(velocitylist, reverse=True)
print("heloup")

