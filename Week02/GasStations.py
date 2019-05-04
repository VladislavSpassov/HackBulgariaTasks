def gas_stations(distance,tank_size,stations):
    gas_stations_in_route = []
    distance_traveled = 0
    while True:
        if(distance_traveled + tank_size >= distance):
            break
        gas_station = max([station for station in stations if station <= distance_traveled + tank_size])
        gas_stations_in_route.append(gas_station)
        distance_traveled = gas_station




        return gas_stations_in_route








    stat = [];
    currentReservoair = tank_size

    for index in range(1,len(stations)):
        currentReservoair =  currentReservoair - stations[index - 1]

        
        if(currentReservoair - (stations[index] -  stations[index - 1]) < 0):
            stat.append(stations[index - 1])
            currentReservoair = tank_size

    print(stat)


gas_stations(320,90,[50, 80, 140, 180, 220, 290])
gas_stations(390, 80, [70, 90, 140, 210, 240, 280, 350])

