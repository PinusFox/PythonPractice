point = int(input("Golgozat összpontja: "))

def Classification() -> str:
    if point < 50:
        return "1"
    elif point < 60:
        return "2"
    elif point < 70:
        return "3"
    elif point < 85:
        return "4"
    else:
        return "5"
í
print(f"Elért érdemjegy: {Classification()}")    