"""Ramprobo controller."""
from controller import Robot
from controller import Motor
from controller import Accelerometer
from controller import LED
import math 



class RoboController(Robot):
    def __init__(self):
        super(RoboController,self).__init__()
        self.timeStep = 32
        
        self.accelerometer=self.getDevice("accelerometer") 
        self.accelerometer.enable(self.timeStep)
        
        self.front_led = self.getDevice("front led") 
        self.back_led = self.getDevice("back led") 
        self.left_led = self.getDevice("left led") 
        self.right_led = self.getDevice("right led")
        
        self.left_motor = self.getDevice("left wheel motor") 
        self.right_motor = self.getDevice("right wheel motor") 
        self.left_motor.setPosition(math.inf) 
        self.right_motor.setPosition(math.inf)
        self.left_motor.setVelocity(0.5)
        self.right_motor.setVelocity(-0.5)
        self.direction_switch = False
        self.accValues=[]
        
    
    def run(self):
    while self.step(self.timeStep) != -1:
        acceleration = self.accelerometer.getValue()
        for i in range(3):
        self.accValues.append(self.accelerometer.getValue())
        
        if (abs(self.accValues[1]) > abs(self.accValues[0])):
            
            self.front_led.set(false)
            self.back_led.set(false)
            self.left_led.set(self.accValues[1] > 0.0)
            self.right_led.set(self.accValues[1] < 0.0)
        else:
            self.front_led.set(self.accValues[0] <0.0)
            self.back_led.set(self.accValues[0] > 0.0)
            self.left_led.set(false)
            self.right_led.set(false)
            self.accValues=[]



controller = RoboController()
controller.run()



      