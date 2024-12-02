#IMPORT MODULES
import numpy
import pandas
import matplotlib.pyplot as plt
from scipy import stats
from sklearn import linear_model
from sklearn import tree
from sklearn.metrics import r2_score
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier



#VARIABLES
speed = [99, 88, 89, 92, 95, 89, 90.9, 96.8, 90, 93.1, 94, 94.22, 98.9]

x = numpy.random.uniform(0.0, 5.0, 250)


#FUNCTIONS

    #Mean
print(f"The mean value of the speeds is {numpy.mean(speed)}")

    #Median
print(f"The median value of the speeds is {numpy.median(speed)}")

    #Mode
print(f"The mode is: {stats.mode(speed)}")

    #Standard Deviation
print(f"The standard deviation of the speeds is {numpy.std(speed)}")

    #Variance
print(f"The variance of the speeds is {numpy.var(speed)}")

    #Percentile (a bit confused)
print(f"The percentile for 10% for speeds is {numpy.percentile(speed, 10)}")

    #Printing random data sets
print(f"This will print a random data set of 250 float numbers, between 0 and 5 {numpy.random.uniform(0.0, 5.0, 250)}")

    #Histogram
plt.hist(x, 5)
plt.show()

    #Normal random data set and its histogram
y = numpy.random.normal(5.0, 1.0, 100000) 
plt.hist(y, 100)
plt.show() #This will print a figure of an array of 100000 floats with a mean value of 5.0 and a standard deviation of 1.0 which will show how many values are within what range 
    
    
    #SCATTER PLOT (makes a proper graph using dots)
xnorm = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ynorm = [90, 80, 70, 60, 50, 40, 30, 20, 10, 100] #i.e (5, 10) , (6, 20) , (7, 30) , (5, 40) , (6, 50) , (7, 60) , (5, 70) , (6, 80) , (7, 90)

#To get input for a list
notalist = input("Enter 9 numbers with space in between for first list: ")
x = notalist.split()
x = [int(num) for num in x] #Not necessary but works well to convert the list data to int

notalist2 = input("Enter 9 numbers for second list: ")
y = notalist2.split()

print(x)
print(y)

plt.scatter(xnorm, ynorm)
plt.show()

    #RANDOM SCATTER PLOT
xrand = numpy.random.normal(10.0, 0.1, 250)
yrand = numpy.random.normal(-1.0, 2, 250)

plt.scatter(xrand, yrand)
plt.show()

    #LINEAR REGRESSION (shows you future of a data, as in where the next line of graph will go to)
slope, intercept, r, p, std_err = stats.linregress(xnorm, ynorm)

        #Here "r" is the coefficient of correlation which signifies the relation between x axis and y axis, its value will be within -1 an 1, where 0 means no relation

def linearregfunc(xnorm): #We can use this function to predict values of y axis corresponding to values of x axis
    return slope * xnorm + intercept

print(f"The value of graph at x = 2.2 is: {linearregfunc(2.2)}") #Predicts value of x at 2.2, noted that t

mymodel = list(map(linearregfunc, xnorm))

print(f"The relationship is {r}")
plt.scatter(xnorm, ynorm)
plt.plot(xnorm, mymodel)
plt.show()

    #POLYNOMIAL REGRESSION
polymodel = numpy.poly1d(numpy.polyfit(xnorm, ynorm, 3))
polyline = numpy.linspace(1, 22, 100)

print(f"The value of y at x = 1.25 is: {polymodel(1.25)}") #Prints value of y at a corresponding given x

print(r2_score(ynorm, polymodel(xnorm)))

plt.scatter(xnorm, ynorm)
plt.plot(polyline, polymodel(polyline))
plt.show()

    #PANDAS (we can use it to predict a value from using 2 different values)
df = pandas.read_csv("anime.csv")

valuestore = ['Weight', 'Volume']

ind = df[valuestore] #These are independent values which will be used to predict the dependent value
dep = df['CO2'] #This is the dependent value which we wil predict

regresser = linear_model.LinearRegression() #Creates a class object for linear regression
regresser.fit(ind, dep) #Takes parameters for the regression

predictedCO2 = regresser.predict([[2300, 1300]]) #Predicts value of CO2 when weight is 2300 and volume is 1300
print("Predicted value for CO2 when weight = 2300, volume = 1300", predictedCO2)

