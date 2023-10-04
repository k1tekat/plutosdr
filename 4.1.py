import numpy as np 
import time 
import random as rd
import matplotlib.pyplot as plt 

lower_Limit = 10
Upper_Limit = 500000000000
bottom_step = 10000
top_step = 30000

arr = []

for i in range(lower_Limit, Upper_Limit, rd.randint(bottom_step,top_step)): #preparing the array
    arr.append(i)
rd.shuffle(arr) #mix numbers

arr_size = len(arr)

arr_list = []
arr_np = np.array(arr_size) #init list and numpy array

arr_list = arr.copy()
arr_np = np.copy(arr) #copy arr in list and numpy array

start = time.time()
arr_np = np.sort(arr_np)
np_time = time.time() - start
print("np time:",
      (np_time) * 10**3, "ms")

start = time.time()
arr_list.sort()
list_time = time.time() - start
print("np time:",
      (list_time) * 10**3, "ms")
print("arrsize: ",arr_size,"/n")
plt.plot([0,arr_size], [0,(np_time * 10**3/1000)], label='NumPy') 
plt.plot([0,arr_size], [0,(list_time* 10**3/1000)], label='Lists') 
plt.xlabel('Номер элемента') 
plt.ylabel('Время (c)') 
plt.grid() 
plt.legend() 
plt.show()