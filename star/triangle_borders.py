# *
# **
# * *
# *  *
# *****

n = int(input("Enter input : "))

print("*")
for i in range(1, n-1):
    print("*" + " "*(i-1) + "*")

print("*"*n)