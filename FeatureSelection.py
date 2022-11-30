# ANOVA feature selection for numeric input and categorical output
# from operator import index
# from turtle import color
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import SelectKBest
import pandas as pd
from sklearn.feature_selection import f_classif
import matplotlib.pyplot as pl
import consts

# # #define the dataset
# print('Reading dataset ...')

df=pd.read_csv(consts.DATASET_PATH_DROP)

X = df.drop(['Label'], axis=1)  # drop colum Label
X = X.astype('float64')
Y = df['Label']  # Y col Label

# # define feature selection
# apply feature selection, 30 feature
fs = SelectKBest(score_func=f_classif, k=30)
X_selected = fs.fit(X, Y)
dfscores = pd.DataFrame(X_selected.scores_)
dfcolumns = pd.DataFrame(X.columns)
featureScores = pd.concat([dfcolumns,dfscores],axis=1)
featureScores.columns = ['Feature','Score']  #naming the dataframe columns
# print(featureScores.nlargest(30,'Score'))
# featureScores.plot.bar(x='Feature', y='Score')

# view plot feature and score
featureScores.nlargest(30,'Score').plot.bar(x='Feature', y='Score')
pl.show()



# # create Dataset with 30 Feature score_
# dft=pd.read_csv(consts.DATASET_PATH_SDN,usecols=consts.COLUMN_30)
# dft.to_csv(consts.DATASET_PATH_SDN_30, index=False)
# print(dft.shape)

#create Dataset nmap scan vul
# dft=pd.read_csv("I:\Visual code\sdn-ml\dataset\ScanVulNmap.csv",usecols=consts.COLUMN_30)
# dft.to_csv(consts.DATASET_TEST_NMAP_Drop, index=False)

# #create Dataset DoS
# dft=pd.read_csv("I:\Visual code\sdn-ml\dataset\DoSFlow.csv",usecols=consts.COLUMN_30)
# dft.to_csv(consts.DATASET_TEST_DoS_Drop, index=False)
# # print(dft.shape)

# #create Dataset nmap scan vul + Dos
# df = pd.concat([pd.read_csv(consts.DATASET_TEST_DoS_Drop), pd.read_csv(consts.DATASET_TEST_NMAP_Drop)], ignore_index=True)
# df.to_csv(consts.DATASET_TEST_NMAP_DoS_Drop,index=False)

# check Datashet
# df=pd.read_csv(consts.DATASET_TEST_NMAP_DoS_Drop)
# print(df.head)

# create Dataset SQLi
# dft=pd.read_csv(consts.DATASET_TEST_SQLI,usecols=consts.COLUMN_30)
# dft.to_csv(consts.DATASET_TEST_SQLI_DROP, index=False)
# print(dft.shape)