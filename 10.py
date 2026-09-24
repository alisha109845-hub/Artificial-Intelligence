#take input for rows and colunms
m=int(input("Enter Rows (m):"))
n=int(input("Enter Colunms (n):"))

#Create 2D array
arr=[]
for i in range(m):
    row=[]
    for j in range(n):
        row.append(i*j)
    arr.append(row)

print (arr)