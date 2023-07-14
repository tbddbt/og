#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 21:48:14 2023

@author: asdss
"""
import numpy as np
import matplotlib.pyplot as plt

def cooordinates(s)
datas=[]
with open("/home/asdss/Documents/project1/KARD_a01_a02/a01_s01_e01_realworld.txt") as f:
    data = f.readlines()
    for row in data:
        datas.append([float(x) for x in row.split()])

plt.show()



#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 16:57:59 2023

@author: asdss
"""

import numpy as np
import matplotlib.pyplot as plt

def coordinates(s):
  datas=[]
  with open(s) as f:
     data = f.readlines()
  for row in data:
        datas.append([float(x) for x in row.split()])
        
  return datas

datas =coordinates("/home/asdss/Documents/project1/KARD_a01_a02/a01_s01_e01_realworld.txt")
print(datas[0:15])
