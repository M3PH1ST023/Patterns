#     *
#    ***
#   *****
#  *******
# *********

n = int(input("Enter input : "))

print("With space : ")
print( "  "*(n-1) + "*")
for i in range(1, n):
    print("  "*(n-i-1) +"* "*(i*2+1))

print("Without space : ")
print(" "*(n-1) + "*")
for i in range(1, n):
    print(" "*(n-i-1) +"*"*(i*2+1))