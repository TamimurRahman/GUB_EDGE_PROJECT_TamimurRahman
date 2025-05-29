numbers = list(map(int, input("Enter space-separated numbers: ").split()))
mean_value = sum(numbers) / len(numbers)
print("Mean:", mean_value)
sorted_numbers = sorted(numbers)
n = len(sorted_numbers)
if n % 2 == 0:  
    median_value = (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2
else:  
    median_value = sorted_numbers[n // 2]
print("Median:", median_value)
frequency = {}
for num in numbers:
    frequency[num] = frequency.get(num, 0) + 1

max_count = max(frequency.values())
modes = [key for key, value in frequency.items() if value == max_count]
if len(modes) == 1:
    print("Mode:", modes[0])
else:
    print("No unique mode or multiple modes:", modes)
