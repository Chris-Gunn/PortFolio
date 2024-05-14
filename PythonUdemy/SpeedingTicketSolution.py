def speeding(is_birthday,speed):
    if is_birthday:
        speed = speed - 5
    else:
        speed = speed
    if speed > 80:
        return "Big ticket"
    elif speed > 60:
        return "Small ticket"
    else:
        return "No Ticket"

print(speeding(True, 65))






