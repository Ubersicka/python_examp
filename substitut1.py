from sys import exit

k = int(input())
l = int(input())
m = int(input())
n = int(input())
counter = 0

for i in range(k, 9):
    for j in range(9, l - 1, -1):
        for y in range(m, 9):
            for z in range(9, n - 1, -1):
                if i % 2 == 0 and y % 2 == 0 and j % 2 == 1 and z % 2 == 1:
                    if i == y and j == z:
                        print("Cannot change the same player.")
                    else:
                        print(f"{i}{j} - {y}{z}")
                        counter += 1
                if counter == 6:
                    exit()
