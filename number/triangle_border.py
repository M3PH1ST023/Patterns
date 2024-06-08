# 1 2 3 4 5
# 2     5
# 3   5
# 4 5
# 5

# 1 2 3 4 5
#   2     5
#     3   5
#       4 5
#         5

n = int(input("Enter input : "))

print("triangle border : ")
for i in range(1, n+1):
    print (str(i)+" ", end="")
print()

if n>1:
    j = 0

    for i in range(2, n):
        print(str(i)+ (((n-2)*2-1) - j)* " "+str(n))
        j+=2

    print(n)

print("reverse triangle border : ")
for i in range(1, n+1):
    print (str(i)+" ", end="")
print()

if n>1:
    j = 0

    for i in range(2, n):
        print("  "*(i-1), end="")
        print(str(i)+ (((n-2)*2-1) - j)* " "+str(n))
        j+=2

    print("  "*(n-1)+str(n))