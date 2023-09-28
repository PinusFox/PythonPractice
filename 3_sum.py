sums = ["első", "második", "harmadik"]

def CompareSums() -> None:
    previousSum = None
    
    for sum in sums:
        if sum != previousSum and previousSum != None:
            print("Három különböző számot Írt be.")
            return
    
        previousSum = sum
    
    print("Három azonos számot írt be.")

for i in range(len(sums)):
    sums[i] = int(input(f"Írja be az {sums[i]}: "))

print(f"[LOG] Számok: {sums}")

print(f"A három szám közül a(z) {max(sums)} legnagyobb.")

CompareSums()
