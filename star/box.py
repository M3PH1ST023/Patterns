# *****
# *   *
# *   *
# *   *
# *****

n = int(input("Enter input : "))

print("With space : ")
print("* "*n)
for i in range(1, n-1):
    print("* "+ "  "*(n-2)+"*")
print("* "*n)

print("Without space : ")
print("*"*n)
for i in range(1, n-1):
    print("*"+ " "*(n-2)+"*")
print("*"*n)