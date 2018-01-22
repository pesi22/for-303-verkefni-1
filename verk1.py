
phone_numbers = {"petur":"8978220","addy":"8927178"}


user_get_name = input("whats the Name: ")
comp_echo_number = phone_numbers.get(user_get_name,"")
if comp_echo_number == "":

    print("This number is not in the phone book !" + " would you like to add them to the phone book ? if so press y:n")
    add_input = input()
    print(add_input)

    if add_input == "y":
        add_input_number = input("what is " + user_get_name + "'s phone number ? ")
        phone_numbers.update({user_get_name:add_input_number})
        print(user_get_name + "'s phone number has been added to the phone book !")
        print(phone_numbers)

else:
    print(user_get_name + "'s phone number is " + comp_echo_number)
    edk_input = input("would you like to edit or delete this number if so press e:d:k (edit, delete, keep) ")

    if edk_input == "e":
        edk_edit_number = input("what is " + user_get_name + "'s new phone number ? ")
        phone_numbers[user_get_name] = edk_edit_number
        print(user_get_name + " number has been changed ")
        print(phone_numbers)

    elif edk_input == "d":
        del phone_numbers[user_get_name]
        print(user_get_name + " has been deleted from the phone book ")
        print(phone_numbers)

    elif edk_input == "k":
        print(user_get_name + " has not been changed ")
        print(phone_numbers)








