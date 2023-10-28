nums = None

while nums is None:
    try:
        length = int(input("Kérlek add meg a Fibonacci-sorozat sorszámát: "))

        if length <= 0:
            print("A sorszám csak pozitív egész szám lehet.")
            raise ValueError
        
    except ValueError:
        print("Csak számot és egész számot lehet beírni!")
        
    finally:
        nums = [0] * length

nums[0] = 0
nums[1] = 1

for i in range(2, len(nums)):
    nums[i] = sum(nums[i-2:i])

print(f"A Fibonacci-sorozat {len(nums)}. eleme: {nums[-1]}")