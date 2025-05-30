'''
Q. r1 = upper limit 1 (0,1)
   r2 = upper limit 2 (0,1,2)
   r3 = upper limit 1 (0,1)
sum should not == 2
   (0,0,0)(0,0,1)(0,1,0)(1.1.1)
'''
r1 = 1
r2 = 2
r3 = 1
res = [[i,j,k] for i in range(r1+1) for j in range(r2+1) for k in range(r3+1) if i+j+k != 2]
print(res)