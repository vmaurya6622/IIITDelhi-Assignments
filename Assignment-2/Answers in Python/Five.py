import time
start = time.time()
x=int(input("Enter the value of Cx : "))
y=int(input("Enter the value of Cy : "))
matrix=[[2,3,1],
        [4,6,1],
        [8,1,1],
        [5,3,1],
        [2,6,1]]

multipend=[[x,0,0],
        [0,y,0],
        [0,0,1]]


multiplication = []

for i in range(len(matrix)):
    k=[0,0,0]
    multiplication.append(k)


for i in range(len(matrix)):
    for j in range(len(multipend[0])):
        for k in range(len(multipend)):
            multiplication[i][j] += (matrix[i][k]) * (multipend[k][j])

coordinates=[] 
for i in multiplication:
    y=[i[0],i[1]]
    y=tuple(y)
    coordinates.append(y)
print(coordinates) 
end = time.time()
print("Total time elapsed to compute is ",end - start)   