import pandas as pd
import numpy as np
#array = np.array(["blue", "yellow", "pink", "purple"]) # get the array
#series1 = pd.Series(array)  #create the series from the array
#print(series1)

#list = [19, 175, 41, 22]
#series2 = pd.Series(list) #create the series from the list
#print(series2)

#color=["pink", "white", "black", "blue"]
#occurence = [20, 15, 6, 43]
#S=pd.Series(occurence, index=color)
#print(S)
#color=["pink", "white", "black", "blue"]
#S1=pd.Series([20, 15, 6, 43], index=color)
#S2=pd.Series([3, 22, 9, 10], index=color)
#print(S1+S2)

#fruits = ["apples", "oranges", "cherries", "pears"]
#fruits_ro = ["mere", "portocale", "cirese", "pere"]
#S = pd.Series([20, 33, 52, 10], index=fruits)
#S2 = pd.Series([17, 13, 311, 32], index=fruits_ro)
#print(S+S2)

#list = [['Jack', 34, 'Paris'], ['Thomas', 30, 'Roma'], 
 #      ['Alexandre', 16, 'New York']] 
#df = pd.DataFrame(list, columns =['name', 'age', 'city'])
#print(df)
#dictionary  = { 'name' : ['Jack', 'Thomas', 'Alexandre'],
 #   'age' : [34, 30, 16],
  #  'city' : ['Paris', 'Roma', 'New York']}

#df = pd.DataFrame(dictionary)
#print(df)



my_numpy_array=np.random.randn(3,4)
print(my_numpy_array)
df1=pd.DataFrame(my_numpy_array, columns=list("abcd"))
print(df1)

df=pd.read_csv("csv file example - Sheet1.csv")
print(df)
print(df.info())
print(df.head())   #to show the first 5 rows of our data
print(df.describe())  # we will get a detailed description of numerical variables of our data such as mean, min, std, max...etc