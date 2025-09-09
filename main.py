import time
from os import system, name

while True:
    choice = input("Do Yo Want To Start ? (y/n) :")
    if 'y' == choice.lower():
        hour = int(input("Enter Amount Of Hour :"))
        minutes = int(input("Enter Amount Of minutes :"))
        second = int(input("Enter Amount Of second :"))
        total = hour * 60 * 60 + minutes * 60 + second
        print("Timer Started Now ... ")
        time.sleep(1)
        while total >= 1:
            print(total)
            total = total - 1
            time.sleep(1)
            if name == "nt":
                system("cls")
            else:
                system("clear")
        print("Timer Ended ...")
    elif 'n' == choice.lower():
        print("Exiting ...")
    else:
        print("Invalid Input !!")
