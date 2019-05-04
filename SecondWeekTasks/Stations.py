import pdb

#pdb.set_trace()
def gas_stations(distance, tank_size, stations):
    result = []
    for index in range(len(stations)):
        if(index == len(stations) - 2):
            if(distance - stations[index]> tank_size):
                result.append(stations[index + 1])
                break
        if(index == 1):
            if(stations[0] < tank_size and stations[index] > tank_size):
                result.append(stations[0])
        if(stations[index + 2] - stations[index] >= tank_size):

            result.append(stations[index + 1])

        print(result)
        
    return result    

print(gas_stations(320, 90, [50, 80, 140, 180, 220, 290]))
print(gas_stations(390, 80, [70, 90, 140, 210, 240, 280, 350]))
