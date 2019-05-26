from contextlib import contextmanager
import time 
import datetime



@contextmanager
def performance(file_name):
    file = open(file_name,"w+")
    start = time.perf_counter()
    yield 
    end = time.perf_counter()


    file.write("{0}    {1}".format(datetime.datetime.now(),end - start))



with performance("log_file.txt"):
    time.sleep(1)







@contextmanager
def assertRaises(exception,msg = None):
    try:
        yield 
    except exception:
        pass
    else:
        raise exception
    


class assertRaises:
    def __init__(self,exception,message = None):
        self.exception = exception
        self.message = message

    def __enter__(self):
        pass

    def __exit__(self, exception_class,exc):
        
        if(exception_class == self.exception_class):
            if(message is not None):
                return True
            
            return False    

        return False    


def assertRaises(expected_exception_class,message = None):
    try:

        yield 
    except Exception as exc:
        if type(exc) == expected_exception_class:

