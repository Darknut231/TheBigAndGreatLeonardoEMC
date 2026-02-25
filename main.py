#https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2 519 - Bangladesh NG - Nigeria ID - 1440donesia TM - Turkmes610tan 285 - Algeria 1440 - 1440dia SA - Saudia Arabia
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay
df = pd.read_csv('the big and great dataset (TBaGD).csv')
#print(df.dtypes)
df_no_missing = df.loc[(df["cost(mil$)"] != "Unknown") & (df["cost(mil$)"] != "") & (df["Date of order"] != "Unkown") & (df["Still operatable?"] != "?")]
X = df_no_missing.drop('Successfull procurement',axis=1).copy()
X = X.drop('Model of the helicopter',axis=1).copy()
X = X.drop('GDP billions $ of the owner',axis=1).copy()
y = df_no_missing['Successfull procurement'].copy()
X_train, X_test, y_train, y_test = train_test_split(X,y,random_state=20)
clf_dt = DecisionTreeClassifier(random_state=10)
clf_dt = clf_dt.fit(X_train,y_train)
plt.figure(figsize=(15,7.5))
plot_tree(clf_dt,
          filled=True,
          rounded=True,
          class_names=["Success","Unsuccess"],
          feature_names=X.columns)
plt.show()
#df_no_missing = df with no missings in cost or date =)
