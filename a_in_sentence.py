# The program tries to find out number of time used in the sentence.

the_sentence = input('Enter a sentece and we will tell you the A score: ')
count = 0
for charactor in the_sentence:
    if charactor == "a" or charactor == "A":
        count = count + 1

print('The sentence you have entered has A count of :', count, sep = " ")        