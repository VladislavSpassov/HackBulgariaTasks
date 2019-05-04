import csv 

def filter(file,**kwargs):

    reader = csv.DictReader(open(file),fieldnames = ("full_name", "favourite_color", "company_name", "email", "phone_number", "salary"))   
    result = [] 
    kwarg = []
    for kw in kwargs:
        print(kw)
        kwarg.append(kw)
        

    count = 0
    salaries = []
    for line in reader:
        #print(line)
        result.append(line)
        
        #if(kwargs["full_name"] == line["full_name"]):
            #print(line)


        #if(kwargs["full_name"] == line["full_name"] and kwargs["favourite_color"] == line["favourite_color"]):
            #print(line)
        
        
        #if(kwargs["full_name_startswith"] in line["full_name"]):
         #   print(line)


        #if(kwargs["email__contains"] in line["email"]):
            #print(line)


        #if(int(line["salary"]) >= kwargs["salary__gt"] and int(line["salary"]) <= kwargs["salary__lt"]):
            #print(line)
                
        
        if(int(line["salary"]) >= kwargs["salary__gt"] and int(line["salary"]) <= kwargs["salary__lt"]):
            salaries.append(line)

        

    print(sorted(salaries,key = lambda s: s["salary"]))
    
#filter('example_data.csv',full_name="Diana Harris")
#print("---------")
#filter('example_data.csv', full_name="Diana Harris", favourite_color="lime")
#filter('example_data.csv',full_name_startswith = "Diana")

#filter('example_data.csv', email__contains="@gmail")
#filter('example_data.csv', salary__gt=1000, salary__lt=3000)
filter('example_data.csv', salary__gt=1000, salary__lt=3000, order_by='salary')


    