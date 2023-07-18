# This program counts how many times a word is repeated in the given text document.

def word_counter(input_str):            # function line
    word_list = input_str.split()
    counter = {}

    for word in word_list:
        if word in counter:
            counter[word] += 1
        else:
            counter[word] = 1

    return counter

with open("sampleTEXT.txt", "r", encoding="utf-8") as f:
    f_content = f.read()

result = word_counter(f_content)

# Print the word count
print(result)

