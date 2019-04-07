import random


class Song:
    def __init__(self, title, artist, album, length):
        self.title = title
        self.artist = artist
        self.album = album
        self.length = length

    def __str__(self):
        return str("{0} - {1} from {2} - {3}".format(self.artist,self.title,self.album,self.length))

    def __eq__(self,other):
        if(self.title == other.title):
            return True

        return False

    def __hash__(self):
          return hash((self.title, self.artist,self.album,self.length))

    def lengt(self,**kwargs):
        if(len(kwargs) == 0):
            return self.length

        lst = self.length.split(":")


        for key,value in kwargs.items():
            if(key == "minutes"):
                return lst[len(lst) - 2]
            if(key == "seconds"):
                return lst[len(lst) - 1]
            if(key == "hours"):
                if(len(lst) == 2):
                    return 0
                return lst[0]


s = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")
print(type(s))

print(s.lengt(seconds = True))

class Playlist:
    count = 0
    def __init__(self,name,repeat = False,shuffle = False):
        self.name = name
        self.repeat = repeat
        self.shuffle = shuffle
        self.lst = []

    def add_song(self,song):
        self.lst.append(song)

    def remove_song(self,song):
         self.lst.remove(song)

    def add_songs(self,songs):
        for s in songs:
            self.lst.append(s)

    def total_length(self):
        hours = 0
        minutes = 0
        seconds = 0
        for s in self.lst:
            hours += int(s.lengt(hours = True))
            minutes += int(s.lengt(minutes = True))
            seconds += int(s.lengt(seconds = True))

        hours += int(minutes / 60) 
        minutes = int(minutes % 60) 
        minutes += int(seconds / 60)
        seconds = seconds % 60

        l = ""
        l += str(hours) + ":" + str(minutes) + ":" + str(seconds)

        return l

    def artists(self):
        artisten = {}
        for s in self.lst:
            if(s.artist not in artisten):
                artisten[s.artist] = 1
            else:
                artisten[s.artist] += 1

        return artisten

    def next_song(self):
        Playlist.count += 1
        if(self.repeat):
            if(count == len(self.lst)):
                count = 1
            return self.lst[Playlist.count - 1]
        if(self.shuffle):
            i = random.randint(1,len(self.lst))
            return self.lst[i]

        return self.lst[Playlist.count - 1]
    def pprint_playlist(self):
        for s in self.lst:
            print(s)

    def save(self):
        for i in range(len(self.name)):
            if(self.name[i] == " "):
                self.name[i] = "-"

        f= open("{0}.txt".format(self.name),"w+")
        for song in self.lst:
            f.write(str(song))
            f.write("\n")
        for line in f:
            print(line)
    @staticmethod
    def load(path):
        f = open(path,"r")
        for line in f:
            subsets = line.split("from")
            artist = ""
            title = ""
            album = ""
            length = ""
            for index in range(len(subsets)):
                if(index == 0):
                    artist = subsets[0][0]
                    title = subsets[0][2]
                elif(index == 1):
                    album = subsets[1][0]
                    length = subsets[1][1]
pla = Playlist("Manowar")
so = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="6:44")

pla.add_songs([s,so])

pla.total_length()

pla.save()

code = Playlist.load("/home/vladislavspassov/Desktop/Python101/27.03.2019/Manowar.txt")
print(code.name)


