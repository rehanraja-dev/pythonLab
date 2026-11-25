# print("START")
# print("Enter X and Y for Devision")
# x = int(input())
# y = int(input())
# z = x / y
# print("End")



# print("START")
# print("Enter X and Y for Devision")
# x = int(input())
# y = int(input())
# try:
#     z = x / y
# except ZeroDivisionError as e:
#     print(e)
# print("End")


# def Divide(x,y):
    
#     try:
#         z = x / y
#         print(z)
#     except ZeroDivisionError as e:
#         print(e)


# print("START")
# print("Enter X and Y for Devision")
# Divide(13,5)
# Divide(15,5)
# Divide(13,0)
# Divide(33,5)
# Divide(13,5)
# Divide(13,0)
# Divide(13,5)
# print("End")


# s1 = "Hello India"

# try:
#     for i in range(len(s1)+3):
#         print(s1[i])
# except IndexError as e:
#     print(e)

# print("Normal Termination")


# print("START")
# print("Enter X and Y for Devision")

# try:
#     x = int(input())
#     y = int(input())
#     z = x / y
# except ZeroDivisionError as e:
#     print(e)

# except ValueError as e:
#     print(e)

# print("End")


print("START")

try:
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    print(x/y)
    L1 = [1,22,333,444]
    for i in range(10):
        print (L1[i])
except Exception as e:
    print(e)

print("End")