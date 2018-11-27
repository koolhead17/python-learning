sentence = input('Enter a sentence: ')
space_count = 0
for charactors in sentence:
    if charactors == " " :
        space_count = space_count + 1
number_of_words = space_count + 1
print('You have entered the sentence: ', sentence, sep= ' ')
print('The sentence has ', number_of_words, 'words', sep=' ')
print('the sentence has ', space_count, 'space inside it.', sep=' ')


