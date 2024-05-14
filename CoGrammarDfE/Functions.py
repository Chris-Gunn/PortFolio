# ************ Example 7 ************
def put_number_in_list(num):
        newList = []
        newList.append(num)
        return newList

while True:
    num_choice = int(input("Choose a number: "))
    num_store = put_number_in_list(num_choice)
    again = input("Choose another number?").lower()
    if again == "yes":
        continue
    elif again == "no":
        print(num_store)
        break