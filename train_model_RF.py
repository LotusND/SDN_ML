import pandas as pd
import consts
from time import time
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from pickle import dump
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, f1_score


def train_model():
    print('Reading dataset ...')
    df = pd.read_csv(consts.DATASET_PATH_30)
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
    X = scl.fit_transform(X.to_numpy())
    dump(scl, open(consts.X_STANDARD_SCALE_MODEL, 'wb'))
    # print(scl.mean_)
    print('Normalize data done!')

    print('Training model ...')
    start = time()
    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=0.3, random_state=0)

    rfc = RandomForestClassifier(n_estimators=50,
                                 min_samples_split=2,
                                 min_samples_leaf=1,
                                max_depth=110,
                                 bootstrap=True,
                                 max_features='log2',
                                 )

    # rfc = RandomForestClassifier(n_estimators=100,
    #                              min_samples_split=2,
    #                              min_samples_leaf=1,
    #                              max_depth=120,
    #                              bootstrap=True,
    #                              max_features='sqrt'
    #                              )
    rfc.fit(X_train, Y_train)
    dump(rfc, open(consts.RANDOM_FOREST_MODEL, 'wb'))
    print(time()-start)
    print('Train model done!')

    print('Predicting model ...')
    Y_pred = rfc.predict(X_test)
    print('Predict model done!')

    print(classification_report(Y_test, Y_pred))
    print(f1_score(Y_test, Y_pred, average='macro'))

    # print(accuracy_score(y_true=Y_test, y_pred=Y_pred))

    # # print(confusion_matrix(Y_test, Y_pred))


train_model()
