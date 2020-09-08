print("hello world 0831")

list_square=[]
for i in range(1,4):
    list_square.append(i**2)
print(list_square)



list_square2 = [i**2 for i in range(1,4)]
print(list_square2)


a = {1,2,3,3}
b= {4,3,1}
print(a.union(b))
a.add(6)
print(a)
