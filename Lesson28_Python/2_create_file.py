with open("test.txt", "w") as file:
    file.write("This is a test file for programming homework")

with open("test.txt", "r") as file:
    content = file.read()
    print(content)