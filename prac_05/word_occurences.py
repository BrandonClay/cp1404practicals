
words_counting = {}

user_text = input("Enter a string!: ")
word_list = user_text.split()

for word in word_list:
    frequency = words_counting.get(word, 0)
    words_counting[word] = frequency + 1

max_variable = max(len(word)for word in word_list)
word_list = list(words_counting.keys())
word_list.sort()

for word in word_list:
    print("{:{}}: {}".format(word, max_variable, words_counting[word]))
