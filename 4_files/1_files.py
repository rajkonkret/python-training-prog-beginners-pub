# Character Meaning
#     --------- ---------------------------------------------------------------
#     'r'       open for reading (default)
#     'w'       open for writing, truncating the file first
#     'x'       create a new file and open it for writing
#     'a'       open for writing, appending to the end of the file if it exists
#     'b'       binary mode
#     't'       text mode (default)
#     '+'       open a disk file for updating (reading and writing)
file = open("example_text.txt", "r")
print(file.readlines())
file.close()

# otwieranie pliku za pomocą context manager
with open("example_text.txt", "r") as file:
    print(file.readlines())


with open("example_text.txt", "r") as file:
    for line in file:
        print(line.strip())  # usuwa białe znaki ze stringa z początku i końca linii

with open("example_text.txt", "rb") as file:
    file_content: bytes = file.read()
    print(file_content)
    print(type(file_content))
    print(file_content[0])
    print(file_content[1])

with open("polish_letters.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())

with open("string.txt", "w") as file:
    lines = ["abc\n", "def\n"]
    file.writelines(lines)

with open("string.txt", "a") as file:
    lines = ["python", "can append", "to file"]
    for line in lines:
        file.write(line + "\n")

with open("polish_letters.txt", "r") as input_file:
    with open("result.txt", "w") as output_file:
        for line in input_file:
            output_file.write(line)


with open("polish_letters.txt", "r") as input_file, \
    open("result.txt", "w") as output_file:
    for line in input_file:
        output_file.write(line)
