# # env = input("Enter your current env:")
# # print("My current env is:",env) 
# a=input("enter your first number: ")
# b=input("enter your second number: ")
# print(type(a), type(b))
# print("converting datatypes")
# c=int(a)
# d=int(b)
# print(type(c), type(d))
# print(type(a), type(b))
# print(a+b)
# print(c+d)

env = input("To check if you are eligible to make the chnage enter you current env: ")
if env == "prod":
    print("This is Prod environment and a CR is needed for change")
elif env == "qa":
    print("This is QA environment and a snow request is needed for change")
else:
    print("This is Dev/test environment and can proceed with change")

