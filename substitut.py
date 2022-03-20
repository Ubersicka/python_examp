from sys import exit
k = int(input())
l = int(input())
m = int(input())
n = int(input())
counter = 0
for first in range(k, 9):
    for second in range(9, l - 1, -1):
        for third in range(m, 9):
            for four in range(9, n - 1, -1):
                if first % 2 == 0 and third % 2 == 0 and second % 2 == 1 and four % 2 == 1:
                    if first == third and second == four:
                        print("Cannot change the same player.")
                    else:
                        print(f'{first}{second} - {third}{four}')
                        counter += 1
                if counter == 6:
                    exit()
