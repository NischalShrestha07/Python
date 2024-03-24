# WAP TO OPEN AND WRITE  "hi python" for existing file
filePath = "newFile.txt"

with open(filePath, 'w') as file:
    file.write("hi python !!")

print(f"'hi python' has been written to {filePath}.")
