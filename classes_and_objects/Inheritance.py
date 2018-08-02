class Parent():
    def family_name(self):
        name1 = "Kalisa"
        print(name1)


class Child(Parent):        # to inherit from a certain class, you pass the name of the parent class as the child class's parameter.
    def first_name(self):
        name2 = "Jules Maurice"
        print(name2)

# let's create objects for only Child class and it can use everthing from Parent class bcz
# it inherited it's stuff.

object1 = Child()
#object1.first_name()    # here to access Child's function
#object1.family_name()   # here to access Parent's function


    # *** The following is about Multiple Inheritance ***


class GrandChild(Child, Parent):    # here it is inheriting both classes; remember to order them correctly
    def longer_name(self):
        name = "Mulisa"
        print("\nThis is now my longer name\n", name)


gc = GrandChild()
gc.longer_name()
gc.first_name()
gc.family_name()

