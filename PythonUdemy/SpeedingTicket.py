birthday = input("Is it your birthday today? Print 'True' or 'False' \n")
speed = int(input("Do you know what speed you were going, sir? \n"))
def speeding(birthday,speed):
    if birthday == "True":
        speed = speed - 5
    if speed <= 60:
        print("No ticket")
    elif 61 <= speed <= 80:
        print("Small ticket")
    elif speed > 80:
        print("Big ticket")



speeding(birthday,speed)