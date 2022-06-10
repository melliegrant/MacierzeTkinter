import re
import sys
import numpy as np


def read_matrix(file):
    data = file.read()
    data = re.findall("(?:{[0-9,]+}[,\\s]*)+", data)
    data = [re.findall("(?:\\d[,\\s]*)+", tmp) for tmp in data]
    matrix1 = []
    matrix2 = []
    num_of_columns = 0
    for i in range(len(data[0])):
        matrix1.append([int(x) for x in data[0][i].split(',') if x.strip().isdigit()])
        if i == 0:
            num_of_columns = len(matrix1[0])
        else:
            if len(matrix1[i]) != num_of_columns:
                sys.exit("Nieprawidłowy format pierwszej macierzy")
    for i in range(len(data[1])):
        matrix2.append([int(x) for x in data[1][i].split(',') if x.strip().isdigit()])
        if i == 0:
            num_of_columns = len(matrix2[0])
        else:
            if len(matrix2[i]) != num_of_columns:
                sys.exit("Nieprawidłowy format drugiej macierzy")
    return np.array(matrix1), np.array(matrix2)









if __name__ == '__main__':
    file = open('matrix.txt', 'r')
    matrix1, matrix2 = read_matrix(file)
    file.close()
    while True:
        print("1. Transponowanie Macierzy\n"
              "2. Dodawanie Macierzy\n"
              "3. Odejmowanie Macierzy\n"
              "4. Mnożenie macierzy przez liczbe rzeczywistą\n"
              "5. Mnożenie Macierzy\n"
              "6. Wyznacznik Macierzy\n"
              "7. Macierz Odwrotna\n"
              "8. Rząd Macierzy\n"
              "0. Wyjście")
        choice = int(input())
        match choice:
            case 1:
                print(matrix1.transpose())
            case 2:
                try:
                    result = matrix1 + matrix2
                except Exception as e:
                    print("Nie można dodać macierzy")
                else:
                    print(result)
            case 3:
                try:
                    result = matrix1 - matrix2
                except Exception as e:
                    print("Nie można odjąć macierzy")
                else:
                    print(result)
            case 4:
                print("Wpisz liczbe rzeczywistą")
                number = float(input())
                print(np.dot(number, matrix1))
            case 5:
                try:
                    result = matrix1.dot(matrix2)
                except Exception as e:
                    print("Nie można pomnożyć macierzy")
                else:
                    print(result)
            case 6:
                try:
                    result = np.linalg.det(matrix1)
                except Exception as e:
                    print("Nie można policzyć wyznacznika macierzy")
                else:
                    print(result)
            case 7:
                try:
                    result = np.linalg.inv(matrix1)
                except Exception as e:
                    print("Nie można policzyć macierzy odwrotnej")
                else:
                    print(result)
            case 8:
                print(np.linalg.matrix_rank(matrix1))
            case 0:
                sys.exit()
            case _:
                print("Nieprawidłowa Wartość")
