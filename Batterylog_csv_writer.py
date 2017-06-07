
# coding: utf-8

Batteries= ["MAT0001.csv","MAT0002.csv","MAT0003.csv","MAT0004.csv","MAT0005.csv","MAT0006.csv","MAT0007.csv","MAT0008.csv"]


#User selects battery to log
def choosebattery():
    done = False
    while not done:
        choice = (int(input("Which battery? (1-8):")))
        choice -= 1
        if(choice in range(8)):    
            return Batteries[choice]
            done = True
        else:
            print('Sorry, selection must be between 1-8')
cbat = choosebattery()

import csv

with open(cbat,"r") as file:
    read = csv.reader(file)
    lines = [row for row in read]
for line in lines[0:1]:
    print (line)
for last in lines[-1:]:
    print (last)

#Collect Cycle input
print ("Enter Current Cycle")
response = None
while response not in {"Y", "N"}:
    response = input("Please enter Y or N: ")
    response = response.upper()
    cy = response

#Charger input    
print ("Enter Current Charger")
response = None
while response not in {"SC-G", "QS", "BOSCA", "OFF", "OTHER"}:
    response = input("Please enter one: 'SC-G', 'QS', 'Bosca', 'off', 'other'")
    response = response.upper()
    if response == "OTHER":
        explain = input("Please explain")
        ch = response + ":" + explain
    else:
        ch = response 

#Location
print ("Enter Current Location")
response = None
while response not in {"RACK1", "RACK2", "RACK3", "RACK4", "EV001", "EV002", "EV003", "EV004", "FLOOR", "OTHER"}:
    response = input("Please enter one: 'Rack 1 - 4', 'EV001 - 004', 'Floor' or 'other'")
    response = response.upper()
    if response == "OTHER":
        explain = input("Please explain")
        lo = response + ":" + explain
    else:
        lo = response    

#Voltage        
done = False
while not done:
    choice = (float(input("Enter Current Voltage:")))
    modchoice = choice * 10
    if(modchoice in range(500,700)):
        vo = choice
        done = True
    else:
        print('Sorry, selection must be between 50 and 70')
        
import csv

#add inputs to current battery dataframe
with open(cbat, "a") as clog:
    log_app = csv.writer(clog)
    log_app.writerow([cy,ch,lo,vo])

