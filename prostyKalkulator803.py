# Prosty kalkulator w Pythonie DUC ANH DINH S25002


# Funkcja dodawania
def dodawanie(x, y):
    return x + y

# Funkcja odejmowania
def odejmowanie(x, y):
    return x - y

# Funkcja mnożenia
def mnozenie(x, y):
    return x * y

# Funkcja dzielenia
def dzielenie(x, y):
    return x / y

# Funkcja potęgowania
def potega(x, y):
    return x ** y

# Funkcja konwersji z binarnego na dziesiętny system
def bin_na_dec(x):
    liczba = 0
    for cyfra in str(x):
        liczba = liczba * 2 + int(cyfra)
    return liczba

print("Wybierz działanie.")
print("1. Dodawanie")
print("2. Odejmowanie")
print("3. Mnożenie")
print("4. Dzielenie")
print("5. Potęgowanie")
print("6. Konwersja z binarnego na dziesiętny system")

# Pobierz wybór od użytkownika
wybor = input("Wybierz (1/2/3/4/5/6): ")

# Wykonaj odpowiednie działanie
if wybor in ['1', '2', '3', '4']:
    # Pobierz dane od użytkownika
    liczba1 = float(input("Podaj pierwszą liczbę: "))
    liczba2 = float(input("Podaj drugą liczbę: "))

    # Wykonaj wybrane działanie i wyświetl wynik
    if wybor == '1':
        print(liczba1, "+", liczba2, "=", dodawanie(liczba1, liczba2))

    elif wybor == '2':
        print(liczba1, "-", liczba2, "=", odejmowanie(liczba1, liczba2))

    elif wybor == '3':
        print(liczba1, "*", liczba2, "=", mnozenie(liczba1, liczba2))

    elif wybor == '4':
        print(liczba1, "/", liczba2, "=", dzielenie(liczba1, liczba2))

elif wybor == '5':
    # Pobierz dane od użytkownika
    liczba1 = float(input("Podaj liczbę: "))
    liczba2 = int(input("Podaj potęgę: "))

    # Wykonaj potęgowanie i wyświetl wynik
    print(liczba1, "^", liczba2, "=", potega(liczba1, liczba2))

elif wybor == '6':
    # Pobierz dane od użytkownika
    liczba_binarna = input("Podaj liczbę binarną: ")

    # Wykonaj konwersję i wyświetl wynik
    print(liczba_binarna, "w systemie dziesiętnym to", bin_na_dec(liczba_binarna))

else:
    print("Nieprawidłowe dane")
