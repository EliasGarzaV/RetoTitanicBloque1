#%%
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import random
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

#pd.DataFrame({'PassengerId' : idxtest, 'Survived' : prediction}).to_csv('..\Results\RandomForest_gender_submission.csv', index = False)