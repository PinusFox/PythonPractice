sentence = input("Kérlek add meg a szöveget: ").lower()
searchedWord = input("Kérlek add meg a keresendő karakterláncot: ").lower()

numberOfOccurrences = sentence.count(searchedWord)

print(f"A \"{searchedWord}\" karakterlánc előfordulása a szövegben: {numberOfOccurrences}")
