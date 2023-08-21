#%%
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

train = pd.read_csv(r'..\Data\\train_clean.csv')
train = train.drop(columns = [train.columns[0]])
#%%
test = pd.read_csv(r'..\Data\\test.csv')
idxtest = test['PassengerId']

test['Age'] = test['Age'].fillna(test['Age'].mean())
test['Fare'] = test['Fare'].fillna(test['Fare'].mean())
test = pd.get_dummies(test, columns = ['Embarked'])
test['is_male'] = pd.get_dummies(test['Sex'])['male']
test = test.drop(columns= ['Cabin', 'PassengerId', 'Ticket', 'Name', 'Sex'])


X_train = train.drop(columns=['Survived'], axis=1)
X_test = test

y_train = train['Survived']
#%%
classifier = RandomForestClassifier(max_depth=5)
classifier.fit(X_train, y_train)
prediction = classifier.predict(X_test)

pd.DataFrame({'PassengerId' : idxtest, 'Survived' : prediction}).to_csv('..\Results\RandomForest_gender_submission.csv', index = False)