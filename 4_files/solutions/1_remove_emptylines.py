# Napisz program, którzy otworzy plik tekstowy i zapisze dane z niego do innego pliku pomijając puste linie

with open("file_with_empty_lines.txt", "r") as input_file, \
    open("result.txt", "w") as output_file:
    for line in input_file:
        if len(line.strip()) != 0: # line != "\n"
            output_file.write(line)
