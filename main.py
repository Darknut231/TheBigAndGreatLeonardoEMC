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
for i in df['Model of the helicopter']:
    print(type(i))