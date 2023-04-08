#Addison Olstad
#CSCI 102 - Section G
#Assessment 11
#References: None
#Time: 15 minutes

import math

def print_output(string):
    print(f'OUTPUT {string}')

def cylinder_vol(radius, height):
    volume = 3.1415 * (radius ** 2) * height
    volume = f'{volume:.2f}'
    print_output(volume)

def lbs_to_kg(pounds):
    kg = pounds * 0.4536
    kg = f'{kg:.4f}'
    print_output(kg)

def polar_coords(x,y):
    r = math.sqrt((x**2) + (y**2))
    r = f'{r:.2f}'
    theta = math.degrees(math.atan(y/x))
    theta = f'{theta:.2f}'
    string_r = "r: "
    string_t = "theta: "
    string_r += r
    string_t += theta
    print_output(string_r)
    print_output(string_t)

def yen_to_dollars(yen):
    dollars = yen * 0.0068
    dollars = f'{dollars:.2f}'
    print_output(dollars)

def quad_form(a,b,c):
    root1 = (-(b) - math.sqrt((b**2)-(4*a*c))) / (2*a)
    root2 = (-(b) + math.sqrt((b**2)-(4*a*c))) / (2*a)
    root1 = int(root1)
    root2 = int(root2)
    print_output(root1)
    print_output(root2)
