count_students = int(input())

group_1 = 0
group_2 = 0
group_3 = 0
group_4 = 0
avarage_ocenka = 0

for i in range(count_students):
    ocenka_examp = float(input())
    if ocenka_examp >= 5:
        group_1 += 1
    elif ocenka_examp >= 4:
        group_2 += 1
    elif ocenka_examp >= 3:
        group_3 += 1
    else:
        group_4 += 1
    avarage_ocenka += ocenka_examp
percent_group_1 = group_1 / count_students * 100
percent_group_2 = group_2 / count_students * 100
percent_group_3 = group_3 / count_students * 100
percent_group_4 = group_4 / count_students * 100
total_ocenka = (avarage_ocenka / count_students)

print(f'Top students: {percent_group_1:.2f}%')
print(f'Between 4.00 and 4.99: {percent_group_2:.2f}%')
print(f'Between 3.00 and 3.99: {percent_group_3:.2f}%')
print(f'Fail: {percent_group_4:.2f}%')
print(f'Average: {total_ocenka:.2f}')
