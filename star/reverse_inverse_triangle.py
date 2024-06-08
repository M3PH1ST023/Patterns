# *****
#  ****
#   ***
#    **
#     *

n = int(input("Enter input : "))

print("With space : ")
for i in range(1, n+1):
    print("  "*(i-1) + "* "*(n-i+1))

print("Without space : ")
for i in range(1, n+1):
    print(" "*(i-1) +"*"*(n-i+1))