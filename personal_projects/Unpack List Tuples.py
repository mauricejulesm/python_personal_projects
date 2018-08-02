"""The following program uses a list of items
    then calculates the average just using 3 variables
     you have to add a * on the middle variable"""

def average_marks(grades):
    vital, munemu, *maurice, GB = grades
    average_calcul = sum(maurice) / len(maurice)
    print('The average marks for the students is: ')
    print(average_calcul)

average_marks([78, 60, 80, 65])