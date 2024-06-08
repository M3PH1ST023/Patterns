# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

n = int(input("Enter input : "))

print("Same numbers in a row : ")
for i in range(1, n+1):
    for j in range(1, i+1):
        print(i, end=" ")
    print()

print("Same numbers in a column : ")
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()