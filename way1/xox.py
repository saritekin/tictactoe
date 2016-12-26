""" 
  xox
|7|8|9|
|4|5|6|
|1|2|3|

"""

import random

f=open('dbs','r+')

arr=[]
arr2=[]
arr3=[]

for i in range(1,5):
	arr.append(i)

#print(arr[0:])
def allscenario():
	for i in range(24):
		random.shuffle(arr)
		while arr in arr2:
			random.shuffle(arr)
		if len(arr2) == 24:
			break
		arr2.append(arr[0:])
	#print(arr2[0:])
	f.write(str(arr2[0:]))
	




allscenario()


#print(arr2[0:])
























