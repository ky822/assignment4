alist=[1,2,3,4,5,6,7,8,9]

#statement

b=alist[:4]*4 
b[b.index(2)]=3#replace the 2 with 3
b.sort()

print b
