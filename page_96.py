# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 12:42:52 2022

@author: Mugdho
"""


bd_division_info={}
bd_division_info["Barishal"]={"district":6,"upazila":39,"union":333}
bd_division_info["Chittagong"]={"district":11,"upazila":97,"union":336}
bd_division_info["Dhaka"]={"district":13,"upazila":93,"union":1833}
bd_division_info["Khulna"]={"district":10,"upazila":59,"union":270}
bd_division_info["Mymensingh"]={"district":4,"upazila":34,"union":350}
bd_division_info["Rajshahi"]={"district":8,"upazila":70,"union":558}
bd_division_info["Rangpur"]={"district":8,"upazila":58,"union":536}
bd_division_info["Sylhet"]={"district":4,"upazila":38,"union":334}

dist = sum(item["district"] for item in bd_division_info.values())
print("Number of District in Bangladesh is =", dist)
upz = sum(item["upazila"] for item in bd_division_info.values())
print("Number of Upazila in Bangladesh is =", upz)    
uno = sum(item["union"] for item in bd_division_info.values())
print("Number of union in Bangladesh is =", uno)
  # extra
#dict to list  
t = bd_division_info.items()
print(t)
z = list(t)
print(z)
