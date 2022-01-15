#!/bin/python3
import math
import os
import random
import re
import sys
if __name__ == '__main__':
    arr = []
    a = []
    b = []
    c = []
    d = []
    e = []
    f = []
    g = []
    sums =[]
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
        if _ < 4 :
            a += arr[_][0:4]
            c += arr[_][2:6]
            b += arr[_][1:5]    
        if _ > 0 and _< 5:
            
            d += arr[_][1:5]
            
        if _ > 1:
            e += arr[_][0:4]
            f += arr[_][1:5]    
            g += arr[_][2:6]
    
    for i in range(0,16):
       sums.append(a[i] + b[i] + c[i] + d[i] + e[i] + f[i] + g[i])        
    print(max(sums))
  