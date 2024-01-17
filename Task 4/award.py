# Request the user to say what time they managed for swimming, cycling and running
swimming = int(input("How long did it take you to swim in minutes? \n"))
cycling = int(input("How long did it take you to cycle in minutes? \n"))
running = int(input("How long did it take you to run in minutes? \n"))

# The total time the user took complete all three disciplines and printed as a string in minutes
total_time = swimming + cycling + running
print(str(total_time) + " minutes")

# Checks if the user was able to get a time under 100 minutes
if total_time <= 100:
    print("You have been given the Provincial Colours award!")
# Checks if the user was able to get a time between than 100 and 105 minutes
elif (total_time > 100) and (total_time <= 105):
    print("You have been given the Provincial Half Colours award!")
# Checks if the user was able to get a time between than 105 and 110 minutes
elif (total_time > 105) and (total_time <= 110):
    print("You have been given the Provincial Scroll award!")
# Checks if the user went over the time limit of 110 minutes
else:
    print("You have not earned an award.")