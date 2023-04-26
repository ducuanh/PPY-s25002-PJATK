#zadanie z listy2 DinhDucAnh s25002
#zadanie1

# Pobieranie danych od użytkownika
start = int(input("Podaj liczbę początkową: "))
end = int(input("Podaj liczbę końcową: "))
step = int(input("Podaj wielkość odstępu między liczbami: "))

# Wypisywanie liczby
for number in range(start, end + 1, step):
    print(number)


#zadanie2
message = input("Wprowadź komunikat: ")

# Odwracanie komunikatu
reversed_message = message[::-1]

    # Wypisywanie odwróconego komunikatu
print("Odwrócony komunikat:", reversed_message)
#zad3
import random

def get_random_word():
    words = ['komputer', 'programowanie', 'python', 'rozwiązanie', 'algorytm', 'funkcja', 'zmienna']
    return random.choice(words)

def main():
    word = get_random_word()
    word_length = len(word)

    print(f"Komputer wybrał losowe słowo. Słowo ma {word_length} liter.")
    chances_left = 5
    letters_found = []

    while chances_left > 0:
        letter = input(f"Pozostało {chances_left} szans. Podaj literę: ")

        if letter in word:
            if letter not in letters_found:
                letters_found.append(letter)
                print("Tak")
            else:
                print("Ta litera już była podana!")
        else:
            print("Nie")
            chances_left -= 1

        if len(letters_found) == len(set(word)):
            print("Gratulacje, odgadłeś słowo:", word)
            break

    if chances_left == 0:
        print("Niestety, nie udało się odgadnąć słowa. Słowo to:", word)

if __name__ == "__main__":
    main()
#zad4
import random

def get_random_word():
    words = ['komputer', 'programowanie', 'python', 'rozwiązanie', 'algorytm', 'funkcja', 'zmienna']
    return random.choice(words)

def display_hangman(tries):
    stages = [
        '''
            --------
            |      |
            |      O
            |     \\|/
            |      |
            |     / \\
            -
        ''',
        '''
            --------
            |      |
            |      O
            |     \\|/
            |      |
            |     /
            -
        ''',
        '''
            --------
            |      |
            |      O
            |     \\|/
            |      |
            |
            -
        ''',
        '''
            --------
            |      |
            |      O
            |     \\|
            |      |
            |
            -
        ''',
        '''
            --------
            |      |
            |      O
            |      |
            |      |
            |
            -
        ''',
        '''
            --------
            |      |
            |      O
            |
            |
            |
            -
        ''',
        '''
            --------
            |      |
            |
            |
            |
            |
            -
        '''
    ]
    return stages[tries]

def main():
    word = get_random_word()
    word_length = len(word)
    tries = 6

    guessed_word = ['_' for _ in range(word_length)]

    print("Witaj w grze Szubienica!")
    print(display_hangman(tries))

    while tries > 0 and '_' in guessed_word:
        print(" ".join(guessed_word))
        letter = input("Podaj literę: ")

        if letter in word:
            for i, c in enumerate(word):
                if c == letter:
                    guessed_word[i] = letter
        else:
            tries -= 1
            print(display_hangman(tries))
            print(f"Nie ma takiej litery. Pozostało prób: {tries}")

    if '_' not in guessed_word:
        print(" ".join(guessed_word))
        print("Gratulacje, udało Ci się odgadnąć słowo!")
    else:
        print(f"Niestety, nie udało Ci się odgadnąć słowa. Słowo to: {word}")

if __name__ == "__main__":
    main()
#zad 5
def draw_board(board):
    for row in board:
        print(" ".join(row))

def check_win(board, player):
    # Sprawdzanie wierszy
    for row in board:
        if all([cell == player for cell in row]):
            return True

    # Sprawdzanie kolumn
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True

    # Sprawdzanie przekątnych
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True

    return False

def main():
    board = [['_' for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    current_player = 0

    draw_board(board)
    moves_left = 9

    while moves_left > 0:
        print(f"Ruch gracza {players[current_player]}")
        row = int(input("Podaj numer wiersza (1-3): ")) - 1
        col = int(input("Podaj numer kolumny (1-3): ")) - 1

        if board[row][col] == '_':
            board[row][col] = players[current_player]
            draw_board(board)
            moves_left -= 1

            if check_win(board, players[current_player]):
                print(f"Gracz {players[current_player]} wygrywa!")
                break

            current_player = 1 - current_player
        else:
            print("To pole jest już zajęte. Spróbuj ponownie.")

    if moves_left == 0:
        print("Gra zakończona remisem!")

if __name__ == "__main__":
    main()
