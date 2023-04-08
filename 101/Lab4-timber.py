#Addison Olstad
#CSCI 101 - section C
#Python Lab 4
#References:
#Time:

#max of 20,000 acres of land are available in the area
#Reforestation equation for each year: (X * (1 + rate) )
    # x is the area of forest currently standing
#Year, int, 0-300
#Rate, float, 0-15
#acres, int, 0-20000

print("Input the number of years to print in the reforestation table:")
years = int(input("YEARS> "))

print("Input the reforestation rate as a percentage:")
rate = float(input("RATE> "))

print("Input the number of acres remaining after harvesting:")
st_acres = int(input("ACRES> "))

print("The reforestation table is:")
print("Year, # Acres, % of Forest")
per_forest = round(float((st_acres / 20000) * 100), 2)
print(f'OUTPUT 0, {st_acres:.1f}, {per_forest:.2f}%')

value = st_acres
for i in range(0, years, 1):
    new_rate = (rate / 100)
    if i == 0:
        end_acres = (st_acres * (1 + new_rate))
    else:
        end_acres = (value * (1 + new_rate))
    value += (end_acres - value)
    end_per = round(float((value / 20000) * 100), 2)
    print(f'OUTPUT {i+1}, {end_acres:.1f}, {end_per:.2f}%')

count = 0
while end_acres < 20000:
    new_rate = (rate / 100)
    if count == 0:
        end_acres = round((st_acres * (1 + new_rate)), 1)
    else:
        end_acres = round((value * (1 + new_rate)), 1)
    value += (end_acres - value)
    end_per = round(float((value / 20000) * 100), 2)
    count += 1
    

print("The number of years until complete reforestation is:")
print(f'OUTPUT {count}')
