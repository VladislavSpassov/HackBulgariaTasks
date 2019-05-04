def tuple_concat(t):
    return str(t[0]) + str(t[1])



'''def elevator(people_weight,people_floor,max_people,max_weight):
    trips = 0
    current_weight = 0
    start = 0
    for index,person in enumerate(people_weight):
        current_weight += people_weight
        if(current_weight > max_weight) or len(people_weight[start:index]) >= max_people:
            trips += len(set(people_floor[start:index])) + 1
            current_weight = people_weight
            start = index

    trips += len(set(people_floor[start:])) + 1

    return trips
'''




