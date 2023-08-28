# Import the libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
path = os.getcwd()
import random
random.seed(0)

sns.set()

def titanic_gnb():
    data = pd.read_csv(r'..\Data\\train_clean.csv')

    feature_cols = ['Survived', 'Pclass', 'Age', 'SibSp', 'Parch', 'Fare',
        'Embarked_C', 'Embarked_Q', 'Embarked_S', 'is_male']
    X = data.drop(columns = "Survived")
    y = data.Survived

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0, shuffle=False) # 70% training and 30% test

    clf = GaussianNB()
    clf.fit(X_train, y_train)

    pred = clf.predict(X_test)

    acc = accuracy_score(y_test,pred)
    #acc

    # Create a Confusion Matrix
    matrix = pd.DataFrame(
            confusion_matrix(y_test, pred),
            columns=['Predicted 0', 'Predicted 1'],
            index=['Actual 0', 'Actual 1'])
    return acc, matrix