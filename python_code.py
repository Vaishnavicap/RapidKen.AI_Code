node = int(input("Enter the number of nodes :"))
edges = 0
arr = []
sec = []
for i in range(0,2):
    col = []
    for j in range(node - 1):
        x = int(input())
        col.append(x)
        sec.append(x)
        if(x != sec[i]): 
            edges = edges + 1 
    arr.append(col)
print(arr)
print(edges)
