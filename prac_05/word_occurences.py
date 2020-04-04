
words_counting = {}

user_text = input("Enter a string!: ")
word_list = user_text.split()

for word in word_list:
    frequency = words_counting.get(word, 0)
    words_counting[word] = frequency + 1

for word in word_list:
    print(word, words_counting[word])


print(words_counting)