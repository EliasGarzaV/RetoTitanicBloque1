#%%
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import random
import pickle
random.seed(0)

def titanic_rf(dep: int, X_train, y_train, X_test, y_test):

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

def titanic_rf_tuned(n_trees, dep: int, crit, X_train, y_train, X_test, y_test):

    classifier = RandomForestClassifier(n_estimators=n_trees,
                                        max_depth= dep,
                                        random_state=0,
                                        criterion=crit,
                                        min_samples_leaf=5,
                                        )
    classifier.fit(X_train, y_train)
    prediction = classifier.predict(X_test)
    acc = accuracy_score(y_test,prediction)
    #acc

    # Create a Confusion Matrix
    matrix = pd.DataFrame(
            confusion_matrix(y_test, prediction),
            columns=['Predicted 0', 'Predicted 1'],
            index=['Actual 0', 'Actual 1'])
    return acc, matrix, classifier

#pd.DataFrame({'PassengerId' : idxtest, 'Survived' : prediction}).to_csv('..\Results\RandomForest_gender_submission.csv', index = False)
def serialize_rf(dep: int, X_train, y_train, path):

    classifier = RandomForestClassifier(max_depth= dep, random_state=0)
    classifier.fit(X_train, y_train)
    
    # Serialize the model to a file using pickle
    with open(path, 'wb') as model_file:
        pickle.dump(classifier, model_file)
        
    return True
    
#%%
train = pd.read_csv(r'..\Data\\train_clean.csv')
train = train.drop(columns = [train.columns[0]])
y = train.Survived  
X  = train.drop(columns = "Survived")

serialize_rf(9, X, y, r'..\Interface\model.pkl')
    
    
# %%
