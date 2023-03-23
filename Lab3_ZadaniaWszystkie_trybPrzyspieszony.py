#DinhDucAnhs25002

#zadanie 1 z przyśpieszonej
# Prośba o wprowadzenie danych przez użytkownika

name = input("Proszę podać swoje imię: ")
birthdate = input("Proszę podać swoją datę urodzenia w formacie RRRR-MM-DD: ")
email = input("Proszę podać swój adres e-mail: ")
phone_number = input("Proszę podać swój numer telefonu: ")

# Tworzenie listy, krotki i słownika z danymi użytkownika
user_list = [name, birthdate, email, phone_number]
user_tuple = (name, birthdate, email, phone_number)
user_dict = {'Imię': name, 'Data urodzenia': birthdate, 'E-mail': email, 'Numer telefonu': phone_number}

# Wyświetlenie danych użytkownika na ekranie
print("Twoje dane w postaci listy: ")
print(user_list)
print("\nTwoje dane w postaci krotki: ")
print(user_tuple)
print("\nTwoje dane w postaci słownika: ")
print(user_dict)
#---------------------------------------------------------------------------------------------------
#zadanie 2 z przyśpieszonej
import math

#liczba z zakresu od -20 do 20
numbers = []
for i in range(20):
    number = int(input(f"Podaj liczbę {i+1}/20 z zakresu [-20,20]: "))
    if number < -20 or number > 20:
        print("Liczba spoza zakresu! Wprowadź jeszcze raz.")
        i -= 1
    else:
        numbers.append(number)

# 1. utworzenie kopii listy
numbers_copy = numbers.copy()

# 2. znalezienie liczb pierwszych i utworzenie krotki
prime_numbers = []
for number in numbers_copy:
    if number > 1:
        is_prime = True
        for i in range(2, int(math.sqrt(number))+1):
            if number % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(number)
prime_numbers_tuple = tuple(prime_numbers)

# 3. podniesienie do potęgi 2 liczby podzielne przez 2 i utworzenie krotki
squared_numbers = []
for number in numbers_copy:
    if number % 2 == 0:
        squared_numbers.append(number ** 2)
squared_numbers_tuple = tuple(squared_numbers)

# 4. zamiana liczb podzielnych przez 2 na literę A w oryginalnej liście
for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        numbers[i] = 'A'

# wyświetlenie wyników
print("Lista pierwotna:", numbers)
print("Kopia listy:", numbers_copy)
print("Liczby pierwsze:", prime_numbers_tuple)
print("Liczby podzielne przez 2 podniesione do kwadratu:", squared_numbers_tuple)
#--------------------------------------------------------------------------------------
#zadanie 3 z przyszpieszonej
import numpy as np
#zadanie zrobione poprzez broadcasting
ainput = int(input("podaj wymiar 1 tablicy "))
a = np.arange(1, ainput)
b = np.arange(1, ainput)

table = np.multiply.outer(a, b)

print(table);

#-------------------
#zadanie 4 z przyśpieszonej listy
def catalan_number(n):
    if n == 0:
        return 1
    else:
        return (4*n-2)/(n+1) * catalan_number(n-1)

number = int(input("Podaj liczbę: "))

# wypisujemy wszystkie liczby Catalana mniejsze od podanej przez użytkownika
for n in range(number):
    catalan_n = catalan_number(n)
    if catalan_n < number:
        print(f"Liczba Catalana dla n={n} wynosi: {catalan_n:.0f}")

#zadanie 5 z przyśpieszonej listy
# tworzymy listę produktów
products = []


# definiujemy klase produktu
class Product:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price


# definiujemy funkcję do wyświetlania listy produktów
def display_products():
    print("Nr\tNazwa produktu\tIlość\tCena")
    for index, product in enumerate(products):
        print(f"{index}\t{product.name}\t{product.quantity}\t{product.price}")


# definiujemy funkcję do dodawania produktu do listy
def add_product():
    name = input("Podaj nazwę produktu: ")
    quantity = int(input("Podaj ilość produktu: "))
    price = float(input("Podaj cenę produktu: "))
    products.append(Product(name, quantity, price))
    print("Produkt został dodany!")


# definiujemy funkcję do usuwania produktu z listy
def remove_product():
    display_products()
    index = int(input("Podaj numer produktu do usunięcia: "))
    del products[index]
    print("Produkt został usunięty!")


# definiujemy funkcję do modyfikacji produktu
def edit_product():
    display_products()
    index = int(input("Podaj numer produktu do edycji: "))
    product = products[index]
    name = input("Podaj nową nazwę produktu: ")
    quantity = int(input("Podaj nową ilość produktu: "))
    price = float(input("Podaj nową cenę produktu: "))
    product.name = name
    product.quantity = quantity
    product.price = price
    print("Produkt został zmodyfikowany!")


# definiujemy funkcję główną
def main():
    while True:
        option = input("Wybierz opcje [d - dodaj, u - usuń, e - edytuj, w - wyświetl, q - zakończ]: ")
        if option == 'd':
            add_product()
        elif option == 'u':
            remove_product()
        elif option == 'e':
            edit_product()
        elif option == 'w':
            display_products()
        elif option == 'q':
            break
        else:
            print("Błędna opcja!")


if __name__ == "__main__":
    main()

