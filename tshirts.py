# This is a program that takes input from you to take an order for customized t-shirts.

def make_shirts():
    """This will make the shirt with a custom size and message."""
    listOfSizes = ['s', 'm', 'l', 'xl', 'xxl']
    active = True

    while active:

        print("\n(enter 'q' to exit any time)")
        size = input("What size of t-shirt do you want?(S/M/L/XL/XXL): ")

        if size == 'q':
            print("\nThanks for visiting:)")
            break
        if size.lower() not in listOfSizes:
            print("\nPlease choose correct size (S/M/L/XL/XXL).")
            continue

        print("\n(enter 'q' to exit any time)")
        message = input("What do you want to be printed on your t-shirt: ")
        if message == 'q':
            print("\nThanks for visiting.:)")
            break

        print("\nThis is to confirm your order that you want a tshirt of size: " + size.title().upper() + " and the message printed should be: " + message)
        
        confirmation = input("\nPress y to confirm and n to rechoose your order. Press q to quit ")
        active_2 = True

        while active_2:
           
            if confirmation == "y":
                print("\nThanks for your order.:)") 
                active = False
                active_2 = False

            elif confirmation == "n":
                print("\nPlease choose your order again: ")
                active_2 = False

            elif confirmation == "q":
                print("\nThanks for visiting:)")
                active = False
                active_2 = False
                
            else:
                confirmation = input("\nChoose only 'y'/'n'/'q' for yes, no and quit respectively: ")
                continue
make_shirts()