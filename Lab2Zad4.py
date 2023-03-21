binary = input("Podaj liczbę w systemie dwójkowym: ")
octal = input("Podaj liczbę w systemie ósemkowym: ")
hexadecimal = input("Podaj liczbę w systemie szesnastkowym: ")

decimal_binary = int(binary, 2)
decimal_octal = int(octal, 8)
decimal_hexadecimal = int(hexadecimal, 16)

print("Liczba w systemie dziesiętnym:")
print(f"Liczba binarna {binary} = {decimal_binary}")
print(f"Liczba ósemkowa {octal} = {decimal_octal}")
print(f"Liczba szesnastkowa {hexadecimal} = {decimal_hexadecimal}")
