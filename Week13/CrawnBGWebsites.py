import requests 
from bs4 import BeautifulSoup
from time import sleep

start = "http://register.start.bg/"
f = requests.get(start)
soup = BeautifulSoup(f.text, 'html.parser')
websites = []
for link in soup.find_all('a'):
    l = link.get('href')

    #if(not type(l) is None or not type(l)is unicode):
        #print(l)
    ext = ".bg"
    ht = "http"
    website = {}
    count = 0 
    if l is None:
        continue
    elif u"link.php" in l :
        try:
            lin = start + str(l) 

            obj1 = requests.get(lin)
            exists = False
            for key in obj1.headers:
                if(key == "Server"):
                    exists = True
                    break

            if(exists):
                #is_chunked = obj1.headers.get('transfer-encoding', '') == 'chunked'
                #if(is_chunked):
                    #continue
                #elif(obj1.status_code != 200):
                    #print("different status code from 200")
                    #continue
                #else:
                print(l)
                
                print(obj1.headers["server"])
                count+=1
            else:
                print("Not this time")
                continue
        except requests.exceptions.ConnectionError as e:
            pass
        
    
    elif ext and ht in l:
        try:
            
            obj = requests.get(l)
            #is_chunked = obj.headers.get('transfer-encoding', '') == 'chunked'
            #if(is_chunked):
                #continue
            #elif(obj.status_code != 200):
                #print("differen t status code from 200")
                #continue
            #else:
            print(l)

            print(obj.headers["server"])
            count +=1
        except requests.exceptions.ConnectionError as e:
            pass

    else:
        print("Not gonna work")
        continue
    
        #print(obj1)
    #if(".bg" in l): 
        #r = requests.get(l)
        #print(r.headers["Server"])
