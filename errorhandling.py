#Error Handling Lab 🧪: Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.
try:
    fileName = input("Enter file name/file path: ")
    file = open(fileName, "r")
    data = file.read()
    print("File successfully read/ found")
except FileNotFoundError:
    print("File not found/ File cant be read")
finally:
    file.close()