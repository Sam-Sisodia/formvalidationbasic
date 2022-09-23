from django.test import TestCase

# Create your tests here.
print("helo")

# a= 10000
# b = 50
# c = 200

# if a>b and a>c:
#     print("A is gater ",a)

# elif b>a and b>c :
#     print("B is grater",b)

# else:
#     print("c is grater",c)




for  i in range(1,6):
    for k in range(1,6-i):
        print(" ",end="" )
    for  j in range(1,6-i):
        print("*" , end=" ")
    print()