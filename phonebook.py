hasQuit = False
phonebook = {}

menu = """
Electronic Phone Book
=====================
1. Look up an entry
2. Set an entry
3. Delete an entry
4. List all entries
5. Quit 
"""

while not(hasQuit):
    print(menu) 

    selected_option = input("what do you want to do (1-5)? ")

    if selected_option == "2":
        name = input("what is the contact's name? ")
        phone_number = input("what is their phone number? ")
        phonebook[name] = phone_number
        print("Contact added Successfully")
        print(menu)
    elif selected_option == "1":
        name = input("What contact's number would you like? ")
        print(phonebook[name])
        print(menu)
    elif selected_option == "3":
        name = input("What contact's number would you like to delete? ")
        phonebook.pop(phonebook[name], phone_number)      
    elif selected_option == "4":
        print(phonebook[name] + phonebook[name] )       
    elif selected_option =="5":
        hasQuit = True
    
        

