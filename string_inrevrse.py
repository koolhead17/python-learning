alphabet = input('enter a string and we will reverseit for you:' )
print('you have entered: ', alphabet, sep=' ')
print('lenght of string','is: ', len(alphabet), sep=' ' )
rev_alphabet = alphabet[-1:-(len(alphabet)+1):-1]
print('the revese of string you have typed is: ', rev_alphabet, sep=' ')





