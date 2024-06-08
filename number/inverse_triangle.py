# 5
# 4 4
# 3 3 3
# 2 2 2 2
# 1 1 1 1 1

# 5
# 5 4
# 5 4 3
# 5 4 3 2
# 5 4 3 2 1

# 5 5 5 5 5
#   4 4 4 4
#     3 3 3
#       2 2
#         1

# 5 4 3 2 1
#   5 4 3 2
#     5 4 3
#       5 4
#         5

n = int(input("Enter input : "))

print("Same number in row : ")
for i in range (1, n+1):
    for j in range(1, i+1):
        print(n-i+1, end=" ")
    print()

print("Same number in column : ")
for i in range (1, n+1):
    for j in range(1, i+1):
        print(n-j+1, end=" ")
    print()

print("inverse, reverse - same number in row : ")
for i in range (1, n+1):
    print("  "*(i-1),end="")
    for j in range(1, n-i+2):
        print(n-i+1, end=" ")
    print()

print("inverse, reverse - same number in column : ")
for i in range (1, n+1):
    print("  "*(i-1),end="")
    for j in range(1, n-i+2):
        print(n-j+1, end=" ")
    print()