# environment
# the vehicle is on a multi-lane road and the position of the vehicle 
# that is the lane in which the vehicle is will be the left most lane 
# assuming it has just started for this environment the vehicles on 
# the rear and sides are not considered and the vehicles in the front will be considered.
# the agent will the root node and the vehicles just in front in each lane 
# will be the next level which will be randomly generated and using bfs or dfs 
# which gap if present between any vehicle in front should be taken is decided 
# the level in front of the next level is not vivsible to the agent 
# using bfs 
# for the vehicles ahead we will find all the gaps and the nearest gap is selected 
# using dfs 
# the first empty lane found is visited

import turtle
import random
import time

windowGraphic = turtle.Screen()
windowGraphic.title("4- lane highway")
windowGraphic.setup(1000,800)
# windowGraphic.bgcolor("white")
windowGraphic.bgpic("road.png")
windowGraphic.listen()
windowGraphic.register_shape("car31.gif")
windowGraphic.register_shape("car32.gif")

myCar = turtle.Turtle()
myCar.hideturtle()
myCar.shape("car31.gif")
myCar.shapesize(1, 1)
myCar.up()
myCar.goto(-420,-250)
myCar.showturtle()
# myCar.goto(-420+(2*280),-250)
# myCar.goto(-420+(1*280),-250)


# def generateRandomVehicle():
carsTop = []
carsMid = []
carsBot = []
x = -420
for i in range(4):
    car = turtle.Turtle()
    car.hideturtle()
    car.shape("car32.gif")
    car.shapesize(1,1)
    car.up()
    car.goto(x,250)
    carsTop.append(car)
    carm = car.clone()
    carm.goto(x,0)
    carsMid.append(carm)
    carb = car.clone()
    carb.goto(x,-250)
    carsBot.append(carb)
    # car.showturtle()
    x = x + 280

def generateCarAhead():
    carArray = []
    for i in range(4):
        carArray.append(random.randint(0,1))
    return carArray

myCarcords = 0
newCarChords = 0
while(True):
    carPosition = generateCarAhead()
    #dfs
    if 0 in carPosition:
        for i in range(4):
            if(carPosition[i]==0):
                newCarChords = i
                break
        for i in range(4):
            if(carPosition[i]==1):
                carsTop[i].showturtle()
        time.sleep(0.5)
        myCar.goto(-420+(newCarChords*280),0)
        myCarcords = newCarChords
        for i in range(4):
            if(carPosition[i]==1):
                carsTop[i].hideturtle()
                carsMid[i].showturtle()
        time.sleep(0.5)
        for i in range(4):
            if(carPosition[i]==1):
                carsMid[i].hideturtle()
                carsBot[i].showturtle()
        time.sleep(0.5)
        for i in range(4):
            if(carPosition[i]==1):
                carsBot[i].hideturtle()
        time.sleep(0.5)
        myCar.goto(-420+(myCarcords*280),-250)
    else:
        print("Waiting for lanes to get empty!!\n\n")
        for i in range(4):
            if(carPosition[i]==1):
                carsTop[i].showturtle()
        time.sleep(1)
        for i in range(4):
            if(carPosition[i]==1):
                carsTop[i].hideturtle()
        time.sleep(0.5)