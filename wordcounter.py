# This program counts how many times a word is repeated in the given text document.

def word_counter(input_str):
    word_list = input_str.split()
    counter = {}

    for word in word_list:
        if word in counter:
            counter[word] += 1
        else:
            counter[word] = 1

    return counter

def print_top_k(counter, k):
    sorted_count = sorted(counter.items(), key=lambda x: x[1], reverse=True)

    for i in range(k):
        print(sorted_count[i])

with open("sampleTEXT.txt", "r", encoding="utf-8") as f:
    f_content = f.read()

k = int(input("Enter the value of k: "))

result = word_counter(f_content)
print_top_k(result, k)
