with open("notes.txt", "a") as file:
    text = input("Enter text to append: ")
    file.write("\n" + text)

print("Text appended successfully.")
