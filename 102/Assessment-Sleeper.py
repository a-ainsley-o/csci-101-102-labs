#Addison Olstad
#CSCI 101- Section C
#Python Assessment 1
#References: Got help from a compsci student about modules and while loops
#Time: 45 minutes

#Asking for inputs
#print("How many minutes early would you like your alarm to go off?")
early = int(input("EARLY> "))
#print("What time do you need to get out of bed?")
hours = int(input("HOURS> "))
minutes = int(input("MINUTES> "))

#military time.... 24 hours, but in minutes
spare_hours = early // 60
mminutes = early % 60

nhours = hours - spare_hours
nminutes = minutes - mminutes

#to compensate for turning the hours over
while nminutes < 0:
    nminutes += 60
    nhours -= 1
while nhours < 0:
    nhours += 24 

#for zero notation and for 0 entry
if early == 0:
    nminutes = minutes
    nhours = hours
if nhours < 10:
    nhours = "0" + str(nhours)
if nminutes < 10:
    nminutes = "0" + str(nminutes)
if nminutes == 0:
    nminutes = "00"
if nhours == 0:
    nhours = "00"

#printing results
#print("You should set your alarm for:" )
print("OUTPUT", nhours, nminutes)
