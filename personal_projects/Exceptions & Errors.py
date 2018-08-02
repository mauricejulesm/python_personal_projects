print("How old are you?\n")

while True:
    try:
        Age = int(input("Enter your age hoss: \n"))
        life_expectancy = 2017/Age
        print("Woow, did you know you can live other:", life_expectancy, " Years")
        break   # break after try:
    except ValueError:  # Use this to handle the user wh might enter non Integer thing
        print("You entered a wrong value. Try again\n")

    except ZeroDivisionError:   # Use this to handle the user who might try to enter zero ( 2017/0 will create an Arthimetic Error)
        print("Never enter zero, you stupid idiot ! hhahahha\n")

        # Another way to handle errors is to use keyword ( except: ) only
        # It works like this:
        ''' :except:
                print("put here what you want to appear as a warning")
                '''
        # however, this is really not  recommended bcz it might hide all errors made in the program
        # which might cause it to misbehave

    finally:        # You use this to do something that should happen no matter what ( as long as the loop as finished)
        print("The loop finished!\n*****Thank you for Using this app! *****\n")


