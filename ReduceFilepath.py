import pdb


#pdb.set_trace()

def reduce_file_path(path):
    result = PathWithoutLastSlash(path)
    result = TwoDots(result)
    result = OneDot(result)
    print(result)

def PathWithoutLastSlash(p):
    if(len(p) == 1 and p == "/"):
        return p
    result = ""
    for i in range(0,len(p) - 1):
        if(p[i] == "/" and p[i] == p[i + 1]):
            continue
        result += p[i]

    return result


def TwoDots(p):
    dots = ".."
    result = ""
    prev = 0
    curr = 0
    count = 0
    for index in range(0,len(p) - 1):
        currentstr = ""
        if(p[index] == "/"):
            if(prev == 0 and curr == 0):
                curr = index
            else:
                prev = curr
                curr = index

            result +=p[index]
            count +=1
            if(index == len(p) - 2):
                result+=p[index + 1]
            continue

        if(p[index] == "." and p[index] == p[index + 1]):
            result = result[0:prev] + result[curr:index]

            continue

        result+= p[index]
        
    return result

def OneDot(p):
    result =""

    for index in range(0,len(p) - 1):
        if(p[index] == "." and p[index + 1] == "/"):
            continue

        result += p[index]
    return result
reduce_file_path("/srv/./././././")


reduce_file_path("/")

reduce_file_path("/srv/../")
reduce_file_path("/srv/www/htdocs/wtf/")

reduce_file_path("/srv/www/htdocs/wtf")

reduce_file_path("/srv/./././././")

reduce_file_path("/etc//wtf/")

reduce_file_path("/etc/../etc/../etc/../")
reduce_file_path("//////////////")
reduce_file_path("/../")



