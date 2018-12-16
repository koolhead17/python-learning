def keyword_arguments(msg, times):
    for i in range(times):
        print(msg)


keyword_arguments('hello world', 6)

print()

print('This is can written in another way too.')

print()

keyword_arguments(times= 6, msg= 'hello world')