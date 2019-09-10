from tkinter import filedialog
import pandas as pd
import numpy as np
import os

os.system('cls')
print("Select the file you want to preprocess!!")
file_path = filedialog.askopenfilename()

dataset = pd.read_csv(file_path)
os.system('cls')
print (dataset)


entered_value = 0
x_columns = []
x = []


while entered_value != 'exit':
    os.system('cls')
    print(dataset)
    print('Enter "exit" when you are done entering the columns ')
    print("Enter the column which you want to include in Feature Matrix ")
    entered_value = input("Enter the column: ")
    x_columns.append(entered_value)


x_columns.remove('exit')
x_columns.sort()
os.system('cls')
print(x_columns)


x_columns_values = list(dataset.columns.values)

x_columns_values_select = []

for i in x_columns:
        x_columns_values_select.append(x_columns_values[int(i)])
        
x = dataset[x_columns_values_select]







entered_value = 0
y_columns = []
y = []


while entered_value != 'exit':
    os.system('cls')
    print(dataset)
    print('Enter "exit" when you are done entering the columns ')
    print("Enter the column which you want to include in matrix of dependent variables.")
    entered_value = input("Enter the column: ")
    y_columns.append(entered_value)


y_columns.remove('exit')
y_columns.sort()
os.system('cls')
print(y_columns)


y_columns_values = list(dataset.columns.values)

y_columns_values_select = []

for i in y_columns:
        y_columns_values_select.append(y_columns_values[int(i)])
        
y = dataset[y_columns_values_select]

def imputer():
    global x
    x_columns = []
    from sklearn.preprocessing import Imputer
    imputer = Imputer(missing_values = 'NaN' , strategy='mean' ,axis= 0)
    os.system('cls')
    print("Here we are taking the default stratergy as maen")
    
    entered_value = 0
    
    while entered_value != 'exit':
        os.system('cls')
        print(dataset)
        print('Enter "exit" when you are done entering the columns ')
        print("Enter the column on which you want to use imputer in X-matrix.")
        entered_value = input("Enter the column: ")
        x_columns.append(entered_value)
    
    
    x_columns.remove('exit')
    os.system('cls')
    print(x_columns)
    
    
    for i in x_columns:
            i = int(i)
            j = i+1
            imputer = imputer.fit(x.values[1:, i:j])
            x.values[:, i:j] = imputer.transform(x.values[:, i:j]) 
        
         
    
imputer()





def categorial_data():
    
    global x
    global x_columns_values
    global y
    x_columns_values_select = []
    from sklearn.preprocessing import LabelEncoder
    from sklearn.preprocessing import OneHotEncoder
    label_encoder = LabelEncoder()
    entered_value = 0
    x_columns= []
    
    while entered_value != 'exit':
        os.system('cls')
        print(x)
        print('Enter "exit" when you are done entering the columns ')
        print("Enter the column on which you want to use encoding.")
        entered_value = input("Enter the column: ")
        x_columns.append(entered_value)
    
    
    x_columns.remove('exit')
    os.system('cls')
    print(x_columns)
    
    for i in x_columns:
        x_columns_values_select.append(x_columns_values[int(i)])
        
    for i in x_columns_values_select:
        
        x[i] = label_encoder.fit_transform(x[i])
        
        
    x_columns_values_select = []
    
    for i in x_columns:
        x_columns_values_select.append(x_columns_values[int(i)])
        
        
        x_columns_int = []
    
    for i in x_columns:
        i = int(i)
        x_columns_int.append(i)
        
    onehotencoder = OneHotEncoder(categorical_features= x_columns_int)
    
    
    
    
    
    
    


    x = onehotencoder.fit_transform(x).toarray()
    
        

    os.system('cls')
    print('Do you want to apply label encoding on Y Matrix?(Y/N)')
    y_encode = input('Enter Y/N:')
    
    
    if y_encode == 'y':
        labelencoder_y = LabelEncoder()
        y = labelencoder_y.fit_transform(y)    
    
    
    
    else:
        pass
    
    
    
    
    
categorial_data()  
   

def feature_scaling():
    global x
    
    os.system('cls')
    print('Do you want to apply feature scaling to matrix?(Y/N)?')
    feature_scaling_choice = input('Do you want to apply feature scaling?:')
    
    if feature_scaling_choice == 'y':
        
        from sklearn.preprocessing import StandardScaler
        feature_scalar = StandardScaler()    
        x = feature_scalar.fit_transform(x)
        


    else:
         pass



feature_scaling()

 
    
    
np.set_printoptions(formatter={'float_kind':'{:f}'.format},precision= 2)
os.system('cls')    
print("Using imputer with mean stratergy to data")
print('-----------------------------------')
print("The X matrix is:")
print(x)
print('-----------------------------------')
print('The Y matrix is:')
print(y)
print('-----------------------------------')

