
file_path = "text1.txt"


with open(file_path, 'w') as file:
    file.write("This is a test. This test is only a test.")


word_count = {}
with open(file_path, 'r') as file:
    for line in file:
        words = line.split()
        for word in words:
            word = word.lower().strip('.,"')
            word_count[word] = word_count.get(word, 0) + 1

result_path = "word_count.txt"
with open(result_path, 'w') as file:
    for word, count in word_count.items():
        file.write(f"{word}: {count}\n")

print("Word frequencies saved in:", result_path)
