import sys
import os


def chapter_generators(directory):

    for filename in sorted(os.listdir(directory)):
        if(".txt" in filename):
            f = open(filename,"r")
            print(filename)
            currectChapter = []
            for line in f:
                if("#" not in line):
                    currectChapter.append(line)
                else:
                    title = line
                    yield "".join(currectChapter)
                    currectChapter = [line]
                



for gen in chapter_generators("/home/vladislavspassov/Desktop/Python101/05.04.2019/"):
    print(gen)
    



