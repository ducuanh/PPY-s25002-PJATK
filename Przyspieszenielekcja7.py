#zadanie 1
class Product:
    def __init__(self, name, price, category, quantity):
        self.name = name
        self.price = price
        self.category = category
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} ({self.category}) - {self.price} PLN - Ilość: {self.quantity}"


class SimpleFoodDatabase:
    def __init__(self):
        self.products = []

    def add_product(self, name, price, category, quantity):
        new_product = Product(name, price, category, quantity)
        self.products.append(new_product)

    def remove_product(self, name):
        for product in self.products:
            if product.name == name:
                self.products.remove(product)
                print(f"{name} został usunięty z bazy.")
                return
        print(f"{name} nie został znaleziony w bazie.")

    def search_product(self, name):
        for product in self.products:
            if product.name == name:
                print(product)
                return
        print(f"{name} nie został znaleziony w bazie.")

    def display_all_products(self):
        for product in self.products:
            print(product)


if __name__ == "__main__":
    database = SimpleFoodDatabase()

    database.add_product("Chleb", 3.5, "Pieczywo", 100)
    database.add_product("Mleko", 2.2, "Nabiał", 50)
    database.add_product("Jajka", 8.0, "Nabiał", 30)

    database.display_all_products()

    database.search_product("Mleko")

    database.remove_product("Jajka")
    database.display_all_products()

#zadanie 2
import heapq


class Graph:
    def __init__(self):
        self.nodes = {}
        self.edges = {}

    def add_node(self, node):
        self.nodes[node] = []
        self.edges[node] = {}

    def add_edge(self, node1, node2, weight):
        self.nodes[node1].append(node2)
        self.nodes[node2].append(node1)
        self.edges[node1][node2] = weight
        self.edges[node2][node1] = weight


class DijkstraAlgorithm:
    def __init__(self, graph):
        self.graph = graph

    def shortest_path(self, start, end):
        distances = {node: float('infinity') for node in self.graph.nodes}
        distances[start] = 0

        priority_queue = [(0, start)]
        visited = set()

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            if current_node in visited:
                continue

            visited.add(current_node)

            if current_node == end:
                return current_distance

            for neighbor in self.graph.nodes[current_node]:
                distance = current_distance + self.graph.edges[current_node][neighbor]

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return None


if __name__ == "__main__":
    graph = Graph()

    nodes = ['A', 'B', 'C', 'D', 'E', 'F']
    edges = [
        ('A', 'B', 4),
        ('A', 'C', 2),
        ('B', 'C', 1),
        ('B', 'D', 5),
        ('C', 'D', 8),
        ('C', 'E', 10),
        ('D', 'E', 2),
        ('D', 'F', 6),
        ('E', 'F', 3),
    ]

    for node in nodes:
        graph.add_node(node)

    for edge in edges:
        graph.add_edge(*edge)

    dijkstra = DijkstraAlgorithm(graph)
    shortest_distance = dijkstra.shortest_path('A', 'F')
    print("Najkrótsza odległość między A i F wynosi:", shortest_distance)
#zadanie3

class Osoba:
    osoby = []

    def __init__(self, imie, nazwisko, plec, data_urodzenia):
        self.imie = imie
        self.nazwisko = nazwisko
        self.plec = plec
        self.data_urodzenia = data_urodzenia
        Osoba.osoby.append(self)

    def wyswietl_info(self, format='dict'):
        if format == 'list':
            return [self.imie, self.nazwisko, self.plec, self.data_urodzenia]
        elif format == 'tuple':
            return (self.imie, self.nazwisko, self.plec, self.data_urodzenia)
        else:
            return {
                'imie': self.imie,
                'nazwisko': self.nazwisko,
                'plec': self.plec,
                'data_urodzenia': self.data_urodzenia,
            }

    @classmethod
    def wyswietl_osoby(cls):
        return [osoba.wyswietl_info() for osoba in cls.osoby]


class Gracz(Osoba):
    gracze = []

    def __init__(self, imie, nazwisko, plec, data_urodzenia, nick, typ, email):
        super().__init__(imie, nazwisko, plec, data_urodzenia)
        self.nick = nick
        self.typ = typ
        self.email = email
        Gracz.gracze.append(self)

    def wyswietl_info(self, format='dict'):
        osoba_info = super().wyswietl_info(format)
        if format == 'list':
            return osoba_info + [self.nick, self.typ, self.email]
        elif format == 'tuple':
            return osoba_info + (self.nick, self.typ, self.email)
        else:
            osoba_info.update({
                'nick': self.nick,
                'typ': self.typ,
                'email': self.email,
            })
            return osoba_info

    @classmethod
    def wyswietl_graczy(cls):
        return [gracz.wyswietl_info() for gracz in cls.gracze]


if __name__ == "__main__":
    osoba1 = Osoba("Jan", "Kowalski", "M", "1990-01-01")
    osoba2 = Osoba("Anna", "Nowak", "F", "1995-03-15")

    print("Informacje o osobach:")
    for osoba in Osoba.osoby:
        print(osoba.wyswietl_info())

    gracz1 = Gracz("Marek", "Zieliński", "M", "2000-05-10", "M4r3k", "Human", "marek@przyklad.pl")
    gracz2 = Gracz("Ewa", "Kowalczyk", "F", "2002-07-20", "EwkaGamer", "Human", "ewa.gamer@przyklad.pl")

    print("\nInformacje o graczach:")
    for gracz in Gracz.gracze:
        print(gracz.wyswietl_info())
