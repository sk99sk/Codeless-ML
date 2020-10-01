#Regressions
import pandas as pd
import numpy as np

dataset_train = pd.read_csv('train.csv')

from sklearn.preprocessing import Imputer

imputer = Imputer(missing_values='NaN',strategy='mean')

dataset_train.iloc[:,0:2] = imputer.fit_transform(dataset_train.iloc[:,0:2])


from sklearn.linear_model import LinearRegression

import matplotlib.pyplot as plt

#print('x_train matrix is------------')
x_train = dataset_train.iloc[:, 0]
#print(x_train)



y_train = dataset_train.iloc[:,1]
#print('y_train matrix is-------------')
#print(y_train)


dataset_test = pd.read_csv('test.csv')

x_test = dataset_test.iloc[:,0]
#print('X test matrix is ---------')
#print(x_test)

x_test = x_test.values
x_test = x_test.reshape(-1,1)
#print(x_test.shape)

y_test= dataset_test.iloc[:,1]
#print('Y test matrix is --------')
#print(y_test)
x_train = x_train.values
x_train = x_train.reshape(-1,1)

y_train = y_train.values
y_train = y_train.reshape(-1,1)

#print(type(x_test))
#print(x_test)

y_pred =[]




def poly_reg():
	global x_train
	global y_train
	global y_pred
	
	from sklearn.preprocessing import PolynomialFeatures
	
	poly_reg = PolynomialFeatures()
	#poly_reg.fit(x_train,y_train)
	
	y_pred=poly_reg.fit_transform(x_train)
    
    print(y_pred)
    

#	plt.scatter(x_test,y_test,color='red')
#	plt.plot(x_test,y_pred,color='blue')
#	plt.show()



def lin_reg():
	global x_train
	global y_train
	global y_pred
	lin_reg = LinearRegression()
	lin_reg.fit(x_train,y_train)

	y_pred = lin_reg.predict(x_test)

#lin_reg()
poly_reg()




#print('The error between the values is:')

	
	
	

	
	
	
np.set_printoptions(formatter={'float_kind':'{:f}'.format},precision= 2)	
	
#print(y_pred)
#print(y_pred.count)

#y_diff =[]
#for i in range(0,(y_test.count()-1)):
#	y_temp = y_pred[i] - y_test[i]
#	y_temp = int(y_temp)
#	y_temp = y_temp/y_test*100
#	y_diff.append(y_temp)

#print(y_diff)