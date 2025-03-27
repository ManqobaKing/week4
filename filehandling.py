#File Read & Write Challenge 🖋️: Create a program that reads a file and writes a modified version to a new file.

with open("newfile.txt", "r") as rfile:
    contents = rfile.read()
    with open("modified.txt", "w") as wfile:
        wfile.write(contents.upper() + "\n")
        wfile.write("AMEN.")
        
    print("newfile.txt was succesfully modified to modified.txt")




