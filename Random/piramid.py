height = int(input("Irja be a piramis magasságát: "))

for row in range(1, height * 2 + 1, 2):
    print(('*' * row).center(height * 2))