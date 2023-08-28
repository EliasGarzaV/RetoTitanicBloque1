#%%
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import random
random.seed(0)

def titanic_rf(dep: int):
    train = pd.read_csv(r'..\Data\\train_clean.csv')
    train = train.drop(columns = [train.columns[0]])
    y = train.Survived  
    X  = train.drop(columns = "Survived")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1, shuffle=False) # 70% training and 30% test

    #%%
    #test = pd.read_csv(r'..\Data\\test.csv')
    #idxtest = test['PassengerId']

    #test['Age'] = test['Age'].fillna(test['Age'].mean())
    #test['Fare'] = test['Fare'].fillna(test['Fare'].mean())
    #test = pd.get_dummies(test, columns = ['Embarked'])
    #test['is_male'] = pd.get_dummies(test['Sex'])['male']
    #test = test.drop(columns= ['Cabin', 'PassengerId', 'Ticket', 'Name', 'Sex'])


    #X_train = train.drop(columns=['Survived'], axis=1)
    #X_test 
    #%%
    classifier = RandomForestClassifier(max_depth= dep, random_state=0)
    classifier.fit(X_train, y_train)
    prediction = classifier.predict(X_test)
    acc = accuracy_score(y_test,prediction)
    #acc

    # Create a Confusion Matrix
    matrix = pd.DataFrame(
            confusion_matrix(y_test, prediction),
            columns=['Predicted 0', 'Predicted 1'],
            index=['Actual 0', 'Actual 1'])
    return acc, matrix

#pd.DataFrame({'PassengerId' : idxtest, 'Survived' : prediction}).to_csv('..\Results\RandomForest_gender_submission.csv', index = False)