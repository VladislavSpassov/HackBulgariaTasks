from random_word import RandomWords



def book_generator(count,chapterlength):

    r = RandomWords()
    r.get_random_word()
`   print(r)


book_generator(3,4)