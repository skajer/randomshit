def register():

    account_name = print("Enter username: ")
    account_name = input()
    print(account_name)
    print("\n")

    pass1 = print("Enter password: ")
    pass1 = input()
    print(pass1)
    print("\n")

    pass2 = print("Repeat password")
    pass2= input()
    print(pass2)
    print("\n")


    while True:
        if pass1 == pass2:
            print("Successfully registered")
            break

        if pass1 == pass2:
            print("Hasło się zgadza")
            print(input())
            print("\n")
            break

        else:
            wrongpass = input(print("Password is wrong, try again:"))
            pass


            if wrongpass == pass1:
                print("Successfully registered")
                break

    zpw = open("logst","w+")
    zpw.write("username: \n")
    zpw.write(account_name)
    zpw.write("\n")
    zpw.write("\n")
    zpw.write("password: \n")
    zpw.write(pass1)
    zpw.write("\n")
    zpw.write("\n")
    zpw.close()

register()