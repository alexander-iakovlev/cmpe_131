from collections import Counter

my_file = open("document.txt", "r", encoding='utf-8')
data = my_file.read()

#checks every char to make sure is alphanumeric and removes /n with strip
data_formatted="".join(c for c in data if (c.isalnum() or c.isspace())).strip()

#splits list into string
word_list = data_formatted.split(' ')

#sorts by frequency
result = [item for items, c in Counter(word_list).most_common() for item in [items] * c]

#counts and prints frequency
i = 0
j = 0
while i < 5:
    current_word = result[j]
    count = 0
    while result[j] == current_word:
        count += 1
        j += 1
    print(current_word, ": ", count)
    i += 1