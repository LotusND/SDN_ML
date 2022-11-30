from xml.sax.handler import feature_namespaces
import pandas as pd
import consts
from sklearn.model_selection import train_test_split
from sklearn import tree
from pickle import dump
from sklearn.feature_selection import SelectFromModel
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.metrics import f1_score
from time import time

def train_model():
    print('Reading dataset ...')
    df = pd.read_csv(consts.DATASET_PATH_DROP)
    print(df.shape)
    X = df.drop(['Label'], axis=1)  # drop colum Label X
    X = X.astype('float64')
    Y = df['Label']  # Y col Label
    print('Read data done!')

    print('Normalizing dataset ...')
    lb = LabelEncoder()
    Y = lb.fit_transform(Y)
    dump(lb, open(consts.Y_LABEL_ENCODER_MODEL, 'wb'))
    lb_name_mapping = dict(zip(lb.classes_, lb.transform(lb.classes_)))
    # print(lb_name_mapping)

    scl = StandardScaler()
    X = scl.fit_transform(X)
    dump(scl, open(consts.X_STANDARD_SCALE_MODEL, 'wb'))
    print('Normalize data done!')

    print('Training model ...')
    start=time()
    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=0.3, random_state=0, shuffle=True)
    dts = tree.DecisionTreeClassifier(criterion='entropy', max_depth=30, min_samples_leaf=10,
                       random_state=42)

    dts.fit(X_train, Y_train)
    dump(dts, open(consts.DECISION_TREE_MODEL, 'wb'))
    print(time()-start )
    print('Train model done!')

    print('Predicting model ...')
    Y_pred = dts.predict(X_test)
    print('Predict model done!')

    print(classification_report(Y_test, Y_pred,zero_division=1))
    print(f1_score(Y_test,Y_pred, average='macro'))

    # print(accuracy_score(y_true=Y_test, y_pred=Y_pred))

    # print(confusion_matrix(Y_test, Y_pred))


train_model()
