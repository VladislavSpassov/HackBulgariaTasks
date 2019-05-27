import requests
from bs4 import BeautifulSoup
from time import sleep
import json
from sqlalchemy import create_engine,Column,Integer,String,ForeignKey,table, column, select, update, insert
from sqlalchemy.ext.declarative import declarative_base
from urlparse import urlparse
from sqlalchemy.orm import sessionmaker
from sqlalchemy import *


start = "http://register.start.bg/"
f = requests.get(start)
soup = BeautifulSoup(f.text, 'html.parser')
websites = {}

Base = declarative_base()
engine = create_engine('sqlite:///servers.db', echo = True)
Session = sessionmaker(bind=engine)
session = Session()
metadata = MetaData()
connection = engine.connect()
servers = Table('servers', metadata,
    Column('user_id', Integer, primary_key=True),
    Column('server', String, nullable=False),
    Column('website', String)
)
count = 0
metadata.create_all(engine)
for link in soup.find_all('a'):
    l = link.get('href')

    #if(not type(l) is None or not type(l)is unicode):
        #print(l)

    ext = ".bg"
    ht = "http"

    print(count)
    if l is None:
        continue
    elif u"link.php" in l :
        try:
            lin = start + str(l) 
            obj1 = requests.get(lin)
            parsed = urlparse(lin)

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
                if(parsed.netloc not in websites):
                    engine.execute(servers.insert(),server = obj1.headers["Server"],website =  obj1.url)
                    count +=1

            else:
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
            parsed = urlparse(obj.url)
            

            if(parsed.netloc not in websites):
                engine.execute(servers.insert(),server = obj.headers["Server"], website = obj.url)
                count +=1
            else:
                websites[parsed.netloc] +=1
        except requests.exceptions.ConnectionError as e:
            pass

    else:
        continue
    if(count >= 10):
        break

s = select([distinct(servers.c.server)])
result = connection.execute(s)

for row in result:
    websites[row[0]] = 0


s = select([servers.c.server])
result = connection.execute(s)

for row in result:
    websites[row[0]] +=1

print(websites)
