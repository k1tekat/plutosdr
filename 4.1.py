import numpy as np 
import time 
import random as rd
import matplotlib.pyplot as plt 

lower_Limit = 10
Upper_Limit = 5000000
bottom_step = 100000
top_step = 300000


arr = []
arr_list = []
arr_np = []

for i in range(lower_Limit, Upper_Limit, rd.randint(bottom_step,top_step)): #init array
    arr.append(i)
    rd.shuffle(arr) #mix numbers
#arr = [1,56,214,12,2,12,4,45,6,4,3,1,8,6,4,3,1,555]

arr_size = len(arr)
print(arr_size,"\n")

print(arr)
print("\n")

arr_list = arr.copy()
arr_np = np.copy(arr)

print("list ",arr_list)
print("np ",arr_np)

# arr_list = arr
# arr_np = arr

start = time.time()
np.sort(arr_np)
np_time = time.time() - start
print(np_time)

start = time.time()
arr_list.sort()
list_time = time.time() - start
print(list_time)


print("list ",arr_list)
print("np ",arr_np)

plt.plot([0,arr_size], [0,np_time], label='NumPy') 
plt.plot([0,arr_size], [0,list_time], label='Lists') 
plt.xlabel('Номер элемента') 
plt.ylabel('Время (с)') 
plt.grid() 
plt.legend() 
plt.show()

    
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