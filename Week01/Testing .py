def compariosn(a,b):
    if(cmp_to_key(a,b)):
        return True
    else:
        return False

d = {"a" : 1,"b" : 2, "c" : 3}

for v,s in d.items():
    
    print(v , s)


collection = [(1,2,3),("21","afd","daf")]

for v1,v2,v3 in collection:
    print(v1,v2,v3)


lst = ["10","20","30","40","50","60"]
for s in lst:
    print(s[:1])


for idx,s in enumerate(lst):
    print(s,idx)

for s in lst[2 ::2]:
    print(s)



from array import*

arr = array('i',[1,2,21])

for i in arr:
    print(i)


arr.append(5)
arr.insert(2,12)

arr1 = array('i',[124124,14,1,41,4])
arr.extend(arr1)


lst = [14134,134,254252]

arr.fromlist(lst)

print(arr)

