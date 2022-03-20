days = 1
meters = 5364
command = input()
while command != "END":
    if command == "Yes":
        days += 1
    elif command == "No":
        pass
    meter = int(input())
    meters += meter
    if meters >= 8848:
        print(f'Goal reached for {days} days!')
        break
    elif days >= 5:
        print("Failed!")
        print(meters)
        break
    command = input()
if meters < 8848 and days < 5:
    print("Failed!")
    print(meters)
