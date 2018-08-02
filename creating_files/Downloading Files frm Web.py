from urllib import request

# let's create a variable ( we name is however we want)

goog_url = 'https://query1.finance.yahoo.com/v7/finance/download/GOOG?period1=1493581441&period2=1496173441&interval=1d&events=history&crumb=kPgoLk/RbJK'

def download_from_web(csv_url):

    response = request.urlopen(csv_url)   # making the program to connect to the internet
    csv = response.read()   # this csv is just a variable
    csv_string = str(csv)   # here we are converting the above read data into string
    lines = csv_string.split("\\n")     # here we crtd a nu var clld lines and the prgrm will split lines

    dest_url = r'googData.csv'  # this creates the destination of the file
    fx = open(dest_url, "w")    # this prepare the file to write to it

    # now we create a for loop to loop through the file lines then download them
    for line in lines:
        fx.write(line + "\n")
    fx.close()

download_from_web(goog_url)    # to call the function



