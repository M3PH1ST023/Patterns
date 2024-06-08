# *********
#  *******
#   *****
#    ***
#     *

n = int(input("Enter input : "))

print("With space : ")
for i in range(1, n):
    print("  "*(i-1) +"* "*(n*2-(i*2-1)))
print( "  "*(n-1) + "*")

print("Without space : ")
for i in range(1, n):
    print(" "*(i-1) +"*"*(n*2-(i*2-1)))
print(" "*(n-1) + "*")