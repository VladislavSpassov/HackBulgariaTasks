import datetime
import time


def accepts(*types):
    def decorater(f):
        def func(*values):
            for i in range(len(types)):
                if(type(values[i]) != types[i]):
                    raise TypeError



            return f(*values)
        return func
    return decorater


def fu(s):
        result = ""
        for i in range(len(s)):
            asciCode = (ord(s[i]) + number) 
            
            current = chr(asciCode)
            result += (current)
            
        return result

def encrypt(number):
    def decorator(f):
        def func(*args,**kwargs):  
            result = ""
            res = f()
            for i in range(len(res)):
                asciCode = (ord(res[i]) + number) 
                
                current = chr(asciCode)
                result += (current)
                
            return result
        return func
    return decorator 

def log(file_name):
    def decorator(func):
        def f(*args,**kwargs):
            file = open(file_name,"w+")
            value = func(*args,**kwargs)
            file.write(func.__name__ + " was called at " + str(datetime.datetime.now())) 
            file.write("\n")       
            
            return value
        return f
    return decorator


def performance(file_name):
    def decorator(func):
        def f(*args,**kwargs):

            start = time.perf_counter()  
            value = func(*args,**kwargs)
            end = time.perf_counter()
            t = end - start
            print("{0} was called and took {1}seconds to complete".format(func.__name__,t)
)
            return value
        return f
    return decorator

@log("log.txt")
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])



@performance("log.txt")
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])

waste_some_time(3)


@encrypt(2)
def get_low():
    return "Get get get low"

print(get_low())
