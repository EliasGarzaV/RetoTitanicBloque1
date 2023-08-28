import pandas as pd
import os
path = os.getcwd()
import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

train = pd.read_csv(path + '\RetoTitanicBloque1\Data\\train_clean.csv')
train = train.drop(columns = [train.columns[0]])

test = pd.read_csv(path + '\RetoTitanicBloque1\Data\\test.csv')
idxtest = test['PassengerId']


X_train, X_test, y_train, y_test = train_test_split(train.drop(columns='Survived'), train['Survived'], test_size=0.2, random_state=1)

classifier = SVC()
classifier.fit(X_train, y_train)
prediction = classifier.predict(X_test)

acc = accuracy_score(y_test, prediction)
matrix = pd.DataFrame(
        confusion_matrix(y_test, prediction),
        columns=['Predicted 0', 'Predicted 1'],
        index=['Actual 0', 'Actual 1'])

print(matrix)

print(classification_report(y_test,prediction))

#pd.DataFrame({'PassengerId' : idxtest, 'Survived' : prediction}).to_csv(path + '\RetoTitanicBloque1\Results\SVM_gender_submission.csv', index = False)