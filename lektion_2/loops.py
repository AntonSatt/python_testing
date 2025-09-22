import sys

app_is_running = True

while app_is_running == True:
    print("Menu 1")
    print("Menu 2")

    menu_choice = input("Vilken menu? ")

    if (menu_choice == "1"):
        print("Menu 1 vald!")
        sys.exit() 
    elif (menu_choice == "2"):
        print("Menu 2 vald!")
        sys.exit() 
    else:
        print("Inkorrekt val!")

       