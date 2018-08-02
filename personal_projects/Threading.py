import threading

"""
# threading helps to make a program do multiple things at a time
# however, most of the time this is not a good idea mostly in calculations
# it is a mostly a good idea when making a messenger program which will need two checks
# this means the messenger will need two different objects:
    # on will be responsible for sending out
    # and another is responsible for listnening of reading.
    # then create a good chat
"""
class MauriceMessenger(threading.Thread):
    def run(self):                 # this run function is a specific function name needed when creating threading things
        for _ in range(10):               # this _ (underscore) means that u don't really wanna specify which variable
            print(threading.current_thread().getName())    # giving every thread a name

x = MauriceMessenger(name="Send out messages")  # here u can even name you object
y = MauriceMessenger(name="Receive messages")

# we need to call a built in function " start() which will call run function above
x.start()
y.start()