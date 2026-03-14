with open("notes.txt", "w") as file:
    text = input("Enter text to save: ")
    file.write(text)

print("Text saved successfully.")
