import numpy as np 
import time 
import random as rd
import matplotlib.pyplot as plt 

def init_array():
    arr = []
    for i in range(10, 5000000, rd.randint(100000,300000)):
        arr.append(i)
    rd.shuffle(arr)
    return arr

def print_array(arr = []):
    n = 0
    for i in arr:
        print[n]
        n=+1

array = []
array = init_array()
print_array(array)


    
# for i in range(10, 5000000, rd.randint(10000,30000)): 
#     element_counts.append(i) 
   
#     big_np_array = np.random.sample(i)
#     start = time.time() 
#     np.sort(big_np_array) 
#     end = time.time() - start 
#     np_times.append(end) 
   
#     big_lists_array = [] 
#     for j in range(i): 
#         big_lists_array.append(random.random()) 
#     start = time.time() 
#     big_lists_array.sort() 
#     end = time.time() - start 
#     list_times.append(end)
 
# plt.plot(element_counts, np_times, label='NumPy') 
# plt.plot(element_counts, list_times, label='Lists') 
# plt.xlabel('Номер элемента') 
# plt.ylabel('Время (с)') 
# plt.grid() 
# plt.legend() 
# plt.show()