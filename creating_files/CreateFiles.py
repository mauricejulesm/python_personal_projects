# declare an object name ( just any name)

objectForCreating = open("maurice.txt", "w")        # this "w" should be ther to prepare the file for writing on to it
objectForCreating.write("Name: Jules Maurice\n")
objectForCreating.write("Age: 23\n")
objectForCreating.write("School: African Leadership University\n")
objectForCreating.write("Motto: Like Father Like Son - I'm self made\n")
objectForCreating.close()       # we close the thing to stop it from keep using the computer;s memory 

# now let's read the file content
# then after reading
# we can print out the content to the console

# of course we need an object for reading the file

objectForReading = open("maurice.txt", "r")     # also this "r" should be there to help reading
readText = objectForReading.read()    # this like passes the text that hav bnn read to the variable created "readText"
print(readText)
objectForReading.close()
