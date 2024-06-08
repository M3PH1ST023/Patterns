#     1
#    1 2
#   1 2 3
#  1 2 3 4
# 1 2 3 4 5

#     1
#    2 3
#   4 5 6
#  7 8 9 10
# 11 12 13 14 15

n = int(input("Enter input : "))

print("Equilateral triangle similar row pattern : ")
for i in range(1, n+1):
    print(" "*(n-i), end="")
    for j in range(1, i+1):
        print(j,end=" ")
    print()

print("Equilateral triangle incremental pattern : ")
temp = 1
for i in range(1, n+1):
    print(" "*(n-i), end="")
    for j in range(1, i+1):
        print(temp,end=" ")
        temp+=1
    print()