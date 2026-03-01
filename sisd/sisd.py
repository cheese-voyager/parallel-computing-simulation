def sisd_sum(data):
    total = 0
    for x in data:
        total += x
        print(f"Processing {x}, current total = {total}")
    return total

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    result = sisd_sum(numbers)
    print("Sum SISD =", result)