import random 


def random_word_generator(num):
    with open("/etc/dictionaries-common/words","r") as f:
        index = 0
        s = ""
        lines = list(f)
        result = ""
        words = random.sample(lines,num)
        print(words)
        for word in words:
            result+= word[0:len(word) - 1] + " "
            
        return result


def generateChapter(num_chapters,chapter_length):
        f = open("book.txt","w+")
        
        for index in range(1,num_chapters + 1):

            f.write("# Chapter {0}".format(index))
            f.write("\n")
            f.write(random_word_generator(chapter_length))    
            f.write("\n")
            f.write("\n")




generateChapter(10,100)
