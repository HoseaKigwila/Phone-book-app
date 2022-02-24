menu = """
Electronic Phone Book
=====================
1. Look up an entry
2. Set an entry
3. Delete an entry
4. List all entries
5. Quit 
"""

print(menu) 

selected_option = input("what do you want to do (1-5)?")

if selected_option == "2":
    name = input("what is the contact's name?")
    phone_number = input("what is their phone number?")