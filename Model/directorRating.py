# The functions in this module assigns a numerical value to the directors.
# This is essential to use the director as a feature in the regression model.
import creatingDictionary
dataset = creatingDictionary.test()
def populate():
    '''
    This function creates and returns a dictionary.
    The keys are the names of the directors that appear
    in the input dataset.
    The values assigned to the keys are all zero.
    '''
    directorDictionary = {}
    for film in dataset:
        if not(film['Director'] in directorDictionary):
            directorDictionary[film['Director']] = 0
    return directorDictionary

def assignCount():
    '''
    This function calls the populate() function to create the
    dictionary. Later with the for loop it updates the key value from zero
    to the number of films in the dataset directed by the director.
    '''
    directorsDictionary = populate()
    count = 0
    for film in dataset:
        if (film['Director'] in directorsDictionary):
            directorsDictionary[film['Director']] += 1



    return directorsDictionary

def assignTotalRevenue():
    '''
    This function calls the populate() function to create the
    dictionary. Later with the for loop it updates the key value from zero
    to the the total revenue generated by
    films directed by the director (Only the films present in the dataset
    are considered for this purpose).
    '''
    directorsDictionary = populate()
    count = 0
    for film in dataset:
        if (film['Director'] in directorsDictionary):
            directorsDictionary[film['Director']] += float(film['BoxOffice'])



    return directorsDictionary

def assignAverageRevenue():
    '''
    This function calls all the three other functions in this module.
    And stores the dictionaries returned by them in three variables.
    Later it updates the values in the directorsAverage dictionary( the one
    returned by the populate function hence has the values all zero )
    to the average revenue generated by the director( who's name is the key )
    For this it uses the values in the other two dictionaries.
    The keys are the same in all dictionaries. The function devides the total
    Revenue by count to get average.
    '''
    directorsTotal = assignTotalRevenue()
    directorsCount = assignCount()
    directorsAverage = populate()
    for director in directorsAverage:
        directorsAverage[director] = directorsTotal[director] / directorsCount[director]

    return directorsAverage




    



    
