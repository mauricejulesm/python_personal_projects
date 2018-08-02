class Enemy:
    life = 5

    def attack(self):
        print("Ouch!")
        self.life -= 1

    def check_life(self):
        if self.life <= 0:
            print("I am dead!")
        else:
            print("I have " + str(self.life) + " life left !")

# we have to use an object, In order to access functions inside our class

enemyObject1 = Enemy()
enemyObject2 = Enemy()  # the existence of this 2nd object here doesn't affect the 1st's
enemyObject1.attack()
enemyObject1.check_life()
enemyObject2.check_life()   # here you will see that u the ovject to will still have the full life left