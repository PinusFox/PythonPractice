year = None

while year is None:
    try:
        year = int(input("Kérlek add meg a Fibonacci-sorozat sorszámát: "))

        if year <= 0:
            print("A sorszám csak pozitív egész szám lehet.")
            year = None
            raise ValueError
        
    except ValueError:
        print("Csak számot és egész számot lehet beírni!")

if [year % divider == 0 for divider in [4, 100, 400]].count(True) == 3:
    print(f"Az {year} év szökőév.")
else:
    print(f"Az {year} év nem szökőév.")