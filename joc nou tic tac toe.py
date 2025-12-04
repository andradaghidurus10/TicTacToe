from random import randrange
from time import sleep


def afisare_placa(board):
    print('+---+---+---+')
    for element in board:
        print(f'| {element[0]} | {element[1]} | {element[2]} |')
        print('+---+---+---+')


def castigator(board, simbol):
    for rand in range(3):
        if board[rand][0] == board[rand][1] == board[rand][2] == simbol:
            return True
    for coloana in range(3):
        if board[0][coloana] == board[1][coloana] == board[2][coloana] == simbol:
            return True
    if board[0][0] == board[1][1] == board[2][2] == simbol:
        return True
    if board[0][2] == board[1][1] == board[2][0] == simbol:
        return True
    return False

def tabla_plina(board):
    for rand in board:
        for celula in rand:
            if isinstance(celula, int):
                return False
    return True


print('✨Bine ai venit la joc!✨')

while True:

    board = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    print("Tabla arata asa:")
    afisare_placa(board)
    print('Completeaza tabla de joc pentru a castiga 🎉')

    while True:
        mutare = int(input('Introduceti miscarea:'))

        rand = (mutare - 1) // 3
        coloana = (mutare - 1) % 3
        if type(board[rand][coloana]) == int:
            board[rand][coloana] = 'X'
        else:
            print('mutare efectuata deja!')
            continue
        # afisare_placa(board)
        if castigator(board, 'X'):
            print("🎉Felicitari!! Esti castigator🎉")
            break
        if tabla_plina(board):
            print('Egalitate!🤗')
            break
        afisare_placa(board)


        # Mutarea calculatorului
        print("Miscarea mea este....")
        sleep(1.5)

        while True:
            calculator = randrange(1, 10)
            rand = (calculator - 1) // 3
            coloana = (calculator - 1) % 3

            if type(board[rand][coloana]) == int:
                board[rand][coloana] = 'O'
                break
        print(calculator)
        afisare_placa(board)
        if castigator(board, 'O'):
            print("Ups...Mai incearca 😢")
            break
        if tabla_plina(board):
            print('Egalitate!🤗')

    iar = input("Vrei sa incerci iar?").lower()

    if iar != "da":
        print("OK! La revedere! 👋")
        break