for i in range(1):
    env = input("To check if you are eligible to make the chnage enter you current env: ")
    if env == "prod":
        print("This is Prod environment and a CR is needed for change")
    elif env == "qa":
        print("This is QA environment and a snow request is needed for change")
    else:
        print("This is Dev/test environment and can proceed with change")


gas = int(input("Enter your current gas %: "))
while gas != 100:
    print("Refill the tank")
    break
