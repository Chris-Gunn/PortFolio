print('''
Welcome to UniBuddy! Your all-in-one app that makes your freshman journey a
bit easier to navigate.

Please enter your credentials to get started.
''')

name = input("What is your name? ").title()
age = int(input("How old are you? "))
colour = input("What's your favourite colour? ").capitalize()

print(f"""
Welcome {name}! Is see that your favourite colour is {colour}.
I have a few suggestions based on your choice.
""")

if colour == 'Red':
    print("If you like the colour RED, I have the following suggestions for you! ")

    print("""
1. Our red colour themed football club
2. Our labour society
3. Our vampire themed club
4. Our martial arts club
    """)

elif colour == 'Blue':
    print("If you like the colour BLUE, I have the following suggestions for you! ")

    print("""
1. Our swimming club
2. Our conservative society
3. Our sailing club
4. Our cooking club
    """)

elif colour == 'Green':
    print("If you like the colour GREEN, I have the following suggestions for you! ")

    print("""
1. Our climate change society
2. Our golf club
3. Our Guinness drinking club 
4. Our cycling club
    """)

else:
    print("We may not have what you are looking for.")

if age <= 22:

    print("Here are some fresher clubs you could join!")

else:
    print("Here are some event suggestions that could interest you!")

