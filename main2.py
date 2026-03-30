#https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2 519 - Bangladesh NG - Nigeria ID - 1440donesia TM - Turkmes610tan 285 - Algeria 1440 - 1440dia SA - Saudia Arabia
'''
imports the dataset csv file and builds a decision tree and confusion matrix using sklearn and pandas, created by Danylo, newest version 09/03/2026
in plans: add more data
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.svm import SVC
# reading the file
df = pd.read_csv('EMCDATAMilitary.csv')
modelCosts = pd.read_csv('modelToCost.csv')
spendingData = pd.read_csv('spending_data.csv')
print(spendingData['Country'].unique())
militarySpending = []
gdps = []
for row in spendingData:
    gdps.append(row[2])
    militarySpending.append(row[3])
df["Ordered/owned by(gdp)"] = df["Ordered/owned by(gdp)"].map(militarySpending)
for i in range (len(df)):
    df.at[i,'cost(mil$)'] = df.at[i,'cost(mil$)'] * df.at[i,'Quantities']
    if (i > len(df)-4):
        df.at[i,'Successfull procurement'] = 0
    else:
        df.at[i,'Successfull procurement'] = 1
# removing missing data
df_no_missing = df.loc[(df["cost(mil$)"] != "Unknown") & (df["cost(mil$)"] != "")]
X = df_no_missing.drop('Quantities',axis=1).copy()
X = X.drop('Successfull procurement',axis=1).copy()
X = X.drop('Model of the helicopter',axis=1).copy()
#X = X.drop('Ordered/owned by',axis=1).copy()
X = X.drop('Date of order',axis=1).copy()
y = df_no_missing['Successfull procurement'].copy()
'''
one hot encoding
X_encoded = pd.get_dummies(X,columns=['cost(mil$)','Date of order','GDP billions $ of the owner'])
'''
# splitting the data
X_train, X_test, y_train, y_test = train_test_split(X,y,random_state=25) #x encoded here
clf_dt = DecisionTreeClassifier(random_state=15)
clf_dt = clf_dt.fit(X_train,y_train)
def plotTree(clf_dt,X):
    plt.figure(figsize=(15,7.5))
    plot_tree(clf_dt,
            filled=True,
            rounded=True,
            class_names=["Unsuccess","Success"],
            feature_names=X.columns)
#print(clf_dt.feature_importances_)
plotTree(clf_dt,X) #x encoded here

#too many positional arguments???

clf = SVC(random_state=0)
clf.fit(X_train, y_train)
predictions = clf.predict(X_test)
cm = confusion_matrix(y_test, predictions, labels=clf.classes_)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=clf.classes_)
disp.plot() # here the matrix is displayed

plt.show()
#df_no_missing = df with no missings in cost or date =)