name = input("Enter contact name: ")
phone = input("Enter phone number: ")

with open("contacts.txt", "a") as file:
    file.write(name + " - " + phone + "\n")

print("Contact saved.")
