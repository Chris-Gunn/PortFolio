# Request the user to give their age
age = int(input("How old are you? \n"))

# Check if the user is over 100 years
if age > 100:
    print("Sorry, you're dead.")
# Check if the user is 71 or over
elif age >= 71:
    print("You've finally stopped working, thank god!")
# Check if the user is 40 or over
elif age >= 40:
    print("You're over the hill.")
# Check if the user is under 13
elif age < 13:
    print("You qualify for the kiddie discount.")
# Check if the user is exactly 21
elif age == 21:
    print("Congrats on your 21st!")
# Check for any other number
else:
    print("Age is but a number")