print("Coefficient of change for both independent values:", regresser.coef_) #Prints the coefficient for what will happen if we increase/decrease value of one of the independent values
                #In this case however, if we increase the weight by 1kg, CO2 emission will increase by 0.00755095g
                #and if volume is increased by 1cm^3, CO2 emission will increase by 0.00780526g
                
    #SCALE
        #since its not really convenient to compare different values with different measuring units, we use a method call standardization to get a certain standard value for every unit 
        #the formula used for standardization is: z = (x - u) / s
        #where, z is the new standard (comparable) value
        #x is the original value
        #u is the mean value
        #s is the standard deviation
        #however we do not have to do this manually as the sklearn module has a method called StandardScaler()
#scale = StandardScaler()
#df = pandas.read_csv("data.csv")
#X = df[['Weight', 'Volume']]
#scaledX = scale.fit_transform(X)
#print(scaledX)
#scalereg = linear_model.LinearRegression()
#scalereg.fit(scaledX, y)
#scaled = scale.transform([[2300, 1.3]])
#scalepredictedCO2 = scalereg.predict([scaled[0]])
#print(scalepredictedCO2)

#Turned it into a comment since i dont need it





    #DECISION TREE (takes multiple "features" to make a decision for the "target", google it up for better definition)
animedf = pandas.read_csv("anime.csv") #Accessing the created csv file (a dataframe)

print(animedf) #Printing the created csv file

animedfgen = {'M' : 0, 'F' : 1} #Since python cant read the given data in alphabets we can convert it into a number
animedf['Gender'] = animedf['Gender'].map(animedfgen) #Now converting the data from alphabetical to numerical in the database for the column "Gender"

animedfdemo = {'Shounen' : 0, 'Shoujo' : 1, 'Seinen' : 2, 'Josei' : 3}
animedf['Demograph'] = animedf['Demograph'].map(animedfdemo)

animedffavg = {'Action' : 0, 'SliceOfLife' : 1, 'Erotica' : 2, 'Romance' : 3, 'Psychological' : 4, 'Tragedy' : 5}
animedf['FavGenre'] = animedf['FavGenre'].map(animedffavg)

print(animedf) #Prints the new, numerized version of the dataframe

animefeatures = ['Age', 'FavGenre', 'Demograph'] #Now seperate the Features (the columns that we try to predict from) from the Targets (the column we are predicting)
 
Fcolumns = animedf[animefeatures] #Holds the Features
Tcolumns = animedf['Gender'] #Holds the Target

print(Fcolumns)
print(Tcolumns)

animeTree = DecisionTreeClassifier() #Set up a data tree machine
animeTree = animeTree.fit(Fcolumns, Tcolumns) #Define the Columns

tree.plot_tree(animeTree, feature_names=animefeatures) #Create and define the tree
plt.show()


            #THIS CODE {{{PREDICTS}}} by checking given arguments (Features) to find the plausible Target 
print("If the age is 15, favourite genre is Romance and preferred demograph is Shounen then its a (0 for Male, 1 for Female) :", animeTree.predict([[15, 3, 0]])) #([[Age, FavGenre, Demograph]])















#####SOME USEFUL DEFINITIONS#####

#Numerical data - are numbers, and can be split into two numerical categories:
#   Discrete Data
#       - counted data that are limited to integers. Example: The number of cars passing by.
#   Continuous Data
#       - measured data that can be any number. Example: The price of an item, or the size of an item
#Categorical data - are values that cannot be measured up against each other. Example: a color value, or any yes/no values.
#Ordinal data - are like categorical data, but can be measured up against each other. Example: school grades where A is better than B and so on.
#Mean - The average value
#Median - The mid point value
#Mode - The most common value

#Standard Deviation
#   Standard deviation is a number that describes how spread out the values are.
#   A low standard deviation means that most of the numbers are close to the mean (average) value.
#   A high standard deviation means that the values are spread out over a wider range.

#Variance
#   Variance is another number that indicates how spread out the values are.
#   In fact, if you take the square root of the variance, you get the standard deviation!
#   Or the other way around, if you multiply the standard deviation by itself, you get the variance!

#Histogram
#   To visualize the data set we can draw a histogram with the data we collected.
#   We will use the Python module Matplotlib to draw a histogram.