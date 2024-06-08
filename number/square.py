# 1 1 1 1 1
# 2 2 2 2 2
# 3 3 3 3 3
# 4 4 4 4 4
# 5 5 5 5 5

# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5 
# 1 2 3 4 5
# 1 2 3 4 5

n = int(input("Enter input : "))

print("Square row : ")
for i in range(1, n+1):
    for j in range(1, n+1):
        print(i,end=" ")
    print()

print("Square column : ")
for i in range(1, n+1):
    for j in range(1, n+1):
        print(j,end=" ")
    print()