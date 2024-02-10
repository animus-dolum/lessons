import sys


main_word = input()
word_list = list(sys.stdin)

new_word_list = []
for word in word_list:
    new_word_list.append(word[:-1])
word_list = new_word_list

true_list = []
for word in word_list:
    f = True
    for symb in word:
        if word.count(symb) > main_word.count(symb):
            f = False
    if f:
        true_list.append(word)

print(len(true_list))
for word in true_list:
    print(word)
