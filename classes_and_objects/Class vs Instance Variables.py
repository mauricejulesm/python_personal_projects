class My_ex_Girlfriends:
    gender = "Female"   # this is a class variable and it will be shared to all objects in Girl class

    def __init__(self, name):
        self.name = name

first = My_ex_Girlfriends("Aline")
second = My_ex_Girlfriends("Delice")
print(first.gender)
print(second.gender)

print(first.name)
print(second.name)

print("Or print it like this\n")

print(first.gender + " " + first.name +"\n"+second.gender + " " +second.name)