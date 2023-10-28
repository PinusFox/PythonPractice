import random
import os
import platform

testMode = False

#Amennyiben tesztelünk [LOG]-gal  jelölve 1naplózunk
def Logging(text: str) -> None:
    if testMode:
        print(f"\033[32m[LOG] {text}\033[37m") #\033[32m -> zöld ; \033[37m -> fehér

#Csak a tisztaság miatt. Törli az eddig beírtakat a terminálban
def ClearConsole() -> None:
    if platform.uname().system == "Windows":
        os.system('cls')
    elif platform.uname().system == "Linux":
        os.system('clear')

#ismétlés Csökkentésére
def ShowLog() -> None:
    Logging(f"Gondolt szám: {hiddenNum}")
    Logging(f"Max próbálkozás: {attemptLimit}")

while True:
    ClearConsole()
    
    if input("Szeretnéd teszt módban lefuttatni a kódot? (y/n) ").upper() == 'Y':
        testMode = True
        Logging(f"Tesztelés be van állítva")
    else:
        testMode = False
    
    hiddenNum = random.randint(0, 100)
    attemptLimit = 5
    ShowLog()
    
    print("Gondoltam egy számra 0-tól 100-ig.")
    
    #Beállítja a maximum próbálkozások számát
    userAttemptLimit = input("Mennyi próbálkozást szeretnél? (Ha az alapot szeretnéd használni, ami 5 akkor nyomj egy Entert) ")
    try: #Ha nem írunk be számot akkor hibaüzenetet kapunk
        attemptLimit = int(userAttemptLimit)
    except ValueError:
        attemptLimit = 5
    
    ClearConsole()
    for attempt in range(1, attemptLimit + 1):
        ShowLog()
        
        guessedNum = None
        while True: #Ellenőrzi, hogy a szám 0 és 100 között van-e
            try: #Azért kell, hogy amikor a felhasználó nem számot gépel be akkor ne álljon le a program
                guessedNum = int(input(f"{attempt}. próbálkozás: "))
                if 0 <= guessedNum <= 100: #Csak most jöttem rá, hogy nem is kell 'and', és olvashatóbb így
                    Logging(f"A(z) {guessedNum} el lett mentve a tippelések közé.")
                    break
                else:
                    print("Csak 0-tól 100-ig írhatsz számot")
            except ValueError:
                print("Csak 0-tól 100-ig írhatsz számot")
        
        if guessedNum == hiddenNum:
            print("Kitaláltad a számot!")
            print(f"Összesen {attempt} próbálkozásod volt.")
            break
        elif guessedNum < hiddenNum:
            print("Nagyobbra gondoltam!")
        else:
            print("Kissebbre gondoltam!")
        
        if attempt == attemptLimit:
            print("Nem találtad ki!")
    
    if not input("Szeretnél játszani mégegyszer? (y/n) ").upper() == 'Y':
        exit()
