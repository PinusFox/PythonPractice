num = None

def GetFactorial(base: int) -> int:
    result = base

    if base != 1:
        result *= GetFactorial(base - 1)
    
    return result

while num == None:
    try:
        num = int(input("Kérlek add meg egy egész számot: "))
    except ValueError:
        print("Csak számot és egész számot lehet beírni!")

print(f"A(z) {num} faktoriálisa: {GetFactorial(num):,}")