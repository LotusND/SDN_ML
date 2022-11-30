import pandas as pd
import matplotlib.pyplot as plt
import consts

from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn.pipeline import make_pipeline
from sklearn.naive_bayes import GaussianNB
from pickle import dump
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, f1_score


def train_model():
    print('Reading dataset ...')
    df = pd.read_csv(consts.DATASET_PATH_DROP)
    X = df.drop(['Label'], axis=1)  # drop colum Label X
    X = X.astype('float64')
    Y = df['Label']  # Y col Label
    print('Read data done!')

    print('Normalizing dataset ...')
    lb = LabelEncoder()
    Y = lb.fit_transform(Y)
    dump(lb, open(consts.Y_LABEL_ENCODER_MODEL, 'wb'))

    lb_name_mapping = dict(zip(lb.classes_, lb.transform(lb.classes_)))
    print(lb_name_mapping)

    scl = StandardScaler()
    X = scl.fit_transform(X)
    dump(scl, open(consts.X_STANDARD_SCALE_MODEL, 'wb'))
    print('Normalize data done!')

    print('Training model ...')
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=0, shuffle=True)

    gnb = GaussianNB()
    gnb.fit(X_train, Y_train)
    dump(gnb, open(consts.NAVIE_BAYES_MODEL, 'wb'))
    print('Train model done!')

    print('Predicting model ...')
    Y_pred = gnb.predict(X_test)
    print('Predict model done!')

    print(classification_report(Y_test, Y_pred))
    print(f1_score(Y_test, Y_pred, average='macro'))


    # print(accuracy_score(y_true=Y_test, y_pred=Y_pred))

    # print(confusion_matrix(Y_test, Y_pred))


train_model()
# concat_data("dataset/metasploitable-2.csv", "dataset/Normal_data.csv", "dataset/OVS.csv")
# concat_data("dataset/metasploitable-2.csv", "dataset/Normal_data.csv", "dataset/OVS_R.csv")
