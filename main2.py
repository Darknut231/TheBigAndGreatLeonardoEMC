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
modelCosts = pd.read_csv('modelToCost.csv', header=None, index_col=0).squeeze()
spendingData = pd.read_csv('spending_data.csv')
unitedData = pd.read_csv('unitedData.csv')
for index,row in df.iterrows():
    if (len(row.iloc[0]) > 6):
        df.loc[index,'Country'] = df.loc[index,'Country'][2:4]
    else:
        df.loc[index,'Country'] = df.loc[index,'Country'][2:4]
        #print(row[0])
militarySpending = {}
gdps = {}
for index,row in spendingData.iterrows():
    gdps[row.iloc[0]]=row.iloc[2]
    militarySpending[row.iloc[0]] = row.iloc[3]
df["Military spending"] = df["Country"].map(militarySpending)
df["Model"] = df["Model"].map(modelCosts)
df["Gdp"] = df["Country"].map(gdps)
# note for future: connect adjacent procurements into one (if they are similar enough)
# removing missing data
df_no_missing = df.loc[(df["Gdp"] != "Unknown") & (df["Gdp"] != "NA") & (df['Year'] != "NA") & (df['Military spending'] != "NA") & (df["Country"] != "NA") & (df["Year"]!= "NA") & (df["Still Operational"]!= "NA") & (df["Model"]!= "NA") & (df["Successful"]!= "NA")]
#uniting procurements in the same year into one
running = 0
for index,row in df_no_missing.iterrows():
    if(index<len(df_no_missing)-1):
        if(row.iloc[1] == df_no_missing.loc[index+1]['Year'] and row.iloc[0] == df_no_missing.loc[index+1]['Country']):
            running += 1
        else:
            running += 1
            total_cost = running*float(row[3]) #at this point row[3] is meant to be the cost of the helicopter
            new_row = pd.DataFrame([{'Military spending': row.iloc[4], 'Gdp': row.iloc[5],'total cost':total_cost,'Successful':row.iloc[6]}])
            unitedData = pd.concat([unitedData, new_row], ignore_index=True) # adding the new row to the united data
            running = 0
#dropping extra columns
X = unitedData.drop('Successful',axis=1).copy()
y = unitedData['Successful'].copy()
y = y.astype(int)
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