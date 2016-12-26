from itertools import combinations
f=open('allcom','r+')

arr=[1,2,3,4,5,6,7,8,9]


def comb(data):
	if len(data) <= 1:
	    return [data]
	res = []
	for i, c in enumerate(data):
	    for r in comb(data[:i]+data[i+1:]):
	        res.append([c]+r)
	return res

#print(comb(arr))
f.write(str(comb(arr)))



