#Dinh Duc Anh s25002 lista przyśpieszona 6
#zadanie 1
def liczby_doskonale(*args):
    def jest_doskonala(liczba):
        suma_dzielnikow = sum(dzielnik for dzielnik in range(1, liczba) if liczba % dzielnik == 0)
        return suma_dzielnikow == liczba

    wynik = {}
    for liczba in args:
        wynik[liczba] = jest_doskonala(liczba)
    return wynik
  
  #zadanie 2
  from math import factorial

def liczby_catalana(N, filtr='a'):
    def catalan(n):
        return factorial(2 * n) // (factorial(n + 1) * factorial(n))

    def parzysta(x):
        return x % 2 == 0

    def nieparzysta(x):
        return x % 2 != 0

    filtr_funkcji = {
        'p': parzysta,
        'n': nieparzysta,
        'a': lambda x: True
    }

    filtr_funkcja = filtr_funkcji.get(filtr.lower(), lambda x: True)

    i = 0
    liczba_catalana = catalan(i)
    while liczba_catalana < N:
        if filtr_funkcja(liczba_catalana):
            print(liczba_catalana)
        i += 1
        liczba_catalana = catalan(i)
    #zadnie 3
    def sito_eratostenesa(n):
    liczby = [True] * (n + 1)
    p = 2
    while p**2 <= n:
        if liczby[p]:
            for i in range(p**2, n + 1, p):
                liczby[i] = False
        p += 1
    return [x for x in range(2, n + 1) if liczby[x]]

def liczby_pierwsze(limit=75):
    n = 2
    while True:
        if len(sito_eratostenesa(n)) >= limit:
            break
        n += 1
    return sito_eratostenesa(n)[:limit]

pierwsze_75 = liczby_pierwsze()
print(pierwsze_75)
# zadanie 4
def liczby_podzielne(n, rosnaco=True):
    liczba = 1
    licznik = 0
    wynik = []

    while licznik < n:
        if liczba % 2 == 0 and liczba % 3 != 0:
            wynik.append(liczba)
            licznik += 1
        liczba += 1

    wynik.sort(key=lambda x: x, reverse=not rosnaco)
    return wynik
#zadanie 5
def dodaj_produkt(baza, produkt, cena):
    baza[produkt] = cena

def usun_produkt(baza, produkt):
    if produkt in baza:
        del baza[produkt]
    else:
        print("Produkt nie istnieje w bazie.")

def wyswietl_produkty(baza):
    print("Produkty w bazie:")
    for produkt, cena in baza.items():
        print(f"{produkt}: {cena}")

def aktualizuj_produkt(baza, produkt, nowa_cena):
    if produkt in baza:
        baza[produkt] = nowa_cena
    else:
        print("Produkt nie istnieje w bazie.")

def menu():
    baza = {}

    while True:
        print("\nMenu:")
        print("1. Dodaj produkt")
        print("2. Usuń produkt")
        print("3. Wyświetl produkty")
        print("4. Aktualizuj cenę produktu")
        print("5. Wyjdź")

        wybor = input("Wybierz opcję: ")

        if wybor == "1":
            produkt = input("Podaj nazwę produktu: ")
            cena = float(input("Podaj cenę produktu: "))
            dodaj_produkt(baza, produkt, cena)

        elif wybor == "2":
            produkt = input("Podaj nazwę produktu do usunięcia: ")
            usun_produkt(baza, produkt)

        elif wybor == "3":
            wyswietl_produkty(baza)

        elif wybor == "4":
            produkt = input("Podaj nazwę produktu do aktualizacji: ")
            nowa_cena = float(input("Podaj nową cenę produktu: "))
            aktualizuj_produkt(baza, produkt, nowa_cena)

        elif wybor == "5":
            break

        else:
            print("Nieprawidłowy wybór, spróbuj ponownie.")

if __name__ == "__main__":
    menu()
#zadanie 6
import heapq

def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

if __name__ == "__main__":
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }

    distances = dijkstra(graph, 'A')
    print("Odległości od wierzchołka A do pozostałych wierzchołków:")
    for vertex, distance in distances.items():
        print(f"{vertex}: {distance}")
