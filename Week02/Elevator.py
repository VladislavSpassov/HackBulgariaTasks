



import pdb



    
def elevator_trips(people_weight, people_floors, elevator_floors, max_people, max_weight):
    d = {}    
    key = 1

    currentPeople = {}
    elevatorCount = 0
    elevatorFloor = 1
    
    #pdb.set_trace()
    while(key <=  len(people_weight)):

        elevatorFloor = 1
        countPeople = 0
        for index in range(len(people_weight)):
            if(key == len(people_weight) + 1):
                break
            if(people_weight[index] + sum([x[0] for x in d.values()]) <= 200 and countPeople < max_people):
                d[key] = (people_weight[key - 1],people_floors[key - 1])
                key += 1
                countPeople += 1

        while(elevatorFloor <= max([x[1] for x in d.values()])):
            if(any(x[1] == elevatorFloor for x in d.values())):
                for k,value in d.items():
                    if(value[1] == elevatorFloor):
                        d[k] = (0,0)
                        continue                    
                elevatorCount +=1

                if(all(x[1] == 0 for x in d.values())):
                    elevatorFloor = 1
                    elevatorCount +=1
                    continue
            elevatorFloor+=1
    print(elevatorCount)            
    

elevator_trips([80, 60, 40], [2, 3, 5], 5, 2, 200)
elevator_trips([40, 40, 100, 80, 60], [2, 3, 3, 2, 3], 3, 5, 200)
