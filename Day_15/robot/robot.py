# Create three classes Cook waiter Singer | these classes should have a single method to perform
# their activity

# Create robo classes and inherit above classes

class Waiter():
    def serve_food(self):
        print("serve food")

class Singer():
    def Sing(self):
        print("sing a song")

class Cook():
    def cook(self):
        print("cook a food")

class Robot(Cook, Waiter, Singer):
    def robot(self):
        print("I am a Robot")

obj_robo = Robot()
obj_robo.robot()
obj_robo.cook()
