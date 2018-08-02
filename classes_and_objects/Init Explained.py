# init is like a special type of function that gets called automaticall whenever you call an object

class Tuna:
    def __init__(self):
        print("I'm Tuna1 and I'm swimming")

    def swim(self):
        print("I'm Tuna2 and I'm swimming\n")


    # then let's create an object to call our functions
fishCall = Tuna()
fishCall.swim()

# you see! Tuna2 got called despite not creating it's object

print("***************** for the second class *****************\n")


class Enemy:
    def __init__(self, x):
        self.energy = x     # x is the this we passed in init function

    def get_energy(self):
        print(self.energy)

Juvens = Enemy(5)
Paccy = Enemy(18)

Juvens.get_energy()
Paccy.get_energy()