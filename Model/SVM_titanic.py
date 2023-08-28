import pandas as pd
import os
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
path = os.getcwd()
import random
random.seed(0)

def titanic_svm(kernelf : str, degreef: int, X_train, y_train, X_test, y_test):

    classifier = SVC(kernel=kernelf, degree = degreef)
    classifier.fit(X_train, y_train)
    prediction = classifier.predict(X_test)
    
    acc = accuracy_score(y_test, prediction)
    
    # Create a Confusion Matrix
    matrix = pd.DataFrame(
            confusion_matrix(y_test, prediction),
            columns=['Predicted 0', 'Predicted 1'],
            index=['Actual 0', 'Actual 1'])
    return acc, matrix


#train = pd.read_csv(path + '\RetoTitanicBloque1\Data\\train_clean.csv')
#print(train)
#pd.DataFrame({'PassengerId' : idxtest, 'Survived' : prediction}).to_csv(path + '\RetoTitanicBloque1\Results\SVM_gender_submission.csv', index = False)