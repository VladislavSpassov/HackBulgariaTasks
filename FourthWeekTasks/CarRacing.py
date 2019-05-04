import json
import random 
import pdb


class Car:
    def __init__(self,car,model,max_speed):
        self.car = car
        self.model = model
        self.max_speed = max_speed

    def __str__(self):
        return str("car-{0} model-{1} max_speed -{2}".format(self.car,self.model,self.max_speed))



class Driver:
    def __init__(self,driver,car):
        self.driver = driver
        self.car = car

    def __str__(self):
        return str("{0}".format(self.driver))

class Race:
    def __init__(self,lstDrivers,crash_chance):
        for el in lstDrivers:
            if(not isinstance(el,Driver)):
                raise TypeError


        if(crash_chance > 1 or crash_chance < 0) :
            raise ValueError

        self.lstDrivers = []
        for el in lstDrivers:
            self.lstDrivers.append(el)


        self.crash_chance = crash_chance

    def result(self):
        current = self.lstDrivers
        numOfCrashes = round(self.crash_chance * len(self.lstDrivers))
        #print(self.crash_chance * len(self.lstDrivers))
        #print(numOfCrashes)
        crashedCars = []
        currentNums = []
        for el in range(numOfCrashes):
            while(True):
                currentCrash = random.randint(0,len(self.lstDrivers) -1)
                if(currentCrash not in currentNums):
                    currentNums.append(currentCrash)   
                    #print(currentCrash)
                    crashedCars.append(self.lstDrivers[currentCrash])
                    #print(self.lstDrivers[currentCrash])

                    break


        count = 0


        still_not_crashed_cars = len(self.lstDrivers) - len(crashedCars)
        for num in range(still_not_crashed_cars):
            while(True):
                curr = random.randint(0,len(current) - 1)
                #print(curr)
                #print(self.lstDrivers[curr])
                if(curr not in currentNums):
                    print("{0} - {1}".format(self.lstDrivers[curr].driver,(8 - count)))
                    count +=2    
                    break

        for c in crashedCars:
            print("{0} has crashed".format(c))


class Championship:
    def __init__(self,name,races_count):
        self.name = name
        self.races_count = races_count

    #def best3():

def main():

    car = Car("Opel","Astra",240)



    
    with open('cars.json','r') as f:
        data = json.load(f)
    
    cars = []
    drivers = []
    for d in data["people"]:
        current = []
        for key,value in d.items():
            
            current.append(value)

        car = Car(current[1],current[2],current[3])
        cars.append(car)
        driver = Driver(current[0],car)
        drivers.append(driver)
    


    race = Race(drivers,0)


    champ = Championship("Grand Pro",3)
    count = 0
    for c in range(champ.races_count):
        race.result()

if(__name__ == "__main__"):
    main()
