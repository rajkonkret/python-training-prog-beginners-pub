# Napisz program, który wczyta pliki a.txt oraz b.txt i zapisze w pliku c.txt linie, które są
# obecne zarówno w a.txt jak i w b.txt (bez duplikatów).

with open("a.txt", "r") as file_A:
    file_A_lines: list[str] = file_A.readlines()

with open("b.txt", "r") as file_B:
    file_B_lines: list[str] = file_B.readlines()

with open("c.txt", "w") as file_C:
    lines: set[str] = {x for x in file_A_lines if x in file_B_lines}
    file_C.writelines(lines)
